import os
import subprocess
import glob
import time
import tqdm
import math
import logging
import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime
from libs.Loggers import Loggers
from settings.Config import Config
from matplotlib.gridspec import GridSpec

class Ops:

    def __init__(self, TOKEN:str, CHAT_ID:str, delay_proses:int, storage_path_mp4:dict) -> None:
        self.TOKEN:str= TOKEN
        self.CHAT_ID:str = CHAT_ID
        self.start_time = 0
        self.start_proses = True
        self.delay_proses:int = delay_proses
        self.storage_path_mp4:dict = storage_path_mp4
        Loggers()
        super().__init__()
    
    def get_file_data(self) -> dict:
        data = {}
        for key, value in self.storage_path_mp4.items():
            total_video = len([name for name in os.listdir(value) if name.endswith(".mp4")])
            if math.isnan(total_video):
                total_video = 0
            else:
                total_video = int(total_video)

            # total video last 60 minutes
            total_video_last_hour = len([name for name in os.listdir(value) if name.endswith(".mp4") and (time.time() - os.path.getmtime(F"{value}/{name}")) < 3600])
            if math.isnan(total_video_last_hour):
                total_video_last_hour = 0
            else:
                total_video_last_hour = int(total_video_last_hour)

            total_size = sum(os.path.getsize(F"{value}/{name}") for name in os.listdir(value) if name.endswith(".mp4")) / 1024 / 1024
            if math.isnan(total_size):
                total_size = 0
            else:
                total_size = int(total_size)

            data[key] = {
                "total_video": total_video,
                "total_size": total_size,
                "total_video_last_hour": total_video_last_hour,
                "last_video_filename": "-",
            }

            if total_video_last_hour > 0:
                data[key]["last_video_filename"] = max(glob.iglob(F"{value}/*.mp4"), key=os.path.getctime).split("/")[-1]

        return data
    
    def generate_send_chart(self, data:dict) -> None:
        key_data = list(data.keys())
        no = 0
        for key, channel in enumerate(key_data):
            if data[key_data[key]]["total_video_last_hour"] < 1:
                if channel == "INEWSSTREAMING":
                    print("INEWSSTREAMING")
                elif channel == "CNNSTREAMING":
                    print("CNNSTREAMING")
                elif channel == "KOMPASSTREAMING":
                    print("KOMPASSTREAMING")
                elif channel == "METROTVSTREAMING":
                    print("METROTVSTREAMING")
                elif channel == "CNBCSTREAMING":
                    print("CNBCSTREAMING")
                elif channel == "IDXSTREAMING":
                    try:
                        # time.sleep(3)
                        # os.system(f"docker restart engine_server_converter_idx")
                        # time.sleep(3)
                        # os.system(f"docker restart engine_idx_v1")
                        # server_container_idx ="engine_server_converter_idx"
                        # container_idx ="engine_idx_v1"
                        # subprocess.run(["docker", "restart", server_container_idx])
                        # subprocess.run(["docker", "restart", container_idx])
                        logging.info(F"Success Restart : {str(channel)}")
                    except Exception as e:
                        print(str(e))
                        logging.error(F"Error : {str(e)}")
                    
                elif channel == "TVONESTREAMING":
                    logging.info(F"Start : {str(channel)}")
                    try:
                        completed_process = subprocess.run(
                            ["docker", "ps"],
                            check=True,  # Menganggap non-zero exit code sebagai error
                            stdout=subprocess.PIPE,  # Menangkap output
                            stderr=subprocess.PIPE,  # Menangkap error
                            text=True,  # Membaca output dan error sebagai teks
                        )

                        # Menampilkan output
                        print("Output:")
                        print(completed_process.stdout)

                    except subprocess.CalledProcessError as e:
                        print("Error:")
                        print(e.stderr)
                    # try:
                    #     # file_path ='/home/kabayangroup/restart/Tvone.sh'
                    #     # os.chdir("/home/kabayangroup/restart")
                    #     result =  subprocess.run("sh Tvone.sh", shell=True)
                    #     print("Exit code:", result)
                    # except subprocess.CalledProcessError as e:
                    #     print("Error:", e.returncode, e.stderr)
                    # except Exception as e:
                    #     print(str(e))
                    #     logging.error(F"Error : {str(e)}")
                    # logging.info(F"Success Restart : {str(channel)}")
                elif channel == "BERITASATUSTREAMING":
                    # try:
                    #     file_path ='/home/kabayangroup/restart/Beritasatu.sh'
                    #     subprocess.call(['bash', file_path])
                    # except Exception as e:
                    #     print(str(e))
                    #     logging.error(F"Error : {str(e)}")
                    logging.info(F"Success Restart : {str(channel)}")
                elif channel == "TVRISTREAMING":
                    try:
                        # time.sleep(3)
                        # os.system(f"docker restart engine_server_converter_v1")
                        # time.sleep(3)
                        # os.system(f"docker restart engine_tvri_v1")
                        # server_container_tvri ="engine_server_converter_v1"
                        # container_tvri ="engine_tvri_v1"
                        # subprocess.run(["docker", "restart", server_container_tvri])
                        # subprocess.run(["docker", "restart", container_tvri])
                        logging.info(F"Success Restart : {str(channel)}")
                    except Exception as e:
                        print(str(e))
                        logging.error(F"Error : {str(e)}")
                elif channel == "RCTISTREAMING":
                    print("RCTISTREAMING")


    def execute(self) -> None:
        try:
            self.start_time = time.time()
            data = self.get_file_data()
            self.generate_send_chart(data)
            logging.info("Success execute task")
        except Exception as e:
            logging.error(f"Error: {e}")
            self.start_proses = False
        return None


    def StartEngine(self):
        progress_bar = tqdm.tqdm(total=self.delay_proses, desc="Waiting for next task")
        while self.start_proses:
            try:

                if self.start_time == 0 or time.time() - self.start_time >= self.delay_proses:
                    self.execute()
                    progress_bar.reset()
                    os.system('cls' if os.name == 'nt' else 'clear')
                progress_bar.update(1)
                time.sleep(1)       
            except Exception as e:
                logging.error(f"Error: {e}")
                progress_bar.reset()
                self.start_proses = False
                break
            except KeyboardInterrupt:
                progress_bar.reset()
                logging.info("Close Ops")
                self.start_proses = False
                break
        progress_bar.close()


if __name__ == "__main__":
    CONFIG = Config().OPSV3
    ops = Ops(
        TOKEN=CONFIG["TELE_TOKEN"],
        CHAT_ID=CONFIG["TELE_CHAT_ID"],
        delay_proses=CONFIG["SEND_TIME"],
        storage_path_mp4=CONFIG["STORAGE_PATH"],
    )
    ops.StartEngine()
