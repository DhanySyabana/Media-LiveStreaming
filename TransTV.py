import m3u8
import time
import logging
import datetime
import cloudscraper
from libs.Loggers1 import Loggers
from settings.Config import Config
from libs.VideoProsessorTransTV import VideoProsessor
from libs.ErrorHandler import get_error_message, get_exception_message
from libs.PusherNotification import trigger_error_notification
from libs.Countdown import countdown_sleep

class TransTV:

    def __init__(
        self,
        environment: str,
        host_directory: str = None,
        upload_location: str = None,
        headers: dict = None,
        playlist: str = None,
        resolution: str = None
    ) -> None:
        self.environment = environment
        self.host_directory = host_directory
        self.upload_location = upload_location
        self.custom_headers = headers
        self.playlist = playlist
        self.resolution = resolution

        self.scraper = cloudscraper.create_scraper(delay=10, browser='chrome')

        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)

        self.start_process = True
        self.sleep_duration = 10
        self.last_sequence = None
        self.segment_status = None
        self.max_retry = 5
        self.retry_count = 0
        self.max_attempts = 3
        self.countdown_counter = 0
        self.max_countdown_before_notif = 3 
        self.count_file_ts = 200
        self.has_download_error = False
        self.consecutive_errors = 0
        self.max_consecutive_errors = 3

        Loggers()
        super().__init__()

    def _handle_error_with_notification(self, error_message: str, send_immediate: bool = True) -> None:

        if send_immediate and self.countdown_counter == 0:
            trigger_error_notification(channel_name='TransTV', log_text=error_message)
        
        countdown_sleep(300)
        
        self.countdown_counter += 1
        
        if self.countdown_counter > 0 and self.countdown_counter % self.max_countdown_before_notif == 0:
            trigger_error_notification(channel_name='TransTV', log_text=error_message)
            logging.warning(f"Notification sent after countdown cycle {self.countdown_counter} ({self.countdown_counter * 5} minutes total)")
        else:
            remaining_cycles = self.max_countdown_before_notif - (self.countdown_counter % self.max_countdown_before_notif)
            logging.warning(f"Countdown cycle {self.countdown_counter}, next notification in {remaining_cycles} more cycles ({remaining_cycles * 5} minutes)")

    def GetPlaylist(self) -> str:
        
        url = f"{self.host_directory}/{self.playlist}"
        logging.info(f"URL: {url}")
        
        last_error = None
        last_error_detail = None
        last_exc = False

        for attempt in range(1, self.max_attempts + 1):
            try:
                response = self.scraper.get(url, headers=self.custom_headers, timeout=10)
            except Exception as e:
                last_error = get_exception_message(e)
                last_error_detail = str(e)
                last_exc = True
                self.segment_status = None
                if attempt < self.max_attempts:
                    logging.warning(f"Attempt {attempt}/{self.max_attempts} failed (Exception), retrying in 10 seconds...")
                    time.sleep(10)
                    continue
 
                logging.error(
                    f"Exception Get Playlist after {self.max_attempts} attempts: {type(e).__name__}",
                    extra={
                        'log_text': last_error,
                        'detail': last_error_detail
                    },
                    exc_info=True
                )
                self._handle_error_with_notification(last_error, send_immediate=True)
                return None

            if response.status_code != 200:
                self.segment_status = response.status_code
                last_error = get_error_message(response.status_code)
                last_error_detail = response.reason
                if attempt < self.max_attempts:
                    logging.warning(f"Attempt {attempt}/{self.max_attempts} failed (Status {response.status_code}), retrying in 10 seconds...")
                    time.sleep(10)
                    continue
                logging.error(
                    f"Error Get Playlist after {self.max_attempts} attempts: {response.status_code}",
                    extra={
                        'log_text': last_error,
                        'detail': last_error_detail
                    }
                )
                self._handle_error_with_notification(last_error, send_immediate=True)
                return None

            try:
                m3u8_master = m3u8.loads(response.text)
            except Exception as e:
                last_error = get_exception_message(e)
                last_error_detail = str(e)
                last_exc = True
                if attempt < self.max_attempts:
                    logging.warning(f"Attempt {attempt}/{self.max_attempts} failed (Parse error), retrying in 10 seconds...")
                    time.sleep(10)
                    continue
                logging.error(f"Failed to parse playlist m3u8 after {self.max_attempts} attempts: {last_error}", exc_info=True)
                self._handle_error_with_notification(last_error, send_immediate=True)
                return None

            playlists = m3u8_master.data.get("playlists", [])
            if not playlists:
                last_error = "No playlists found in master playlist"
                last_error_detail = "master playlist contains no variant playlists"
                if attempt < self.max_attempts:
                    logging.warning(f"Attempt {attempt}/{self.max_attempts} failed (No playlists), retrying in 10 seconds...")
                    time.sleep(10)
                    continue
                logging.error(f"No playlists after {self.max_attempts} attempts; {last_error}")
                self._handle_error_with_notification(last_error, send_immediate=True)
                return None

            playlist_uri = None
            if hasattr(self, 'resolution') and self.resolution:
                for playlist in playlists:
                    stream_info = playlist.get("stream_info", {})
                    if stream_info.get("resolution") == self.resolution:
                        playlist_uri = f"{self.host_directory}/{playlist['uri']}"
                        logging.info(f"Playlist obtained for resolution {self.resolution}")
                        break

                if not playlist_uri:
                    logging.warning(f"Playlist not found for resolution {self.resolution}, using first available")

            if not playlist_uri:
                playlist_uri = f"{self.host_directory}/{playlists[0]['uri']}"
                logging.info("Get Playlist Success")

            self.countdown_counter = 0
            return playlist_uri

    def GetSegment(self, playlist_uri: str) -> list:
        file_segments = []
        try:
            response = self.scraper.get(playlist_uri, headers=self.custom_headers, timeout=10)
        except Exception as e:
            error_message = get_exception_message(e)
            logging.error(
                f"Exception Get Segments: {type(e).__name__}",
                extra={
                    'log_text': error_message,
                    'detail': str(e)
                }
            )
            self._handle_error_with_notification(error_message, send_immediate=True)
            self.segment_status = None
            return []

        if response.status_code != 200:
            self.segment_status = response.status_code
            error_message = get_error_message(response.status_code)
            logging.error(
                f"Error Get Segments: {response.status_code}",
                extra={
                    'log_text': error_message,  
                    'detail': response.reason
                }
            )
            self._handle_error_with_notification(error_message, send_immediate=True)
            return []

        try:
            m3u8_master = m3u8.loads(response.text)
        except Exception as e:
            logging.error(f"Failed to parse segments m3u8: {e}", exc_info=True)
            return []

        segments = m3u8_master.data.get("segments", [])
        for segment in segments:
            file_segments.append({
                "url": f"{self.host_directory}/{segment['uri']}",
                "sequence": segment['uri'].replace('.ts', '')
            })

        return file_segments[-5:]

    def DownloadSegment(self, segments: list) -> None:
        logging.info("Download Segment")
        self.has_download_error = False
        for segment in segments:
            try:
                response = self.scraper.get(segment["url"], headers=self.custom_headers, timeout=10)
                if response.status_code == 200:
                    file_name = f"{segment['sequence']}.ts"
                    write_file = self.video_prosessor.WriteFile(
                        file_name=file_name,
                        content=response.content,
                        mode="wb",
                        folder="ts"
                    )
                    seq = None
                    try:
                        seq = write_file.get("sequence") if write_file else None
                    except Exception:
                        seq = None

                    if seq:
                        self.last_sequence = seq
                        logging.info(f"Success Download Segment: {file_name}")
                        self.consecutive_errors = 0
                    else:
                        logging.error(f"WriteFile did not return sequence for {file_name}: {write_file}")
                        self.has_download_error = True
                        self.consecutive_errors += 1
                else:
                    self.segment_status = response.status_code
                    error_message = get_error_message(response.status_code)
                    logging.error(
                        f"Error Download Segment: {response.status_code}",
                        extra={
                            'log_text': error_message,
                            'detail': response.reason
                        }
                    )
                    self._handle_error_with_notification(error_message, send_immediate=True)
                    self.has_download_error = True
                    self.consecutive_errors += 1

            except Exception as e:
                error_message = get_exception_message(e)
                logging.error(
                    f"Exception Downloading Segment: {type(e).__name__}",
                    extra={
                        'log_text': error_message,
                        'detail': str(e)
                    },
                    exc_info=True
                )
                self._handle_error_with_notification(error_message, send_immediate=True)
                self.has_download_error = True
                self.consecutive_errors += 1

    def CheckTSFiles(self) -> dict:
        if self.last_sequence is None:
            return {"status": False, "data_ts": []}

        last_ts = f"{self.last_sequence}.ts"
        get_total_files = self.video_prosessor.GetTotalFiles(folder="ts", last_ts=last_ts)

        if get_total_files >= self.count_file_ts:
            list_files = self.video_prosessor.ListFiles(folder="ts", last_ts=last_ts)
            return {"status": True, "data_ts": list_files}

        return {"status": False, "data_ts": []}

    def HandleSegments(self, playlist_uri: str) -> str:
        segments = self.GetSegment(playlist_uri)

        if not segments and self.segment_status in [403, 404, 410, 503]:
            logging.warning("Attempting to refresh playlist due to error")
            playlist_uri = self.GetPlaylist()

        if not segments:
            time.sleep(self.sleep_duration)
            return playlist_uri

        time.sleep(self.sleep_duration)
        self.DownloadSegment(segments)

        check_ts = self.CheckTSFiles()
        
        # Jika ada error download dan ada file TS, lakukan convert langsung
        if self.has_download_error and self.last_sequence is not None:
            # Check apakah ada file TS minimal
            ts_count = self.video_prosessor.GetTotalFiles(folder="ts", last_ts=f"{self.last_sequence}.ts")
            if ts_count > 0:
                logging.warning(f"Download error detected with {ts_count} TS files. Converting to MP4 immediately.")
                now_filename = f"TRANSTVSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
                response = self.video_prosessor.ConcatTS(
                    filename=now_filename,
                    mode="w",
                    optimize_video=False
                )
                logging.info(f"Concat result: {response.get('message')}")

                list_files = self.video_prosessor.ListFiles(folder="ts", last_ts=f"{self.last_sequence}.ts")
                self.video_prosessor.CleanUPTSFolder(
                    list_ts=list_files,
                    metadata=now_filename
                )
                self.has_download_error = False
        # Check normal condition (5 file atau lebih)
        elif check_ts["status"]:
            now_filename = f"TRANSTVSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
            response = self.video_prosessor.ConcatTS(
                filename=now_filename,
                mode="w",
                optimize_video=False
            )
            logging.info(f"Concat result: {response.get('message')}")

            self.video_prosessor.CleanUPTSFolder(
                list_ts=check_ts["data_ts"],
                metadata=now_filename
            )

        return playlist_uri

    def StartEngine(self) -> None:
        logging.info("Start Engine")
        self.video_prosessor.CleanUPTSFolder()
        playlist_uri = self.GetPlaylist()

        try:
            while self.start_process:
                try:
                    if not playlist_uri:
                        playlist_uri = self.GetPlaylist()
                        time.sleep(self.sleep_duration)
                        continue

                    playlist_uri = self.HandleSegments(playlist_uri)
                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    error_message = get_exception_message(e)
                    logging.error(f"Unhandled exception in engine loop: {e}", exc_info=True)
                    self._handle_error_with_notification(error_message, send_immediate=True)
                    time.sleep(self.sleep_duration)
                    continue
        except KeyboardInterrupt:
            self.start_process = False
            logging.info("Stop Engine")
            self.video_prosessor.CleanUPTSFolder()

if __name__ == "__main__":
    ENGINE_NAME = "TRANSTVSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    transtv = TransTV(
        environment=ENGINE["ENVIRONMENT"],
        host_directory=ENGINE["HOST_DIRECTORY"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        playlist=ENGINE["PLAYLIST"],
        resolution=ENGINE["RESOLUTION"]
    )
    transtv.StartEngine()