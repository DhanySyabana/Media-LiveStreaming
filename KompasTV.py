import subprocess
import os
import signal
import logging
import time
import datetime

from libs.Loggers1 import Loggers
from settings.Config import Config
from libs.ErrorHandler import get_error_message, get_exception_message
from libs.PusherNotification import trigger_error_notification
from libs.Countdown import countdown_sleep

class KompasTv:

    def __init__(
            self,
            environment: str,
            url: str = None,
            upload_location: str = None,
            duration: str = None
        ) -> None:
        self.environment = environment
        self.url: str = url
        self.start_process: bool = True
        self.upload_location: str = upload_location
        self.segment_duration = duration

        self.video_prosessor = None  # Jika ada VideoProsessor untuk KompasTv
        Loggers()
        self.countdown_counter = 0
        self.max_countdown_before_notif = 3
        super().__init__()

    def _handle_error_with_notification(self, error_message: str, send_immediate: bool = True) -> None:

        if send_immediate and self.countdown_counter == 0:
            trigger_error_notification(channel_name='KompasTv', log_text=error_message)
        
        countdown_sleep(300)
        
        self.countdown_counter += 1
        
        if self.countdown_counter > 0 and self.countdown_counter % self.max_countdown_before_notif == 0:
            trigger_error_notification(channel_name='KompasTv', log_text=error_message)
            logging.warning(f"Notification sent after countdown cycle {self.countdown_counter} ({self.countdown_counter * 5} minutes total)")
        else:
            remaining_cycles = self.max_countdown_before_notif - (self.countdown_counter % self.max_countdown_before_notif)
            logging.warning(f"Countdown cycle {self.countdown_counter}, next notification in {remaining_cycles} more cycles ({remaining_cycles * 5} minutes)")

    def ensure_directory_exists(self, output_dir):
        os.makedirs(output_dir, exist_ok=True)

    def build_ffmpeg_command(self, stream_url, output_dir, segment_duration):
        return [
            "ffmpeg",
            "-y",
            "-i", stream_url,
            "-c", "copy",
            "-f", "segment",
            "-segment_time", segment_duration,
            "-reset_timestamps", "1",
            "-strftime", "1",
            os.path.join(output_dir, "KOMPASSTREAMING_%m-%d-%H-%M-%S.mp4")  # UBAH NAMA FILE DISINI
        ]

    def kill_process(self, process):
        """Hentikan proses dengan aman"""
        if process and process.poll() is None:  
            logging.info("Terminating FFmpeg process...")
            process.terminate()
            time.sleep(2) 
            if process.poll() is None:
                logging.warning("Process still running, force killing...")
                process.kill()

    def StartEngine(self) -> None:
        logging.info("Start Engine")

        if not self.url:
            logging.error("URL is empty", extra={"log_text": "URL is empty", "detail": "Missing channel URL"})
            return None

        if not self.upload_location:
            logging.error("upload_location is empty", extra={"log_text": "upload_location is empty", "detail": "Missing upload location"})
            return None

        self.ensure_directory_exists(self.upload_location)

        process = None 
        try:
            while self.start_process:
                
                cmd = self.build_ffmpeg_command(self.url, self.upload_location, self.segment_duration)
                logging.info("Starting FFmpeg recording...")

                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True
                )

                low_speed_count = 0  
                url_error_count = 0 

                while True:
                    output = process.stderr.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        logging.info(output.strip())

                        # Deteksi URL Error
                        if "Failed to resolve hostname" in output or "Error opening input" in output:
                            url_error_count += 1
                            logging.error(f"URL error detected {url_error_count} times.")

                            if url_error_count >= 3:
                                logging.error("Stream URL is down. Stopping FFmpeg and retrying...")
                                self._handle_error_with_notification("Stream URL is down", send_immediate=True)
                                self.kill_process(process)
                                break
                        else:
                            url_error_count = 0  #

                        # Deteksi speed rendah
                        if "speed=" in output:
                            try:
                                speed_str = output.split("speed=")[-1].strip().split("x")[0]
                                speed_value = float(speed_str)

                                if speed_value < 0.5:
                                    low_speed_count += 1
                                    logging.warning(f"Low speed detected {low_speed_count} times: {speed_value}x")

                                    if low_speed_count >= 5:
                                        logging.error("Speed too low for too long, stopping FFmpeg...")
                                        self._handle_error_with_notification("Speed too low for too long", send_immediate=True)
                                        self.kill_process(process)
                                        break
                                else:
                                    low_speed_count = 0  

                            except ValueError:
                                logging.warning("Failed to parse speed value from FFmpeg output.")

                self.kill_process(process) 
                logging.info("Stream unavailable. Retrying in 10 seconds...")
                time.sleep(10) 

        except Exception as e:
            error_message = get_exception_message(e)
            logging.error(f"ERROR in recording: {e}", extra={"log_text": error_message, "detail": str(e)}, exc_info=True)
            self._handle_error_with_notification(error_message, send_immediate=True)
            logging.info("Retry in 3 seconds...")
            time.sleep(3)

        except KeyboardInterrupt:
            self.start_process = False
            logging.info("Stop Engine")
            return None

if __name__ == "__main__":
    ENGINE_NAME = "KOMPASSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]

    kompastv = KompasTv(
        environment=ENGINE["ENVIRONMENT"],
        url=ENGINE["URL"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        duration=ENGINE["DURATION"]
    )
    kompastv.StartEngine()