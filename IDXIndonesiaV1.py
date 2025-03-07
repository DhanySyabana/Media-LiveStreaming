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
from libs.VideoProsessorIDX import VideoProsessor

from settings.Connector import get_channel_data

class IDX:

    def __init__(
            self,
            environment:str,
            url:str = None,
            quality:str = None,
            upload_location:str = None,
            headers: dict = None,
            converter_host: str = None,
            converter_port: int = None,
            buffer_size: int = None,
            cookies: str = None
        ) -> None:
        self.environment = environment
        self.url:str = url
        self.quality:str = quality
        self.start_process:bool = True
        self.upload_location:str = upload_location
        self.custom_headers:dict = headers
        self.video_duration = 5
        self.last_sequence = None
        self.cookies = cookies
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        self.converter_host = converter_host
        self.converter_port = converter_port
        self.buffer_size = buffer_size
        Loggers()
        super().__init__()

    def GetStreamSegment(self) -> list:
        file_segments = []
        print(self.url)
        try:
            
            session = streamlink.Streamlink()
            # proxy_list = list({'trkcytfh:xtfqu68rlqwr@192.46.187.70:6648','trkcytfh:xtfqu68rlqwr@72.46.139.81:6641','trkcytfh:xtfqu68rlqwr@192.53.70.221:5935'})
            # proxy_list = random.choice(proxy_list)
            # proxy_url = "socks5://" + proxy_list
            # Tambahkan cookie autentikasi
            # with open('cookies.txt', 'r') as file:
            
            # print(self.cookies)
            session.set_option("http-cookies", self.cookies)
            # session.set_option("http-proxy", proxy_url)
            # streams = streamlink.streams(self.url)
            streams = session.streams(self.url)
    
            # print(streams)
            stream_url = streams[self.quality]
            # print(stream_url.ar)
            # exit()
            print(stream_url.to_url())
            # exit()
            response =HTTPRequest("get", stream_url.to_url(), headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114    ',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8'
            }).Hit()
            if response.status_code == 200:
                m3u8_obj = m3u8.loads(response.text)
                segments = m3u8_obj.segments
                for segment in segments:
                    file_segments.append({
                        "url": segment.uri,
                        "sequence": int(segment.uri.split("sq/")[1].split("/goap")[0])
                    })
                
                file_segments = file_segments[-5:]
            else:
                file_segments = []
                self.segment_status = response.status_code
                logging.error(F"Error Get Segments: {response.status_code}")
            
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
                    now_filename = F"IDXSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
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
    ENGINE_NAME = "IDXSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    kompas_tv = IDX(
        environment=ENGINE["ENVIRONMENT"],
        url=get_channel_data(ENGINE_NAME)[0]['url'],
        quality=get_channel_data(ENGINE_NAME)[0]['resolusi'],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        cookies=get_channel_data(ENGINE_NAME)[0]['cookies'],
        converter_host=CONFIG.SOCKET_SERVER_KOMPAS["HOST"],
        converter_port=CONFIG.SOCKET_SERVER_KOMPAS["PORT"],
        buffer_size=CONFIG.SOCKET_SERVER_KOMPAS["BUFFER_SIZE"]
    )
    kompas_tv.StartEngine()
    
