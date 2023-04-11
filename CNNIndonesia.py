import m3u8
import time
import socket
import struct
import logging
import datetime
from libs.Loggers import Loggers
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessor import VideoProsessor

class CNNIndonesia:

    def __init__(
            self,
            environment:str,
            host_directory:str = None,
            url_segment:str = None,
            upload_location:str = None,
            headers: dict = None,
            converter_host: str = None,
            converter_port: int = None,
            buffer_size: int = None
        ) -> None:
        self.environment = environment
        self.host_directory = host_directory
        self.url_segment = F"{host_directory}/{url_segment}"
        self.upload_location = upload_location
        self.custom_headers = headers
        self.start_process = True
        self.video_duration = 4
        self.duration_output = 60 * 10
        self.media_sequence = None
        self.converter_host = converter_host
        self.converter_port = converter_port
        self.buffer_size = buffer_size
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        Loggers()
        super().__init__()

    def GetSegment(self) -> str:
        url_segment = None

        response = HTTPRequest("get", self.url_segment, self.custom_headers).Hit()
        
        if response.status_code == 200:
            m3u8_master = m3u8.loads(response.text)
            m3u8_data = m3u8_master.data

            segments = m3u8_data["segments"]
            segment_uri = segments[-1]["uri"]

            if self.media_sequence is None:
                self.media_sequence = int(segment_uri.split("_")[4].split(".")[0])
            else:
                self.media_sequence += 1
            
            url_segment = F"{self.host_directory}/{segment_uri}"
        else:
            logging.error(F"Error Get Segments: {response.status_code}")
            
        return url_segment

    def DownloadSegment(self, segment_uri: str) -> None:
        logging.info("Request to Server Converter - Download Segment")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.converter_host, self.converter_port))

            to_server = {
                "event": "download",
                "environment": self.environment,
                "storage_path": self.upload_location,
                "method": "get",
                "url": segment_uri,
                "headers": self.custom_headers,
                "sequence": self.media_sequence
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
        return None
    
    def CheckTSFiles(self) -> dict:
        last_ts = F"{self.media_sequence}.ts"
        get_total_files = self.video_prosessor.GetTotalFiles(folder="ts", last_ts=last_ts)
        
        if get_total_files * self.video_duration == self.duration_output:
            list_files = self.video_prosessor.ListFiles(folder="ts", last_ts=last_ts)
            return dict(status=True, data_ts=list_files)
        
        return dict(status=False, data_ts=[])
    
    def StartEngine(self) -> None:
        logging.info("Start Engine")

        logging.info("Cleanup TS")
        self.video_prosessor.CleanUPTSFolder()

        try:
            while self.start_process:
                logging.info("Get Segment URI")
                segment_uri = self.GetSegment()

                while segment_uri is None:
                    logging.info("Retry Get Segment URI")
                    segment_uri = self.GetSegment()
                    time.sleep(self.video_duration - 2)

                logging.info("Download segment")
                self.DownloadSegment(segment_uri)
                
                check_ts = self.CheckTSFiles()
                status_ts = check_ts["status"]
                data_ts = check_ts["data_ts"]

                if status_ts:
                    now_filename = F"CNNSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"

                    logging.info("Request to Server Converter - Concat TS")
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.connect((self.converter_host, self.converter_port))

                        to_server = {
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

                    logging.info("Cleanup TS")
                    self.video_prosessor.CleanUPTSFolder(list_ts=data_ts, metadata=now_filename)
                
                time.sleep(self.video_duration)

        except KeyboardInterrupt:
            self.start_process = False
            logging.info("Stop Engine")

            self.video_prosessor.CleanUPTSFolder()
            logging.info("Cleanup TS")
            return None


if __name__ == "__main__":
    ENGINE_NAME = "CNNSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    cnnindonesia = CNNIndonesia(
        environment=ENGINE["ENVIRONMENT"],
        host_directory=ENGINE["HOST_DIRECTORY"],
        url_segment=ENGINE["URL_SEGMENT"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        converter_host=CONFIG.SOCKET_SERVER["HOST"],
        converter_port=CONFIG.SOCKET_SERVER["PORT"],
        buffer_size=CONFIG.SOCKET_SERVER["BUFFER_SIZE"]
    )
    cnnindonesia.StartEngine()
