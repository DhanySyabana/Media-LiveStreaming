import time
import m3u8
import socket
import struct
import logging
import datetime
import streamlink
from libs.Loggers import Loggers
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessorMetro import VideoProsessor

class KompasTV:

    def __init__(
            self,
            environment:str,
            url:str = None,
            quality:str = None,
            upload_location:str = None,
            headers: dict = None,
            converter_host: str = None,
            converter_port: int = None,
            buffer_size: int = None
        ) -> None:
        self.environment = environment
        self.url:str = url
        self.quality:str = quality
        self.start_process:bool = True
        self.upload_location:str = upload_location
        self.custom_headers:dict = headers
        self.video_duration = 5
        self.last_sequence = None
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        self.converter_host = converter_host
        self.converter_port = converter_port
        self.buffer_size = buffer_size
        self.cookies =  {
                "APISID": "j1x4MqaL_L-FGJUK/ArH3LiOKNwpPmF8Ac",
                "HSID": "AUDvag204WShBQnji",
                "LOGIN_INFO": "AFmmF2swRQIhAMKBDiRe4rN7_ncHPzVkdJg7Mtu8Hwe58gF3WFLzUkkNAiAh2RJ5CvRK2WRhKbP_uWaOnFyKoaReb-uZfLeihJbHsQ:QUQ3MjNmeXlpaVlKZ0l5dTd5eEs0dU9hZHEtZFlaUF9ad0hacDM4VHdReWQzU2NNR2F5NGN1YWwxWFNvMU5rZ29FNGcwTDREYUNKUGQ3U01QRnhlSXBLMXpRWkg1NUpaSGhXNWRpWGd1cDJBMUprbnJtdmg0bWVzQVg2emxlRW5kSEwwVmlBeDlCRExIQVkySExKNEg4MjRPVmdXZlAzbnRn",
                "NID": "517=4KR8sJ2RUF-efusAhIxZfs7RchiGeX8AiXzAcbUFVHB70ApQnzb2GqntFt4-vFLKjXsnMObOdAq_X7eHXHbbMbtVu1b0tRns6WJFdQoG1NtcfeE3CxJpnEz5EYVbkdRVv2zEyMj_mltJ1bZu3WeUFKcKUj9X3UUGVZHCSgXp6nUku4Qdw8rCCImkxn5c7q3tRu4Q57GLhaSlMEWU4hFlfzB4z6hCD6DbX-HJ7Qc_Fp34fEzt7L5Yny3-",
                "PREF": "f4=4000000&f6=40000000&tz=Asia.Jakarta",
                "SAPISID": "pObbQDAgEcYxvEy7/AkNH8dY7pLQJwC0m1",
                "SID": "g.a000oAi-3CHWHcjnnU_dipGlbj1fhd6FTWr-AwrfV_pZp5-LHPXb3YA5AmJiR9bxPamjPXC_XAACgYKAVESARUSFQHGX2MiimvElFDDhXq9SRTvErNdthoVAUF8yKouE__NhB00ozFLbfLCN1CL0076",
                "SSID": "A4OXeLiW9Zfe9XhBp"  # Dari .youtube.com
            }
        Loggers()
        super().__init__()

    def GetStreamSegment(self) -> list:
        file_segments = []
        print(self.url)
        
        try:
            session = streamlink.Streamlink()
            # Tambahkan cookie autentikasi
            session.set_option("http-cookies", self.cookies)
            # streams = streamlink.streams(self.url)
            streams = session.streams(self.url)
            stream_url = streams[self.quality]
            print(stream_url.args['url'])
            # exit()
            m3u8_obj = m3u8.load(stream_url.args['url'])

            segments = m3u8_obj.segments
            for segment in segments:
                file_segments.append({
                    "url": segment.uri,
                    "sequence": int(segment.uri.split("sq/")[1].split("/goap")[0])
                })
            file_segments = file_segments[-5:]
        except ValueError as e:
            file_segments = []
            logging.error(F"Error Get Stream Segment: {e}")
        except streamlink.exceptions.PluginError as e:
            file_segments = []
            logging.error(F"Error Get Stream Segment: {e}")

        return file_segments
    
    def RecordStream(self, segments:list) -> None:
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
                logging.info(F"Message from Server Converter: {response['message']}")
                self.last_sequence = response["sequence"]
                logging.info(F"Last Sequence: {self.last_sequence}")

            s.close()
            logging.info("Close Connection - Download Segment")
        return None
    
    def CheckTSFiles(self) -> dict:
        last_ts = F"{self.last_sequence}.ts"
        get_total_files = self.video_prosessor.GetTotalFiles(folder="ts", last_ts=last_ts)
        
        if get_total_files >= 120:
            list_files = self.video_prosessor.ListFiles(folder="ts", last_ts=last_ts)
            return dict(status=True, data_ts=list_files)
        
        return dict(status=False, data_ts=[])

    def StartEngine(self) -> None:
        logging.info("Start Engine")

        logging.info("Cleanup TS")
        self.video_prosessor.CleanUPTSFolder()

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
                    now_filename = F"METROTVSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
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
                        logging.info(F"Message from Server Converter: {response['message']}")

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
    ENGINE_NAME = "METROTVSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    kompas_tv = KompasTV(
        environment=ENGINE["ENVIRONMENT"],
        url=ENGINE["URL"],
        quality=ENGINE["QUALITY"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        converter_host=CONFIG.SOCKET_SERVER_METRO["HOST"],
        converter_port=CONFIG.SOCKET_SERVER_METRO["PORT"],
        buffer_size=CONFIG.SOCKET_SERVER_METRO["BUFFER_SIZE"]
    )
    kompas_tv.StartEngine()
    
