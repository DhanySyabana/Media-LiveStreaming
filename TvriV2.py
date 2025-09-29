import time
import m3u8
import socket
import struct
import logging
import datetime
import requests
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from urllib import parse
from libs.Loggers import Loggers
from libs.Selenium import Selenium
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessor import VideoProsessor

class INewsV1:

    def __init__(
                self,
                environment:str,
                url:str,
                host_directory:str = None,
                search_ext:str = ".m3u8",
                resolution:str = None,
                upload_location = None,
                custom_headers:dict = None,
                converter_host: str = None,
                converter_port: int = None,
                buffer_size: int = None,
            ) -> None:
        self.environment = environment
        self.url = url
        self.host_directory = host_directory
        self.query = None
        self.search_ext = search_ext
        self.resolution = resolution
        self.upload_location = upload_location
        self.video_duration = 7
        self.custom_headers = custom_headers
        self.last_sequence = None
        self.start_process = True
        self.segment_status = None
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        self.converter_host = converter_host
        self.converter_port = converter_port
        self.buffer_size = buffer_size
        Loggers()
        super().__init__()

    def GetPlaylist(self, token:str) -> str:
        playlist_uri = None
        url = F"{self.host_directory}?auth="+token['auth']+"&trace_id="+token['trace_id']
        logging.info(F"URL: {url}")
        response = HTTPRequest("get", url, self.custom_headers).Hit()
        if response.status_code == 200:
            m3u8_master = m3u8.loads(response.text)
            playlists = m3u8_master.data["playlists"]
            for playlist in playlists:
                if playlist["stream_info"]["resolution"] == self.resolution:
                    playlist_uri = F"{playlist['uri']}"
                    self.query = playlist['uri']
                    response = HTTPRequest("get", playlist_uri, self.custom_headers).Hit()
                    break
            logging.info("Get Playlist Success")
        else:
            logging.error(F"Error Get Playlist: {response.status_code}")
        
        return playlist_uri
    
    def GetSegments(self, playlist_uri:str) -> list:
        file_segments = []

        response = HTTPRequest("get", playlist_uri, self.custom_headers).Hit()
        
        if response.status_code == 200:
            m3u8_master = m3u8.loads(response.text)
            m3u8_data = m3u8_master.data
            playlist_uri = playlist_uri.split("index.m3u8")[0]
            segments = m3u8_data["segments"]
            for segment in segments:
                file_segments.append({
                    "url": F"{playlist_uri}/{segment['uri']}",
                    "sequence": int(segment["uri"].split(".ts")[0])
                })

            file_segments = file_segments[-5:]
        else:
            file_segments = []
            self.segment_status = response.status_code
            logging.error(F"Error Get Segments: {response.status_code}")
        
        return file_segments
    
    def DownloadSegment(self, segments:list) -> None:
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
    
    def GetToken(self) -> str:
        token = None
        session = requests.session()
        token = session.post('https://www.vidio.com/live/6441/tokens', self.custom_headers)
        cookies = session.cookies.get_dict()

        page = json.loads(token.text)
        
        token ={
            'auth':page['token'].partition('&trace_id=')[0].replace('auth=',''),
            'trace_id':page['token'].partition('&trace_id=')[2]
        }

        return token
    

    def CheckTSFiles(self) -> dict:
        last_ts = F"{self.last_sequence}.ts"
        get_total_files = self.video_prosessor.GetTotalFiles(folder="ts", last_ts=last_ts)
        
        if get_total_files >= 63:
            list_files = self.video_prosessor.ListFiles(folder="ts", last_ts=last_ts)
            return dict(status=True, data_ts=list_files)
        
        return dict(status=False, data_ts=[])
        

    def StartEngine(self) -> None:
        logging.info("Start Engine")

        logging.info("Cleanup TS")
        self.video_prosessor.CleanUPTSFolder()

        logging.info("Get Token")
        token = self.GetToken()

        logging.info("Get Playlist URI")
        playlist_uri = self.GetPlaylist(token)
        
        try:
            while self.start_process:
                if playlist_uri is not None:
                    logging.info("Get Segment URI")
                    segments = self.GetSegments(playlist_uri)

                    while len(segments) == 0:
                        if self.segment_status == 403:
                            logging.info("Retry Get Token SDI")
                            token = self.GetToken()

                            logging.info("Retry Get Playlist URI")
                            playlist_uri = self.GetPlaylist(token)

                        if self.segment_status == 404:
                            logging.info("Retry Get Token SDI")
                            token = self.GetToken()

                            logging.info("Retry Get Playlist URI")
                            playlist_uri = self.GetPlaylist(token)

                        logging.info("Retry Get Segment URI")
                        segments = self.GetSegments(playlist_uri)
                        time.sleep(self.video_duration)

                    time.sleep(self.video_duration)
                    
                    logging.info("Download segment")
                    
                    try:
                        self.DownloadSegment(segments)
                    except ConnectionResetError or ConnectionRefusedError:
                        while True:
                            try:
                                self.DownloadSegment(segments)
                                break
                            except ConnectionResetError or ConnectionRefusedError:
                                logging.error("Retry Download Segment")
                                time.sleep(self.video_duration)
                                continue
                    
                    check_ts = self.CheckTSFiles()
                    status_ts = check_ts["status"]
                    data_ts = check_ts["data_ts"]

                    if status_ts:
                        now_filename = F"TVRISTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
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

                else:
                    logging.info("Retry Get Playlist URI")
                    playlist_uri = self.GetPlaylist(token)
                    time.sleep(self.video_duration)

        except KeyboardInterrupt:
            self.start_process = False
            logging.info("Stop Engine")

            self.video_prosessor.CleanUPTSFolder()
            logging.info("Cleanup TS")
            return None

if __name__ == "__main__":
    ENGINE_NAME = "TVRISTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    inews = INewsV1(
        environment=ENGINE["ENVIRONMENT"],
        url=ENGINE["URL"],
        host_directory=ENGINE["HOST_DIRECTORY"],
        resolution=ENGINE["RESOLUTION"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        custom_headers=ENGINE["HEADERS"],
        converter_host=CONFIG.SOCKET_SERVER["HOST"],
        converter_port=CONFIG.SOCKET_SERVER["PORT"],
        buffer_size=CONFIG.SOCKET_SERVER["BUFFER_SIZE"],
    )
    inews.StartEngine()   
