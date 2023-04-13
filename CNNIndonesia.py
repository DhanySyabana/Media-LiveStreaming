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
            upload_location:str = None,
            headers: dict = None,
            converter_host: str = None,
            converter_port: int = None,
            buffer_size: int = None,
            playlist: str = None,
            resolution: str = None
        ) -> None:
        self.environment = environment
        self.host_directory = host_directory
        self.url_segment = None
        self.upload_location = upload_location
        self.custom_headers = headers
        self.start_process = True
        self.video_duration = 4
        self.duration_output = 10
        self.last_sequence = None
        self.converter_host = converter_host
        self.converter_port = converter_port
        self.buffer_size = buffer_size
        self.playlist = playlist
        self.resolution = resolution
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        Loggers()
        super().__init__()

    def GetSegment(self) -> list:
        file_segments = []

        response = HTTPRequest("get", self.url_segment, self.custom_headers).Hit()
        
        if response.status_code == 200:
            m3u8_master = m3u8.loads(response.text)
            m3u8_data = m3u8_master.data

            segments = m3u8_data["segments"]
            for segment in segments:
                file_segments.append({
                    "url": F"{self.host_directory}/{segment['uri']}",
                    "sequence": int(segment["uri"].split("_")[4].split(".")[0])
                })
            file_segments = file_segments[-5:]
        else:
            file_segments = []
            logging.error(F"Error Get Segments: {response.status_code}")
            
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
        logging.info(F"Last TS: {last_ts}")
        get_total_files = self.video_prosessor.GetTotalFiles(folder="ts", last_ts=last_ts)
        
        if get_total_files >= 150:
            list_files = self.video_prosessor.ListFiles(folder="ts", last_ts=last_ts)
            return dict(status=True, data_ts=list_files)    
        
        return dict(status=False, data_ts=[])
    
    def GetPlaylist(self) -> str:
        playlist_uri = None
        url = F"{self.host_directory}/{self.playlist}"
        logging.info(F"URL: {url}")

        response = HTTPRequest("get", url, self.custom_headers).Hit()
        if response.status_code == 200:
            m3u8_master = m3u8.loads(response.text)
            playlists = m3u8_master.data["playlists"]
            for playlist in playlists:
                if playlist["stream_info"]["resolution"] == self.resolution:
                    playlist_uri = F"{self.host_directory}/{playlist['uri']}"
                    break
            logging.info("Get Playlist Success")
        else:
            logging.error(F"Error Get Playlist: {response.status_code}")
        
        return playlist_uri
    
    def StartEngine(self) -> None:
        logging.info("Start Engine")

        logging.info("Cleanup TS")
        self.video_prosessor.CleanUPTSFolder()

        logging.info("Get Playlist URI")
        self.url_segment = self.GetPlaylist()

        try:
            while self.start_process:
                logging.info("Get Segment URI")
                segments = self.GetSegment()

                while len(segments) == 0:
                    logging.info("Retry Get Segment URI")
                    segments = self.GetSegment()
                    time.sleep(self.video_duration)

                time.sleep(self.video_duration)

                logging.info("Download segment")
                self.DownloadSegment(segments)
                
                check_ts = self.CheckTSFiles()
                status_ts = check_ts["status"]
                data_ts = check_ts["data_ts"]

                if status_ts:
                    now_filename = F"CNNSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"

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
    ENGINE_NAME = "CNNSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    cnnindonesia = CNNIndonesia(
        environment=ENGINE["ENVIRONMENT"],
        host_directory=ENGINE["HOST_DIRECTORY"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        converter_host=CONFIG.SOCKET_SERVER["HOST"],
        converter_port=CONFIG.SOCKET_SERVER["PORT"],
        buffer_size=CONFIG.SOCKET_SERVER["BUFFER_SIZE"],
        playlist=ENGINE["PLAYLIST"],
        resolution=ENGINE["RESOLUTION"],
    )
    cnnindonesia.StartEngine()
