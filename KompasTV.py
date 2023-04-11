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
from libs.VideoProsessor import VideoProsessor

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
        self.duration_output = 60 * 10
        self.sequence = None
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        self.converter_host = converter_host
        self.converter_port = converter_port
        self.buffer_size = buffer_size
        Loggers()
        super().__init__()

    def GetStreamSegment(self) -> m3u8.model.Segment:
        stream_segment = None

        try:
            streams = streamlink.streams(self.url)
            stream_url = streams[self.quality]

            m3u8_obj = m3u8.load(stream_url.args['url'])
            stream_segment = m3u8_obj.segments[-1]

            if self.sequence is None:
                self.sequence = int(stream_segment.uri.split("sq/")[1].split("/goap")[0])
            else:
                self.sequence = self.sequence + 1
        except streamlink.exceptions.PluginError as e:
            stream_segment = None
            logging.error(F"Error Get Stream Segment: {e}")

        return stream_segment
    
    def RecordStream(self, stream_segment):
        logging.info("Request to Server Converter - Download Segment")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.converter_host, self.converter_port))

            to_server = {
                "event": "download",
                "environment": self.environment,
                "storage_path": self.upload_location,
                "method": "get",
                "url": stream_segment.uri,
                "headers": self.custom_headers,
                "sequence": self.sequence
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
        last_ts = F"{self.sequence}.ts"
        get_total_files = self.video_prosessor.GetTotalFiles(folder="ts", last_ts=last_ts)
        
        if get_total_files * self.video_duration == self.duration_output:
            list_files = self.video_prosessor.ListFiles(folder="ts", last_ts=last_ts)
            return dict(status=True, data_ts=list_files)
        
        return dict(status=False, data_ts=[])

    def StartEngine(self):
        logging.info("Start Engine")

        logging.info("Cleanup TS")
        self.video_prosessor.CleanUPTSFolder()

        try: 
            while self.start_process:

                logging.info("Get Stream Segment")
                stream_segment = self.GetStreamSegment()

                while stream_segment is None:
                    logging.info("Retrying Stream Segment")
                    stream_segment = self.GetStreamSegment()
                    time.sleep(self.video_duration - 3)

                logging.info("Record Stream")
                self.RecordStream(stream_segment)

                check_ts = self.CheckTSFiles()
                status_ts = check_ts["status"]
                data_ts = check_ts["data_ts"]

                if status_ts:
                    now_filename = F"KOMPASSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
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
    ENGINE_NAME = "KOMPASSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    kompas_tv = KompasTV(
        environment=ENGINE["ENVIRONMENT"],
        url=ENGINE["URL"],
        quality=ENGINE["QUALITY"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        converter_host=CONFIG.SOCKET_SERVER["HOST"],
        converter_port=CONFIG.SOCKET_SERVER["PORT"],
        buffer_size=CONFIG.SOCKET_SERVER["BUFFER_SIZE"]
    )
    kompas_tv.StartEngine()
    
