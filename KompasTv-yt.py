import subprocess
import datetime
import os
import logging
import time


class YTRecorder:

    def __init__(self, url, cookies, output_dir, duration=600):
        self.url = url
        self.cookies = cookies
        self.output_dir = output_dir
        self.duration = duration
        os.makedirs(self.output_dir, exist_ok=True)

    def record(self):
        now_filename = f"STREAM_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp4"
        out_path = os.path.join(self.output_dir, now_filename)

        logging.info(f"Recording -> {out_path}")

        # yt-dlp command
        ytdlp_cmd = [
            "yt-dlp",
            "--cookies", self.cookies,
            "-f", "93",
            "-o", "-"
        ]

        # ffmpeg command
        ffmpeg_cmd = [
            "ffmpeg",
            "-y",
            "-i", "pipe:0",

            "-fflags", "+genpts",
            "-r", "25",
            "-vsync", "1",

            "-c:v", "libx264",
            "-preset", "veryfast",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",

            "-t", str(self.duration),
            out_path
        ]

        # piping process
        ytdlp = subprocess.Popen(
            ytdlp_cmd + [self.url],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        )

        ffmpeg = subprocess.Popen(
            ffmpeg_cmd,
            stdin=ytdlp.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        ytdlp.stdout.close()
        out, err = ffmpeg.communicate()

        if ffmpeg.returncode == 0:
            logging.info("Recording finished successfully")
        else:
            logging.error("Recording failed")
            logging.error(err.decode(errors="ignore"))


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    recorder = YTRecorder(
        url="https://www.youtube.com/watch?v=DOOrIxw5xOw",
        cookies="cookies.txt",
        output_dir="storage/kompas",
        duration=600   # 10 menit
    )

    while True:
        try:
            recorder.record()
            time.sleep(1)
        except KeyboardInterrupt:
            print("Stop.")
            break
