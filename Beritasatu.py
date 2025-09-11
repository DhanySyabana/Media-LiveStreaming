import os, re, time, socket, struct, logging, datetime as dt, requests, m3u8, sys
from settings.Config import Config
import urllib3
from libs.VideoProsessorBeritasatuAudio import VideoProsessor as AudioProc
from libs.VideoProsessorBeritasatuVideo import VideoProsessor as VideoProc

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === Ambil daftar segmen m3u8 ===
def get_segments(host, playlist, headers):
    url = f"{host}/{playlist}"
    r = requests.get(url, headers=headers, verify=False)
    if r.status_code != 200:
        logging.error(f"[STREAM] Gagal ambil playlist {url} - status {r.status_code}")
        return []
    m = m3u8.loads(r.text)
    return [
        {"url": f"{host}/{s.uri}", "sequence": re.sub(r"\D", "", s.uri)}
        for s in m.segments
    ][-5:]

# === Kirim perintah download / concat ke server converter ===
def send_to_converter(sock_conf, payload):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        data = str(payload).encode("utf-8")
        s.connect((sock_conf["HOST"], sock_conf["PORT"]))
        s.sendall(struct.pack("I", len(data)))
        s.sendall(data)
        resp = s.recv(sock_conf["BUFFER_SIZE"])
    return eval(resp)

# === Hitung jumlah file TS di folder tertentu ===
def count_files(proc, folder, last_seq):
    return proc.GetTotalFiles(folder=folder, last_ts=f"{last_seq}.ts")

# === Gabungkan audio & video jadi 1 file mp4 ===
def mux_av(upload_location, filename):
    ts_folder = os.path.join(upload_location, "ts")
    final_folder = upload_location   # simpan final di folder utama
    final = os.path.join(final_folder, f"{filename}.mp4")

    video = os.path.join(ts_folder, f"{filename}.mp4")
    audio = os.path.join(ts_folder, f"{filename}.mp3")

    # Mux dengan ffmpeg tanpa menampilkan log di terminal
    if os.name == "nt":  # Windows
        ffmpeg_cmd = f'ffmpeg -y -i "{video}" -i "{audio}" -c copy "{final}" > NUL 2>&1'
    else:               # Linux/Mac
        ffmpeg_cmd = f'ffmpeg -y -i "{video}" -i "{audio}" -c copy "{final}" > /dev/null 2>&1'

    os.system(ffmpeg_cmd)
    logging.info(f"[DONE] File final: {final}")


    # Bersihkan mp3 & mp4 sementara
    for f in [video, audio]:
        if os.path.exists(f):
            os.remove(f)
            logging.info(f"[CLEAN] Hapus MP3 & MP4: {f}")

    # Bersihkan semua TS & TXT juga
    for root, dirs, files in os.walk(ts_folder):
        for file in files:
            if file.endswith(".ts") or file.endswith(".txt"):
                try:
                    os.remove(os.path.join(root, file))
                    logging.info(f"[CLEAN] Hapus sementara: {file}")
                except Exception as e:
                    logging.warning(f"[WARN] Gagal hapus {file}: {e}")

    return final


# === Bersihkan sisa TS/TXT di semua folder ===
def clean_ts(upload_location):
    for folder_name in ["ts", "audio", "video"]:
        folder = os.path.join(upload_location, folder_name)
        if os.path.exists(folder):
            for f in os.listdir(folder):
                if f.endswith(".ts") or f.endswith(".txt"):
                    try:
                        os.remove(os.path.join(folder, f))
                    except Exception as e:
                        logging.warning(f"[CLEAN] Gagal hapus {f}: {e}")

# ========================== MAIN ==========================

