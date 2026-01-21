import time
import logging
import datetime
import os
import subprocess

from libs.Loggers import Loggers
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessorKompas import VideoProsessor

from settings.Connector import get_channel_data


class MetroTV:

    def __init__(
            self,
            environment: str,
            url: str = None,
            quality: str = None,
            upload_location: str = None,
            headers: dict = None,
            converter_host: str = None,
            converter_port: int = None,
            buffer_size: int = None,
            cookies: str = None
        ) -> None:
        self.environment = environment
        self.url: str = url
        self.quality: str = quality
        self.start_process: bool = True
        self.upload_location: str = upload_location
        self.custom_headers: dict = headers

        # mau 20 detik
        self.video_duration = 600

        self.last_sequence = None
        self.cookies = cookies  # ini path cookies file (cookies.txt)
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        self.converter_host = converter_host
        self.converter_port = converter_port
        self.buffer_size = buffer_size
        Loggers()
        super().__init__()

    def _get_yt_stream_url(self) -> str:
        """
        Ambil URL stream (m3u8) dari YouTube pakai yt-dlp.
        360p = format id 93
        """
        cmd = [
            "yt-dlp",
            "--cookies", self.cookies,
            "--js-runtimes", "node",
            "-g",
            "-f", "93",  # 360p
            self.url
        ]
        out = subprocess.check_output(cmd, text=True).strip()
        return out.splitlines()[0]

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

        if not self.url:
            logging.error("URL is empty")
            return None

        if not self.upload_location:
            logging.error("upload_location is empty")
            return None

        if not self.cookies or not os.path.exists(self.cookies):
            logging.error(f"Cookies file not found: {self.cookies}")
            return None

        os.makedirs(self.upload_location, exist_ok=True)

        idx = 1

        try:
            while self.start_process:
                now_filename = f"METROTVSTREAMING_{datetime.datetime.now().strftime('%m-%d-%H-%M-%S')}"
                out_path = os.path.join(self.upload_location, f"{now_filename}.mp4")
                logging.info(f"Save File : {out_path}")

                try:
                    logging.info(f"[{idx}] Fetching stream URL...")
                    stream_url = self._get_yt_stream_url()

                    logging.info(f"[{idx}] Recording {self.video_duration}s -> {out_path}")
                    self._record_chunk_ffmpeg(stream_url, out_path, self.video_duration)

                    # kalau mau langsung diproses (convert/upload) setelah file jadi:
                    # self.video_prosessor.ProcessVideo(out_path)

                    idx += 1

                except subprocess.CalledProcessError as e:
                    logging.error(f"[{idx}] ERROR record: {e}")
                    logging.info("Retry in 3 seconds...")
                    time.sleep(3)

        except KeyboardInterrupt:
            self.start_process = False
            logging.info("Stop Engine")
            return None


if __name__ == "__main__":
    ENGINE_NAME = "METROTVSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]

    metro_tv = MetroTV(
        environment=ENGINE["ENVIRONMENT"],
        url=get_channel_data(ENGINE_NAME)[0]['url'],
        quality=get_channel_data(ENGINE_NAME)[0]['resolusi'],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        headers=ENGINE["HEADERS"],
        cookies="cookies.txt",  # path ke cookies.txt
        converter_host=CONFIG.SOCKET_SERVER_KOMPAS["HOST"],
        converter_port=CONFIG.SOCKET_SERVER_KOMPAS["PORT"],
        buffer_size=CONFIG.SOCKET_SERVER_KOMPAS["BUFFER_SIZE"]
    )
    metro_tv.StartEngine()
