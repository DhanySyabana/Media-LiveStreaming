import time
import m3u8
import socket
import struct
import logging
import datetime
from urllib import parse
from libs.Loggers import Loggers
from libs.Selenium import Selenium
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessor import VideoProsessor

class inews:

    def __init__(self, 
                 environment:str = None,
                 url:str = None,
                 resolution:str = None,
                 upload_location:str = None,
                 headers:dict = None,
                 playlist_directory:str = None,
                 converter_host:str = None,
                 converter_port:int = None,
                 buffer_size:int = None
                 ) -> None:
        self.environment:str = environment
        self.url:str = url
        self.resolution:str = resolution
        self.upload_location:str = upload_location
        self.headers:dict = headers
        self.playlist_directory:str = playlist_directory
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        self.start_process = True
        self.video_duration = 10
        self.segment_status = None
        self.last_sequence = None
        self.converter_host = converter_host
        self.converter_port = converter_port
        self.buffer_size = buffer_size
        Loggers()
        super().__init__()

    def GetPlaylistURI(self, url:str) -> str:
        playlist_uri = None
        logging.info(F"URL: {url}")

        response = HTTPRequest("get", url, self.headers).Hit()
        if response.status_code == 200:
            m3u8_master = m3u8.loads(response.text)
            playlists = m3u8_master.data["playlists"]
            for playlist in playlists:
                if playlist["stream_info"]["resolution"] == self.resolution:
                    playlist_uri = playlist['uri']
                    break
            logging.info("Get Playlist Success")
        else:
            logging.error(F"Error Get Playlist: {response.status_code}")
        
        return playlist_uri

    def GetPlaylistEncrypted(self, selenium:None) -> str:
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
                logging.error("Error: KeyError")
                self.start_process = False
                selenium.CloseDriver()
                break
            except KeyboardInterrupt:
                self.start_process = False
                selenium.CloseDriver()
                break
            if path_uri is not None:
                break
        
        logging.info(F"Path Playlist: {path_uri}")
        return path_uri

    def GetPlaylist(self) -> str:
        logging.info("Setup Selenium")
        selenium = Selenium(self.url, {
            "headless": True,
        })

        selenium.SeleniumCapabilities()
        logging.info("Setup Selenium Capabilities")

        selenium.SeleniumOptions()
        logging.info("Setup Selenium Options")

        logging.info("Find Playlist")
        playlist = self.GetPlaylistEncrypted(selenium)

        selenium.CloseDriver()
        logging.info("Close Selenium Driver")
        
        return playlist
    
    def GetSegments(self, playlist_uri:str) -> list:
        file_segments = []

        response = HTTPRequest("get", playlist_uri, self.headers).Hit()
        
        if response.status_code == 200:
            m3u8_master = m3u8.loads(response.text)
            m3u8_data = m3u8_master.data

            segments = m3u8_data["segments"]

            url_host = parse.urlparse(playlist_uri).scheme + "://" + parse.urlparse(playlist_uri).netloc

            for segment in segments:
                url  = F"{url_host}/joss/134/inews/{segment['uri']}"
                file_segments.append({
                    "url": url,
                    "sequence": int(segment["uri"].split("sleng_")[1].split(".ts")[0])
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
                logging.info(F"Message from Server Converter: {response['message']}")
                self.last_sequence = response["sequence"]
                logging.info(F"Last Sequence: {self.last_sequence}")
            
            s.close()
            logging.info("Close Connection - Download Segment")
        return None
    
    def CheckTSFiles(self) -> dict:
        last_ts = F"{self.last_sequence}.ts"
        get_total_files = self.video_prosessor.GetTotalFiles(folder="ts", last_ts=last_ts)
        
        if get_total_files >= 60:
            list_files = self.video_prosessor.ListFiles(folder="ts", last_ts=last_ts)
            return dict(status=True, data_ts=list_files)
        
        return dict(status=False, data_ts=[])

    def StartEngine(self) -> None:
        logging.info("Start Engine")

        logging.info("Cleanup TS")
        self.video_prosessor.CleanUPTSFolder()

        logging.info("Get Playslist Encrypted")
        playlist_encrypted = self.GetPlaylist()

        logging.info("Get Playlist")
        playlist_uri = self.GetPlaylistURI(playlist_encrypted)

        try:
            while self.start_process:
                if playlist_uri is not None:
                    logging.info("Get Segment URI")
                    segments = self.GetSegments(playlist_uri)

                    while len(segments) == 0:
                        if self.segment_status == 403 or self.segment_status == 410:
                            logging.info("Retry Get Playlist URI - Get Playslist Encrypted")
                            playlist_encrypted = self.GetPlaylist()

                            playlist_uri = self.GetPlaylistURI(playlist_encrypted)

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
                        now_filename = F"INEWSSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
                        logging.info("Request to Server Converter - Concat TS")
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.connect((self.converter_host, self.converter_port))

                            to_server = {
                                "event": "concat",
                                "environment": self.environment,
                                "storage_path": self.upload_location,
                                "mode": "w",
                                "filename": now_filename,
                                "optimize_video" : True,
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
                    logging.info("Retry Get Playlist URI - Get Playslist Encrypted")
                    playlist_encrypted = self.GetPlaylist()

                    playlist_uri = self.GetPlaylistURI(playlist_encrypted)
                    time.sleep(self.video_duration)

        except KeyboardInterrupt:
            self.start_process = False
            logging.info("Stop Engine")

            self.video_prosessor.CleanUPTSFolder()
            logging.info("Cleanup TS")
            return None


if __name__ == "__main__":
    ENGINE_NAME = "INEWSSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    inews = inews(
        environment=ENGINE["ENVIRONMENT"],
        url=ENGINE["URLV1"],
        resolution=ENGINE["RESOLUTIONV1"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        playlist_directory=ENGINE["PLAYLIST_DIRECTORYV1"],
        converter_host=CONFIG.SOCKET_SERVER["HOST"],
        converter_port=CONFIG.SOCKET_SERVER["PORT"],
        buffer_size=CONFIG.SOCKET_SERVER["BUFFER_SIZE"]
    )
    inews.StartEngine()