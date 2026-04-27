import time
import m3u8
import logging
import datetime
import requests
import json

from libs.Loggers import Loggers
from libs.Selenium import Selenium
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessorINews import VideoProsessor
from libs.ErrorHandler import get_error_message, get_exception_message
from libs.PusherNotification import trigger_error_notification
from libs.Countdown import countdown_sleep


class INews:

    def __init__(
        self,
        environment: str,
        url: str,
        host_directory: str = None,
        search_ext: str = ".m3u8",
        resolution: str = None,
        upload_location=None,
        custom_headers: dict = None,
    ) -> None:

        self.environment = environment
        self.url = url
        self.host_directory = host_directory
        self.query = None
        self.search_ext = search_ext
        self.resolution = resolution
        self.upload_location = upload_location
        self.video_duration = 2
        self.custom_headers = custom_headers

        self.last_sequence = None
        self.start_process = True
        self.segment_status = None

        self.video_prosessor = VideoProsessor(
            environment=self.environment,
            storage_path=self.upload_location
        )

        self.max_attempts = 3
        self.countdown_counter = 0
        self.max_countdown_before_notif = 3

        self.has_download_error = False
        self.consecutive_errors = 0
        self.max_consecutive_errors = 3

        Loggers()

        super().__init__()

    def _handle_error_with_notification(self, error_message: str, send_immediate: bool = True) -> None:

        if send_immediate and self.countdown_counter == 0:
            trigger_error_notification(
                channel_name='INewsV1',
                log_text=error_message
            )
        countdown_sleep(300)
        self.countdown_counter += 1
        if self.countdown_counter % self.max_countdown_before_notif == 0:
            trigger_error_notification(
                channel_name='INewsV1',
                log_text=error_message
            )
            logging.warning(
                f"Notification sent after countdown cycle {self.countdown_counter}"
            )

    def GetPathSDI(self, selenium=None) -> str:
        path_uri = None
        token = requests.get('https://api.rctiplus.com/api/v1/live-event/4/url?appierid=undefined', headers={'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2aWQiOjAsInRva2VuIjoiYTQ3MDA0ZTk2ODRkNDBkOSIsInBsIjoid2ViIiwiZGV2aWNlX2lkIjoiMTYwZWZiYmMtMDQ0My0xMWVlLTk0YmUtMDAxNjNlMDM4OGRiIn0.f1zienRzzc0rKo1Mt_BxSqTAaAGxF0Dzmhnx7oJOcbg'})
        page = json.loads(token.text)
        path_uri = page['data']['url']
        auth = path_uri.partition('?auth_key=')[2]
        headers={
            'accept': 'application/json',
            'Authorization':'Bearer '+auth,
            'origin': 'https://www.rctiplus.com',
            'referer': 'https://www.rctiplus.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9'
            }
        self.custom_headers = headers
        logging.info(F"Path SDI: {path_uri}")
        return path_uri

    def GetPlaylist(self, query_sdi: str) -> str:
        playlist_uri = None
        url = f"{query_sdi}"
        logging.info(f"URL: {url}")
        for attempt in range(1, self.max_attempts + 1):
            try:
                response = HTTPRequest(
                    "get",
                    url,
                    self.custom_headers
                ).Hit()
                if response.status_code != 200:
                    raise Exception(response.status_code)
                m3u8_master = m3u8.loads(response.text)
                playlists = m3u8_master.data.get("playlists", [])
                for playlist in playlists:
                    if playlist["stream_info"].get("resolution") == self.resolution:
                        playlist_uri = f"{self.host_directory}/{playlist['uri']}"
                        break
                if not playlist_uri and playlists:
                    playlist_uri = f"{self.host_directory}/{playlists[0]['uri']}"
                self.countdown_counter = 0
                return playlist_uri
            except Exception as e:
                logging.warning(f"Attempt {attempt} failed")
                if attempt == self.max_attempts:
                    error_message = get_exception_message(e)
                    logging.error(error_message)
                    self._handle_error_with_notification(error_message)
                time.sleep(10)
        return None

    def GetSegments(self, playlist_uri: str) -> list:
        file_segments = []
        try:
            response = HTTPRequest(
                "get",
                playlist_uri,
                self.custom_headers
            ).Hit()
            if response.status_code != 200:
                return []
            m3u8_master = m3u8.loads(response.text)
            segments = m3u8_master.data.get("segments", [])
            for segment in segments:
                file_segments.append({
                    "url": f"{self.host_directory}/{segment['uri']}",
                    "sequence": int(
                        segment["uri"].split("seq=")[1].split(".ts")[0]
                    )
                })
        except Exception as e:
            logging.error(get_exception_message(e))
        return file_segments[-5:]

    def DownloadSegment(self, segments: list) -> None:
        logging.info("Download Segment")
        for segment in segments:
            try:
                response = HTTPRequest(
                    "get",
                    segment["url"],
                    self.custom_headers
                ).Hit()
                if response.status_code == 200:
                    file_name = f"{segment['sequence']}.ts"
                    write_file = self.video_prosessor.WriteFile(
                        file_name=file_name,
                        content=response.content,
                        mode="wb",
                        folder="ts"
                    )
                    if write_file:
                        self.last_sequence = segment["sequence"]
                        logging.info(f"Downloaded {file_name}")
                else:
                    logging.error(f"Download error {response.status_code}")
            except Exception as e:
                logging.error(get_exception_message(e))

    def GetToken(self) -> str:
        selenium = Selenium(self.url, {"headless": True})
        selenium.SeleniumCapabilities()
        selenium.SeleniumOptions()
        token = self.GetPathSDI(selenium)
        return token

    def CheckTSFiles(self) -> dict:
        if self.last_sequence is None:
            return {"status": False, "data_ts": []}

        last_ts = f"{self.last_sequence}.ts"
        total = self.video_prosessor.GetTotalFiles(
            folder="ts",
            last_ts=last_ts
        )
        if total >= 3:
            list_files = self.video_prosessor.ListFiles(
                folder="ts",
                last_ts=last_ts
            )
            return {
                "status": True,
                "data_ts": list_files
            }
        return {
            "status": False,
            "data_ts": []
        }

    def HandleSegments(self, playlist_uri: str, token: str):
        segments = self.GetSegments(playlist_uri)
        if not segments:
            time.sleep(self.video_duration)
            return playlist_uri, token
        self.DownloadSegment(segments)
        check_ts = self.CheckTSFiles()
        if check_ts["status"]:
            now_filename = f"INEWSSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
            response = self.video_prosessor.ConcatTS(
                filename=now_filename,
                mode="w",
                optimize_video=False
            )
            logging.info(response)
            self.video_prosessor.CleanUPTSFolder(
                list_ts=check_ts["data_ts"],
                metadata=now_filename
            )
        return playlist_uri, token

    def StartEngine(self):
        logging.info("Start Engine")
        self.video_prosessor.CleanUPTSFolder()
        token = self.GetToken()
        playlist_uri = self.GetPlaylist(token)
        try:
            while self.start_process:
                if not playlist_uri:
                    token = self.GetToken()
                    playlist_uri = self.GetPlaylist(token)
                    time.sleep(self.video_duration)
                    continue
                playlist_uri, token = self.HandleSegments(
                    playlist_uri,
                    token
                )
                time.sleep(self.video_duration)

        except KeyboardInterrupt:
            logging.info("Stop Engine")
            self.start_process = False
            self.video_prosessor.CleanUPTSFolder()
            return None

if __name__ == "__main__":
    ENGINE_NAME = "INEWSSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]

    inews = INews(
        environment=ENGINE["ENVIRONMENT"],
        url=ENGINE["URLV1"],
        host_directory=ENGINE["HOST_DIRECTORYV1"],
        resolution=ENGINE["RESOLUTIONV1"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        custom_headers=ENGINE["HEADERS"]
    )
    inews.StartEngine()