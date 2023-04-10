import m3u8
import time
import logging
import datetime
from libs.Loggers import Loggers
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessor import VideoProsessor

class CNNIndonesia:

    def __init__(
            self,
            environment:str,
            host_directory:str = "https://live.cnnindonesia.com/livecnn/smil:cnntv.smil",
            url_segment:str = "chunklist_w1002049210_b192000_sleng.m3u8",
            upload_location:str = None,
            headers: dict = {
                'referer': 'https://www.cnnindonesia.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            },
            delay_duration:int = 4,
            mp4_duration:int = 660,
        ) -> None:
        self.environment = environment
        self.host_directory = host_directory
        self.url_segment = F"{host_directory}/{url_segment}"
        self.upload_location = upload_location
        self.custom_headers = headers
        self.start_process = True
        self.start_time = time.time()
        self.delay_duration = delay_duration
        self.mp4_duration = mp4_duration
        self.media_sequence = None
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
            segment_uri = segments[0]["uri"]

            if self.media_sequence is None:
                self.media_sequence = int(segment_uri.split("_")[4].split(".")[0])
            else:
                self.media_sequence = self.media_sequence + 1
            
            url_segment = F"{self.host_directory}/{segments[0]['uri']}"
        else:
            logging.error(F"Error Get Segments: {response.status_code}")
            
        return url_segment

    def DownloadSegment(self, segment_uri: str) -> None:
        response = HTTPRequest("get", segment_uri, self.custom_headers).Hit()
        if response.status_code == 200:
            file_name = F"{self.media_sequence}.ts"

            self.video_prosessor.WriteFile(
                file_name=file_name,
                content=response.content,
                mode="wb",
                folder="ts"
            )
        else:
            logging.error(F"Error Download Segment: {response.status_code}")
        logging.info(F"Succes Download Segment")
        return None

    def StartEngine(self) -> None:
        logging.info("Start Engine")

        logging.info("Cleanup TS")
        self.video_prosessor.CleanUPTSFolder()

        self.start_time = time.time()
        try:
            while self.start_process:
                logging.info("Get Segment URI")
                segment_uri = self.GetSegment()

                while segment_uri is None:
                    logging.info("Retry Get Segment URI")
                    segment_uri = self.GetSegment()
                    time.sleep(2)

                logging.info("Download segment")
                self.DownloadSegment(segment_uri)
                
                if time.time() - self.start_time > self.mp4_duration:
                    now_filename = F"CNNSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
                    self.video_prosessor.ConcatTS(
                        filename=now_filename,
                        mode="w",
                    )
                    self.start_time = time.time()

                    logging.info("Cleanup TS")
                    self.video_prosessor.CleanUPTSFolder()

                time.sleep(self.delay_duration)

        except KeyboardInterrupt:
            self.start_process = False
            logging.info("Stop Engine")

            self.video_prosessor.CleanUPTSFolder()
            logging.info("Cleanup TS")
            return None


if __name__ == "__main__":
    cnnindonesia = CNNIndonesia(environment="dev", upload_location="storage/cnnindonesia")
    cnnindonesia.StartEngine()