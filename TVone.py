import time
import m3u8
import socket
import struct
import logging
import datetime
import requests
import streamlink
import random
import sys, json
from libs.Loggers import Loggers
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessorTvone import VideoProsessor
# from libs.Youtube import get_youtube

class MNC:

    def __init__(
            self,
            environment: str,
            url: str = None,
            quality: str = None,
            upload_location: str = None,
            headers: dict = None,
            converter_host: str = None,
            converter_port: int = None,
            buffer_size: int = None,
            id_channel: str = None,
            failure_count: int = 0
        ) -> None:
        self.environment = environment
        self.url = url
        self.quality = quality
        self.start_process = True
        self.upload_location = upload_location
        self.custom_headers = headers
        self.video_duration = 2
        self.last_sequence = None
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        self.converter_host = converter_host
        self.converter_port = converter_port
        self.buffer_size = buffer_size
        self.id_channel = id_channel
        self.failure_count = failure_count
        Loggers()
        self.session = None    


    def SetCookies(self):
        COOKIE_ENDPOINT = "https://siputri.onlinemonitoring.id/api/cookies/livestreaming?channel=TVONESTREAMING&source=Remote1"
        max_retry = 5
        for attempt in range(max_retry):
            try:
                resp = requests.get(COOKIE_ENDPOINT, timeout=5, allow_redirects=False)
                logging.info(f"[DEBUG] Status Code: {resp.status_code}")
                if resp.status_code == 200:
                    cookies = resp.text
                    cookies = json.loads(cookies)
                    self.url = cookies['data']['url']
                    session = streamlink.Streamlink()
                    session.set_option("http-cookies", cookies['data']['cookies'])
                    logging.info("[INFO] Cookies set")
                    self.session = session  
                    return
                else:
                    logging.warning(f"[WARN] Error, Status Code: {resp.status_code}, (attempt {attempt+1}/{max_retry})")
            except requests.RequestException as e:
                logging.warning(f"[WARN] Gagal total ambil cookies: {e} (attempt {attempt+1}/{max_retry})")
            time.sleep(5)
        logging.error("[ERROR] Gagal 5x dalam mengambil cookies. Exiting.")
        sys.exit(1)


    def GetStreamSegment(self) -> list:
        file_segments = []
        break_point = 0
        try:
            while True:
                session = self.session

                try:
                    streams = session.streams(self.url)
                except Exception as e:
                    if "LOGIN_REQUIRED" in str(e):
                        self.login_required_count += 1
                        logging.warning(f"[WARN] LOGIN_REQUIRED ke-{self.login_required_count}/{self.LOGIN_REQUIRED_LIMIT}")
                        if self.login_required_count >= self.LOGIN_REQUIRED_LIMIT:
                            logging.error("[ERROR] LOGIN_REQUIRED terjadi terlalu sering. Keluar.")
                            exit(1)
                        logging.info("Ambil ulang cookies karena LOGIN_REQUIRED...")
                        self.FetchCookies()
                        continue
                    else:
                        logging.error(f"[ERROR] Gagal dapat stream: {e}")
                        continue
                
                if self.quality not in str(streams):
                    logging.error("No streams found")
                    # self.url = get_youtube(self.id_channel)
                    break_point += 1
                    if break_point >= 5:    
                        logging.error("Gagal Get URL")
                        exit()
                        break
                    continue
                
                stream_url = streams[self.quality]

                m3u8_obj = m3u8.load(stream_url.args['url'])

                segments = m3u8_obj.segments
                for segment in segments:
                    file_segments.append({
                        "url": segment.uri,
                        "sequence": int(segment.uri.split("sq/")[1].split("/goap")[0])
                    })
                file_segments = file_segments[-5:]
                break
        except ValueError as e:
            file_segments = []
            logging.error(f"Error Get Stream Segment: {e}")
        except streamlink.exceptions.PluginError as e:
            file_segments = []
            logging.error(f"Error Get Stream Segment: {e}")

        return file_segments
    
    def RecordStream(self, segments: list) -> None:
        logging.info("Request to Server Converter - Download Segment")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.converter_host, self.converter_port))

            to_server = {
                "event": "download",
                "environment": self.environment,
                "storage_path": self.upload_location,
                "method": "get",
                "segments": segments,
                "headers": self.custom_headers
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
                logging.info(f"Message from Server Converter: {response['message']}")
                self.last_sequence = response["sequence"]
                logging.info(f"Last Sequence: {self.last_sequence}")

            s.close()
            logging.info("Close Connection - Download Segment")
        return None
    
    def CheckTSFiles(self) -> dict:
        last_ts = f"{self.last_sequence}.ts"
        get_total_files = self.video_prosessor.GetTotalFiles(folder="ts", last_ts=last_ts)
        
        if get_total_files >= 300:
            list_files = self.video_prosessor.ListFiles(folder="ts", last_ts=last_ts)
            return dict(status=True, data_ts=list_files)
        
        return dict(status=False, data_ts=[])

    def StartEngine(self) -> None:
        logging.info("Start Engine")

        logging.info("Cleanup TS")
        self.video_prosessor.CleanUPTSFolder()
        logging.info("Get Live URL Youtube")
        # self.url = get_youtube(self.id_channel)
        self.SetCookies()

        try: 
            while self.start_process:
                logging.info("Get Stream Segment")
                segments = self.GetStreamSegment()

                while len(segments) == 0:
                    logging.info("Retrying Stream Segment")
                    segments = self.GetStreamSegment()
                    time.sleep(self.video_duration)

                time.sleep(self.video_duration)

                logging.info("Record Stream")
                try:
                    self.RecordStream(segments)
                except ConnectionResetError or ConnectionRefusedError:
                    while True:
                        try:
                            self.RecordStream(segments)
                            break
                        except ConnectionResetError or ConnectionRefusedError:
                            logging.error("Retry Download Segment")
                            time.sleep(self.video_duration)
                            continue
                
                check_ts = self.CheckTSFiles()
                status_ts = check_ts["status"]
                data_ts = check_ts["data_ts"]

                if status_ts:
                    now_filename = f"TVONESTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
                    logging.info("Request to Server Converter - Concat TS")
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((self.converter_host, self.converter_port))

                        to_server = {
                            "event": "concat",
                            "environment": self.environment,
                            "storage_path": self.upload_location,
                            "mode": "w",
                            "filename": now_filename,
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
                        logging.info(f"Message from Server Converter: {response['message']}")

                        s.close()
                        logging.info("Close Connection - Concat TS")

                    logging.info("Cleanup TS")
                    self.video_prosessor.CleanUPTSFolder(list_ts=data_ts, metadata=now_filename)
                
        except KeyboardInterrupt:
            self.start_process = False
            logging.info("Stop Engine")

            self.video_prosessor.CleanUPTSFolder()
            logging.info("Cleanup TS")
            return None

if __name__ == "__main__":
    ENGINE_NAME = "TVONESTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    kompas_tv = MNC(
        environment=ENGINE["ENVIRONMENT"],
        url=ENGINE["URL"],
        quality=ENGINE["QUALITY"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        # id_channel=ENGINE["ID_CHANNEL"],
        converter_host=CONFIG.SOCKET_SERVER_TVONE["HOST"],
        converter_port=CONFIG.SOCKET_SERVER_TVONE["PORT"],
        buffer_size=CONFIG.SOCKET_SERVER_TVONE["BUFFER_SIZE"]
    )
    kompas_tv.StartEngine()
