import time
import m3u8
import logging
import datetime
from urllib import parse
from libs.Loggers import Loggers
from libs.Selenium import Selenium
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessor import VideoProsessor

class INews:

    def __init__(
                self,
                environment:str,
                url:str,
                sdi:str = "inews-sdi.m3u8",
                host_directory:str = "https://d-inews.rctiplus.id",
                search_ext:str = ".m3u8",
                auth_key:str = "auth_key",
                resolution:str = "640x360",
                upload_location = None,
                delay_duration:int = 8,
                mp4_duration:int = 660,
                custom_headers:dict = {
                    'origin': 'https://embed.rctiplus.com',
                    'referer': 'https://embed.rctiplus.com',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
                }) -> None:
        self.environment = environment
        self.url = url
        self.sdi = sdi
        self.host_directory = host_directory
        self.search_ext = search_ext
        self.auth_key = auth_key
        self.resolution = resolution
        self.upload_location = upload_location
        self.delay_duration = delay_duration
        self.mp4_duration = mp4_duration
        self.custom_headers = custom_headers
        self.start_process = True
        self.start_time = time.time()
        self.sequence = None
        self.segment_status = None
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        Loggers()
        super().__init__()

    def GetTokenSDI(self, selenium:None) -> str:
        token_uri = None
        driver = selenium.DriverSelenium()
        driver.get(self.url)

        while self.start_process:
            try:
                for request in driver.requests:
                    if request.response:
                        if self.search_ext in request.url and F"{self.host_directory}/" in request.url:
                            params = parse.parse_qs(parse.urlparse(request.url).query)
                            token_uri = params[self.auth_key][0]
                            break
                    if token_uri is not None:
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
            if token_uri is not None:
                break
        
        logging.info(F"Token SDI: {token_uri}")
        return token_uri
    
    def GetPlaylist(self, token_sdi) -> str:
        playlist_uri = None
        url = F"{self.host_directory}/{self.sdi}?{self.auth_key}={token_sdi}"
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
    
    def GetSegments(self, playlist_uri) -> str:
        url_segment = None

        response = HTTPRequest("get", playlist_uri, self.custom_headers).Hit()
        
        if response.status_code == 200:
            m3u8_master = m3u8.loads(response.text)
            m3u8_data = m3u8_master.data

            segments = m3u8_data["segments"]
            segment_uri = segments[0]["uri"]
            
            url_segment = F"{self.host_directory}/{segment_uri}"
            
            if self.sequence is None:
                self.sequence = int(url_segment.split("seq=")[1].split(".ts")[0])
            else:
                self.sequence = self.sequence + 1
        else:
            url_segment = None
            self.segment_status = response.status_code
            logging.error(F"Error Get Segments: {response.status_code}")
        
        return url_segment
    
    def DownloadSegment(self, segment_uri:str) -> None:
        response = HTTPRequest("get", segment_uri, self.custom_headers).Hit()
        if response.status_code == 200:
            file_name = F"{self.sequence}.ts"
            
            self.video_prosessor.WriteFile(
                file_name=file_name,
                content=response.content,
                mode="wb",
                folder="ts"
            )
            logging.info(F"Success Download Segment: {file_name}")
        else:
            logging.error(F"Error Download Segment: {response.status_code}")
        logging.info(F"Succes Download Segment")
        return None
    
    def GetToken(self) -> str:
        logging.info("Setup Selenium")
        selenium = Selenium(self.url, {
            "headless": True,
        })

        selenium.SeleniumCapabilities()
        logging.info("Setup Selenium Capabilities")

        selenium.SeleniumOptions()
        logging.info("Setup Selenium Options")

        logging.info("Get Token SDI")
        token = self.GetTokenSDI(selenium)

        selenium.CloseDriver()
        logging.info("Close Selenium Driver")
        
        return token
        

    def StartEngine(self) -> None:
        logging.info("Start Engine")

        logging.info("Cleanup TS")
        self.video_prosessor.CleanUPTSFolder()

        logging.info("Get Token SDI")
        token = self.GetToken()

        logging.info("Get Playlist URI")
        playlist_uri = self.GetPlaylist(token)
        

        self.start_time = time.time()
        try:
            while self.start_process:
                if playlist_uri is not None:
                    logging.info("Get Segment URI")
                    segments_uri = self.GetSegments(playlist_uri)

                    while segments_uri is None:
                        if self.segment_status == 403:
                            logging.info("Retry Get Token SDI")
                            token = self.GetToken()

                            logging.info("Retry Get Playlist URI")
                            playlist_uri = self.GetPlaylist(token)

                        logging.info("Retry Get Segment URI")
                        segments_uri = self.GetSegments(playlist_uri)
                        time.sleep(2)
                    
                    logging.info("Download segment")
                    self.DownloadSegment(segments_uri)

                    if time.time() - self.start_time > self.mp4_duration:
                        now_filename = F"INEWSSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
                        self.video_prosessor.ConcatTS(
                            filename=now_filename,
                            mode="w",
                        )

                        self.start_time = time.time()

                        logging.info("Cleanup TS")
                        self.video_prosessor.CleanUPTSFolder()

                    time.sleep(self.delay_duration)
                else:
                    logging.info("Retry Get Playlist URI")
                    playlist_uri = self.GetPlaylist(token)
                    time.sleep(2)
        except KeyboardInterrupt:
            self.start_process = False
            logging.info("Stop Engine")

            self.video_prosessor.CleanUPTSFolder()
            logging.info("Cleanup TS")
            return None

if __name__ == "__main__":
    url = "https://tv.inews.id/live"
    inews = INews(environment="dev", url=url, upload_location="storage/inews")
    inews.StartEngine()   