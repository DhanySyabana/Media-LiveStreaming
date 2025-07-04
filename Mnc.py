import time
import m3u8
import socket
import struct
import logging
import datetime
import streamlink
from libs.Loggers import Loggers
from libs.Selenium import Selenium
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessorMnc import VideoProsessor


class IDXIndonesiaV1:

    def __init__(self,
                 environment: str = None,
                 url: str = None,
                 resolution: str = None,
                 upload_location: str = None,
                 headers: dict = None,
                 playlist_directory: str = None,
                 converter_host: str = None,
                 converter_port: int = None,
                 buffer_size: int = None
                 ) -> None:
        self.environment = environment
        self.url = url
        self.resolution = resolution
        self.upload_location = upload_location
        self.headers = headers
        self.playlist_directory = playlist_directory
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        self.start_process = True
        self.video_duration = 10
        self.segment_status = None
        self.last_sequence = None
        self.converter_host = converter_host
        self.converter_port = converter_port
        self.buffer_size = buffer_size
        self.session = None
        self.LOGIN_REQUIRED_LIMIT = 5
        self.login_required_count = 0
        Loggers()
        super().__init__()

    def SetCookies(self):
        COOKIE_ENDPOINT = "https://siputri.onlinemonitoring.id/api/cookies/livestreaming?channel=MNCSTREAMING&source=Remote2"
        max_retry = 5
        for attempt in range(max_retry):
            try:
                resp = HTTPRequest("get", COOKIE_ENDPOINT, self.headers).Hit()
                if resp.status_code == 200:
                    cookies = resp.json()
                    session = streamlink.Streamlink()
                    session.set_option("http-cookies", cookies['data']['cookies'])
                    logging.info("[INFO] Cookies berhasil di-set")
                    self.session = session
                    return
                else:
                    logging.warning(f"[WARN] Gagal ambil cookies. Status: {resp.status_code} (attempt {attempt+1}/{max_retry})")
            except Exception as e:
                logging.warning(f"[WARN] Error saat ambil cookies: {e} (attempt {attempt+1}/{max_retry})")
            time.sleep(5)

        logging.error("[ERROR] Gagal 5x ambil cookies. Keluar.")
        exit(1)

    def GetPlaylistURI(self, url: str) -> str:
        playlist_uri = None
        logging.info(f"URL: {url}")

        try:
            response = self.session.http.get(url)
            if response.status_code == 200:
                m3u8_master = m3u8.loads(response.text)
                playlists = m3u8_master.data["playlists"]
                for playlist in playlists:
                    if playlist["stream_info"]["resolution"] == self.resolution:
                        playlist_uri = playlist['uri']
                        break
                logging.info("Get Playlist URI berhasil")
            else:
                logging.error(f"Error Get Playlist URI: {response.status_code}")
        except Exception as e:
            logging.error(f"Exception saat GetPlaylistURI: {e}")

        return playlist_uri

    def GetPlaylistEncrypted(self, selenium: None) -> str:
        path_uri = None
        driver = selenium.DriverSelenium()
        driver.get(self.url)

        while self.start_process:
            try:
                for request in driver.requests:
                    if request.response:
                        if self.playlist_directory in request.url:
                            path_uri = request.url
                            break
                    if path_uri is not None:
                        break
            except KeyError:
                logging.error("Error: KeyError saat mengambil request Selenium")
                self.start_process = False
                selenium.CloseDriver()
                break
            except KeyboardInterrupt:
                self.start_process = False
                selenium.CloseDriver()
                break
            if path_uri is not None:
                break

        logging.info(f"Path Playlist: {path_uri}")
        return path_uri

    def GetPlaylist(self) -> str:
        logging.info("Setup Selenium")
        selenium = Selenium(self.url, {"headless": True})
        selenium.SeleniumCapabilities()
        selenium.SeleniumOptions()

        logging.info("Mencari playlist...")
        playlist = self.GetPlaylistEncrypted(selenium)

        selenium.CloseDriver()
        logging.info("Tutup Selenium Driver")

        return playlist

    def GetSegments(self, playlist_uri: str) -> list:
        file_segments = []

        try:
            response = self.session.http.get(playlist_uri)
            if response.status_code == 200:
                m3u8_master = m3u8.loads(response.text)
                segments = m3u8_master.data["segments"]

                for segment in segments:
                    file_segments.append({
                        "url": f"{segment['uri']}",
                        "sequence": int(segment["uri"].split("seq=")[1].split(".ts")[0])
                    })
                file_segments = file_segments[-5:]
            else:
                logging.error(f"[ERROR] Gagal ambil segment. Status: {response.status_code}")
                self.segment_status = response.status_code

                if response.status_code == 403:
                    self.login_required_count += 1
                    logging.warning(f"[WARN] LOGIN_REQUIRED ke-{self.login_required_count}/{self.LOGIN_REQUIRED_LIMIT}")
                    if self.login_required_count >= self.LOGIN_REQUIRED_LIMIT:
                        logging.error("[ERROR] LOGIN_REQUIRED terlalu sering. Keluar.")
                        exit(1)
                    logging.info("Ambil ulang cookies karena 403")
                    self.SetCookies()
        except Exception as e:
            logging.error(f"Exception saat ambil segments: {e}")
            file_segments = []

        return file_segments

    def DownloadSegment(self, segments: list) -> None:
        logging.info("Request to Server Converter - Download Segment")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.converter_host, self.converter_port))

            to_server = {
                "event": "download",
                "environment": self.environment,
                "storage_path": self.upload_location,
                "method": "get",
                "segments": segments,
                "headers": self.headers
            }
            to_server = str(to_server).encode("utf-8")
            data_format = struct.Struct('I')
            data_length = len(to_server)
            s.sendall(data_format.pack(data_length))

            offset = 0
            while offset < data_length:
                sent_bytes = s.send(to_server[offset:])
                offset += sent_bytes

            response = s.recv(self.buffer_size)
            response = eval(response)
            if response:
                logging.info(f"Server response: {response['message']}")
                self.last_sequence = response["sequence"]

            s.close()
            logging.info("Tutup koneksi socket")

    def CheckTSFiles(self) -> dict:
        last_ts = f"{self.last_sequence}.ts"
        total = self.video_prosessor.GetTotalFiles(folder="ts", last_ts=last_ts)

        if total >= 60:
            files = self.video_prosessor.ListFiles(folder="ts", last_ts=last_ts)
            return dict(status=True, data_ts=files)
        return dict(status=False, data_ts=[])

    def StartEngine(self) -> None:
        logging.info("Start Engine")

        logging.info("Cleanup TS Folder")
        self.video_prosessor.CleanUPTSFolder()

        logging.info("Set Cookies")
        self.SetCookies()

        logging.info("Get Playlist Encrypted URL")
        playlist_encrypted = self.GetPlaylist()

        logging.info("Get Playlist URI")
        playlist_uri = self.GetPlaylistURI(playlist_encrypted)

        try:
            while self.start_process:
                if playlist_uri:
                    logging.info("Get Segment URI")
                    segments = self.GetSegments(playlist_uri)

                    while len(segments) == 0:
                        if self.segment_status in [403, 410, 404]:
                            playlist_encrypted = self.GetPlaylist()
                            playlist_uri = self.GetPlaylistURI(playlist_encrypted)
                        segments = self.GetSegments(playlist_uri)
                        time.sleep(self.video_duration)

                    time.sleep(self.video_duration)

                    try:
                        self.DownloadSegment(segments)
                    except (ConnectionResetError, ConnectionRefusedError):
                        while True:
                            try:
                                self.DownloadSegment(segments)
                                break
                            except (ConnectionResetError, ConnectionRefusedError):
                                logging.error("Retry Download Segment")
                                time.sleep(self.video_duration)

                    check = self.CheckTSFiles()
                    if check["status"]:
                        filename = f"MNCSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
                        logging.info("Request to Server Converter - Concat TS")
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.connect((self.converter_host, self.converter_port))

                            to_server = {
                                "event": "concat",
                                "environment": self.environment,
                                "storage_path": self.upload_location,
                                "mode": "w",
                                "filename": filename,
                                "optimize_video": True
                            }
                            to_server = str(to_server).encode("utf-8")
                            s.sendall(struct.Struct('I').pack(len(to_server)))
                            s.sendall(to_server)

                            response = s.recv(self.buffer_size)
                            response = eval(response)
                            logging.info(f"[INFO] Concat Result: {response['message']}")
                            s.close()

                        self.video_prosessor.CleanUPTSFolder(list_ts=check["data_ts"], metadata=filename)
                else:
                    playlist_encrypted = self.GetPlaylist()
                    playlist_uri = self.GetPlaylistURI(playlist_encrypted)
                    time.sleep(self.video_duration)
        except KeyboardInterrupt:
            self.start_process = False
            self.video_prosessor.CleanUPTSFolder()
            logging.info("Engine dihentikan")


if __name__ == "__main__":
    ENGINE_NAME = "MNCSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    idxindonesia = IDXIndonesiaV1(
        environment=ENGINE["ENVIRONMENT"],
        url=ENGINE["URLV1"],
        resolution=ENGINE["RESOLUTIONV1"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        playlist_directory=ENGINE["PLAYLIST_DIRECTORYV1"],
        converter_host=CONFIG.SOCKET_SERVER_MNC["HOST"],
        converter_port=CONFIG.SOCKET_SERVER_MNC["PORT"],
        buffer_size=CONFIG.SOCKET_SERVER_MNC["BUFFER_SIZE"]
    )
    idxindonesia.StartEngine()
