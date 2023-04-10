import time
import m3u8
import logging
import datetime
import streamlink
from libs.Loggers import Loggers
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessor import VideoProsessor

class KompasTV:

    def __init__(
            self,
            environment:str,
            url:str = "https://www.youtube.com/watch?v=4rmf-lk3ito",
            quality:str = "360p",
            upload_location:str = None,
            headers: dict = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            },
        ) -> None:
        self.environment = environment
        self.url:str = url
        self.quality:str = quality
        self.start_process:bool = True
        self.start_time = time.time(),
        self.upload_location:str = upload_location
        self.custom_headers:dict = headers
        self.filename = None
        self.mp4_duration:int = 660
        self.delay_duration:int = 5
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        Loggers()
        super().__init__()

    def GetStreamSegment(self) -> m3u8.model.Segment:
        stream_segment = None

        try:
            streams = streamlink.streams(self.url)
            stream_url = streams[self.quality]

            m3u8_obj = m3u8.load(stream_url.args['url'])
            stream_segment = m3u8_obj.segments[0]
        except streamlink.exceptions.PluginError as e:
            stream_segment = None
            logging.error(F"Error Get Stream Segment: {e}")

        return stream_segment
    
    def RecordStream(self, stream_segment):
        self.filename = F"{stream_segment.program_date_time.astimezone().strftime('%Y%m%d%H%M%S')}.ts"
        response = HTTPRequest("get", stream_segment.uri, self.custom_headers).Hit()
        if response.status_code == 200:
            self.video_prosessor.WriteFile(
                file_name=self.filename,
                content=response.content,
                mode="wb",
                folder="ts"
            )
        else:
            logging.error(F"Error Download Segment: {response.status_code}")
        logging.info(F"Succes Download Segment")
        return None

    def StartEngine(self):
        logging.info("Start Engine")

        logging.info("Cleanup TS")
        self.video_prosessor.CleanUPTSFolder()

        self.start_time = time.time()
        try: 
            while self.start_process:

                logging.info("Get Stream Segment")
                stream_segment = self.GetStreamSegment()

                while stream_segment is None:
                    logging.info("Retrying Stream Segment")
                    stream_segment = self.GetStreamSegment()
                    time.sleep(self.delay_duration - 2)

                logging.info("Record Stream")
                self.RecordStream(stream_segment)

                if time.time() - self.start_time > self.mp4_duration:
                    now_filename = F"KOMPASSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
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
    kompas_tv = KompasTV(environment="prod", upload_location="/home/kabayangroup/www/produksi-tv/public/video_list/KOMPASSTREAMING")
    kompas_tv.StartEngine()
    