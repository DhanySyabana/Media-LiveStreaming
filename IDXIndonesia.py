import time
import logging
import datetime
import os
import subprocess
import shutil
import sys

from libs.Loggers import Loggers
from settings.Config import Config
from libs.VideoProsessorIDX import VideoProsessor
from libs.ErrorHandler import get_error_message, get_exception_message
from libs.PusherNotification import trigger_error_notification
from libs.Countdown import countdown_sleep
from settings.Connector import get_channel_data

class IdxIndonesia:

    def __init__(
            self,
            environment: str,
            url: str = None,
            resolution: str = None,
            upload_location: str = None,
            headers: dict = None,
            cookies: str = None
        ) -> None:
        self.environment = environment
        self.url: str = url
        self.resolution: str = resolution
        self.start_process: bool = True
        self.upload_location: str = upload_location
        self.custom_headers: dict = headers

        # mau 20 detik
        self.video_duration = 601
        self.cookies_max_age_second = 3600 * 6  # 6 jam  
        self.last_sequence = None
        self.cookies = cookies  # ini path cookies file (cookies.txt)
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        Loggers()
        self.countdown_counter = 0
        self.max_countdown_before_notif = 3
        super().__init__()

    def _is_cookie_stale(self) -> bool:
        if not os.path.exists(self.cookies):
            return True
        age = time.time() - os.path.getmtime(self.cookies)
        return age > self.cookies_max_age_second
    
    def _refresh_cookies_from_browser(self) -> bool:
        """Export ulang cookie dari browser lokal."""
        try:
            yt_binary = shutil.which("yt-dlp") or sys.executable
            cmd = [
                yt_binary,
                "--cookies-from-browser", "chrome",
                "--cookies", self.cookies,
                "--skip-download",
                self.url
            ]
            subprocess.run(cmd, check=True, timeout=30)
            logging.info("Cookie berhasil di-refresh dari browser")
            return True
        except Exception as e:
            logging.error(f"Gagal refresh cookie: {e}")
            return False
        
    def _handle_error_with_notification(self, error_message: str, send_immediate: bool = True) -> None:

        if send_immediate and self.countdown_counter == 0:
            trigger_error_notification(channel_name='IDX Channel', log_text=error_message)
        
        countdown_sleep(300)
        
        self.countdown_counter += 1
        
        if self.countdown_counter > 0 and self.countdown_counter % self.max_countdown_before_notif == 0:
            trigger_error_notification(channel_name='IDX Channel', log_text=error_message)
            logging.warning(f"Notification sent after countdown cycle {self.countdown_counter} ({self.countdown_counter * 5} minutes total)")
        else:
            remaining_cycles = self.max_countdown_before_notif - (self.countdown_counter % self.max_countdown_before_notif)
            logging.warning(f"Countdown cycle {self.countdown_counter}, next notification in {remaining_cycles} more cycles ({remaining_cycles * 5} minutes)")

    def _get_yt_stream_url(self) -> str:
        """
        Ambil URL stream (m3u8) dari YouTube pakai yt-dlp.
        360p = format id 93
        """
        # Prefer an installed yt-dlp binary; fall back to `python -m yt_dlp` if not available
        yt_binary = shutil.which("yt-dlp")
        if yt_binary:
            cmd = [
                yt_binary,
                "--cookies", self.cookies,
                "--js-runtimes", "node",
                "-g",
                "-f", "93",  # 360p
                self.url
            ]
        else:
            cmd = [
                sys.executable,
                "-m",
                "yt_dlp",
                "--cookies", self.cookies,
                "--js-runtimes", "node",
                "-g",
                "-f", "93",
                self.url
            ]

        try:
            out = subprocess.check_output(cmd, text=True).strip()
        except FileNotFoundError as e:
            logging.error(
                "yt-dlp not found. Install yt-dlp or ensure it's in PATH.",
                extra={"log_text": "yt-dlp not found", "detail": str(e)}
            )
            self._handle_error_with_notification("yt-dlp not found; install in PATH or add to venv", send_immediate=True)
            return None

        lines = out.splitlines()
        return lines[0] if lines else None

    def _record_chunk_ffmpeg(self, stream_url: str, out_path: str, seconds: int):
        """
        Rekam stream selama X detik jadi mp4.
        """
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel", "error",

            "-reconnect", "1",
            "-reconnect_streamed", "1",
            "-reconnect_delay_max", "5",

            "-i", stream_url,
            "-t", str(seconds),
            "-c", "copy",
            "-movflags", "+faststart",
            out_path
        ]
        subprocess.run(cmd, check=True)

    def StartEngine(self) -> None:
        logging.info("Start Engine")
        if self._is_cookie_stale():
            logging.warning("Cookie stale, refreshing...")
            self._refresh_cookies_from_browser()
        if not self.url:
            logging.error("URL is empty", extra={"log_text": "URL is empty", "detail": "Missing channel URL"})
            return None

        if not self.upload_location:
            logging.error("upload_location is empty", extra={"log_text": "upload_location is empty", "detail": "Missing upload location"})
            return None

        if not self.cookies or not os.path.exists(self.cookies):
            logging.error(f"Cookies file not found: {self.cookies}", extra={"log_text": "Cookies file not found", "detail": str(self.cookies)})
            return None

        os.makedirs(self.upload_location, exist_ok=True)

        idx = 1

        try:
            while self.start_process:
                now_filename = f"IDXSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
                out_path = os.path.join(self.upload_location, f"{now_filename}.mp4")
                logging.info(f"Save File : {out_path}")

                try:
                    logging.info(f"[{idx}] Fetching stream URL...")
                    stream_url = self._get_yt_stream_url()

                    if not stream_url:
                        logging.error(f"[{idx}] Failed to obtain stream URL; skipping iteration", extra={"log_text": "Failed to obtain stream URL"})
                        time.sleep(3)
                        continue

                    logging.info(f"[{idx}] Recording {self.video_duration}s -> {out_path}")
                    self._record_chunk_ffmpeg(stream_url, out_path, self.video_duration)

                    # kalau mau langsung diproses (convert/upload) setelah file jadi:
                    # self.video_prosessor.ProcessVideo(out_path)

                    idx += 1

                except subprocess.CalledProcessError as e:
                    error_message = get_exception_message(e)
                    logging.error(f"[{idx}] ERROR record: {e}", extra={"log_text": error_message, "detail": str(e)}, exc_info=True)
                    self._handle_error_with_notification(error_message, send_immediate=True)
                    logging.info("Retry in 3 seconds...")
                    time.sleep(3)

        except KeyboardInterrupt:
            self.start_process = False
            logging.info("Stop Engine")
            return None


if __name__ == "__main__":
    ENGINE_NAME = "IDXSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]

    idx = IdxIndonesia(
        environment=ENGINE["ENVIRONMENT"],
        url=ENGINE['URL'],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        cookies="cookies.txt"
    )
    idx.StartEngine()