if __name__ == "__main__":
    CONFIG = Config()
    ENG = CONFIG.ENGINE["BERITASATUSTREAMING"]

    AUD = {
        "ENVIRONMENT": ENG["ENVIRONMENT"],
        "HOST_DIRECTORY": ENG["HOST_DIRECTORY"],
        "UPLOAD_LOCATION": ENG["UPLOAD_LOCATION"],
        "HEADERS": ENG["HEADERS"],
        "PLAYLIST": ENG["PLAYLIST_AUDIO"],
        "RESOLUTION": ENG["RESOLUTION"]
    }

    VID = {
        "ENVIRONMENT": ENG["ENVIRONMENT"],
        "HOST_DIRECTORY": ENG["HOST_DIRECTORY"],
        "UPLOAD_LOCATION": ENG["UPLOAD_LOCATION"],
        "HEADERS": ENG["HEADERS"],
        "PLAYLIST": ENG["PLAYLIST_VIDEO"],
        "RESOLUTION": ENG["RESOLUTION"]
    }

    audio_proc = AudioProc(environment=AUD["ENVIRONMENT"], storage_path=AUD["UPLOAD_LOCATION"])
    video_proc = VideoProc(environment=VID["ENVIRONMENT"], storage_path=VID["UPLOAD_LOCATION"])

    last_audio = last_video = None
    N = 100  # jumlah segmen minimal sebelum concat

    try:
        while True:
            seg_aud = get_segments(AUD["HOST_DIRECTORY"], AUD["PLAYLIST"], AUD["HEADERS"])
            seg_vid = get_segments(VID["HOST_DIRECTORY"], VID["PLAYLIST"], VID["HEADERS"])

            if seg_aud:
                resp = send_to_converter(CONFIG.SOCKET_SERVER_BERITASATU_AUDIO, {
                    "event": "download",
                    "environment": AUD["ENVIRONMENT"],
                    "storage_path": AUD["UPLOAD_LOCATION"],
                    "method": "get",
                    "segments": seg_aud,
                    "headers": AUD["HEADERS"]
                })
                if resp and resp.get("sequence"):
                    last_audio = resp["sequence"]

            if seg_vid:
                resp = send_to_converter(CONFIG.SOCKET_SERVER_BERITASATU_VIDEO, {
                    "event": "download",
                    "environment": VID["ENVIRONMENT"],
                    "storage_path": VID["UPLOAD_LOCATION"],
                    "method": "get",
                    "segments": seg_vid,
                    "headers": VID["HEADERS"]
                })
                if resp and resp.get("sequence"):
                    last_video = resp["sequence"]

            # === cek jumlah ts ===
            if last_audio and last_video:
                ca = count_files(audio_proc, "audio", last_audio)
                cv = count_files(video_proc, "video", last_video)
                logging.info(f"[COUNT] Audio TS: {ca}, Video TS: {cv}")

                # === jika cukup segmen, concat dan mux ===
                if ca >= N and cv >= N:
                    now_filename = f"BERITASATUSTREAMING_{dt.datetime.now().strftime('%m-%d-%H-%M-%S')}"
                    logging.info(f"[PROCESS] Mulai concat dengan nama file: {now_filename}")

                    send_to_converter(CONFIG.SOCKET_SERVER_BERITASATU_VIDEO, {
                        "event": "concat",
                        "environment": VID["ENVIRONMENT"],
                        "storage_path": VID["UPLOAD_LOCATION"],
                        "mode": "w",
                        "filename": now_filename
                    })

                    send_to_converter(CONFIG.SOCKET_SERVER_BERITASATU_AUDIO, {
                        "event": "concat",
                        "environment": AUD["ENVIRONMENT"],
                        "storage_path": AUD["UPLOAD_LOCATION"],
                        "mode": "w",
                        "filename": now_filename
                    })

                    mux_av(VID["UPLOAD_LOCATION"], now_filename)

                    # Bersihkan segmen setelah selesai
                    clean_ts(VID["UPLOAD_LOCATION"])
                    clean_ts(AUD["UPLOAD_LOCATION"])
                    last_audio = last_video = None

            time.sleep(3)

    except KeyboardInterrupt:
        logging.warning("[STOP] Program dihentikan paksa (Ctrl+C)")
        clean_ts(VID["UPLOAD_LOCATION"])
        clean_ts(AUD["UPLOAD_LOCATION"])
        sys.exit(0)
