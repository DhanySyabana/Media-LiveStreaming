import os
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

        # Create a figure and GridSpec object
        fig = plt.figure(figsize=(23, 10))
        gs = GridSpec(nrows=2, ncols=5, figure=fig)

        # update margin 
        plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.1, hspace=0.1)

        if data[key_data[0]]["total_video_last_hour"] < 2:
            # Add a line plot to the upper left subplot
            ax1 = fig.add_subplot(gs[0, 0])

            color = "red"
            # if data[key_data[0]]["total_video_last_hour"] < 2:
            #     color = "red"
            #     ax1.spines['bottom'].set_color('red')
            #     ax1.spines['top'].set_color('red')
            #     ax1.spines['right'].set_color('red')
            #     ax1.spines['left'].set_color('red')

            ax1.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
            ax1.text(0.5, 0.5, key_data[0], ha='center', va='center', fontsize=16, weight='bold', color=color)
            ax1.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
            ax1.text(0.5, 0.3, data[key_data[0]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
            ax1.set_xticks([])
            ax1.set_yticks([])

        # Add a bar plot to the upper right subplot
        if data[key_data[1]]["total_video_last_hour"] < 2:
            ax2 = fig.add_subplot(gs[0, 1])
            color = "red"
            # if data[key_data[1]]["total_video_last_hour"] < 2:
            #     color = "red"
            #     ax2.spines['bottom'].set_color('red')
            #     ax2.spines['top'].set_color('red')
            #     ax2.spines['right'].set_color('red')
            #     ax2.spines['left'].set_color('red')
            
            ax2.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
            ax2.text(0.5, 0.5, key_data[1], ha='center', va='center', fontsize=16, weight='bold', color=color)
            ax2.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
            ax2.text(0.5, 0.3, data[key_data[1]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
            ax2.set_xticks([])
            ax2.set_yticks([])

        # Add a scatter plot to the lower left subplot
        if data[key_data[2]]["total_video_last_hour"] < 2:
            ax3 = fig.add_subplot(gs[0, 2])
            color = "red"
            # if data[key_data[2]]["total_video_last_hour"] < 2:
            #     color = "red"
            #     ax3.spines['bottom'].set_color('red')
            #     ax3.spines['top'].set_color('red')
            #     ax3.spines['right'].set_color('red')
            #     ax3.spines['left'].set_color('red')

            ax3.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
            ax3.text(0.5, 0.5, key_data[2], ha='center', va='center', fontsize=16, weight='bold', color=color)
            ax3.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
            ax3.text(0.5, 0.3, data[key_data[2]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
            ax3.set_xticks([])
            ax3.set_yticks([])

        # Add a text box to the lower right subplot
        if data[key_data[3]]["total_video_last_hour"] < 2:
            ax4 = fig.add_subplot(gs[0, 3])
            color = "red"
            # if data[key_data[3]]["total_video_last_hour"] < 2:
            #     color = "red"
            #     ax4.spines['bottom'].set_color('red')
            #     ax4.spines['top'].set_color('red')
            #     ax4.spines['right'].set_color('red')
            #     ax4.spines['left'].set_color('red')
            ax4.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
            ax4.text(0.5, 0.5, key_data[3], ha='center', va='center', fontsize=16, weight='bold', color=color)
            ax4.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
            ax4.text(0.5, 0.3, data[key_data[3]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
            ax4.set_xticks([])
        ax4.set_yticks([])

        if data[key_data[4]]["total_video_last_hour"] < 2:
            ax5 = fig.add_subplot(gs[0, 4])
            color = "red"
            # if data[key_data[4]]["total_video_last_hour"] < 2:
            #     color = "red"
            #     ax5.spines['bottom'].set_color('red')
            #     ax5.spines['top'].set_color('red')
            #     ax5.spines['right'].set_color('red')
            #     ax5.spines['left'].set_color('red')

            ax5.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
            ax5.text(0.5, 0.5, key_data[4], ha='center', va='center', fontsize=16, weight='bold', color=color)
            ax5.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
            ax5.text(0.5, 0.3, data[key_data[4]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
            ax5.set_xticks([])
            ax5.set_yticks([])

        if data[key_data[5]]["total_video_last_hour"] < 2:
            ax6 = fig.add_subplot(gs[1, 0])
            color = "red"
            # if data[key_data[5]]["total_video_last_hour"] < 2:
            #     color = "red"
            #     ax6.spines['bottom'].set_color('red')
            #     ax6.spines['top'].set_color('red')
            #     ax6.spines['right'].set_color('red')
            #     ax6.spines['left'].set_color('red')
            ax6.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
            ax6.text(0.5, 0.5, key_data[5], ha='center', va='center', fontsize=16, weight='bold', color=color)
            ax6.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
            ax6.text(0.5, 0.3, data[key_data[5]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
            ax6.set_xticks([])
            ax6.set_yticks([])

        if data[key_data[6]]["total_video_last_hour"] < 2:
            ax7 = fig.add_subplot(gs[1, 1])
            color = "red"
            # if data[key_data[6]]["total_video_last_hour"] < 2:
            #     color = "red"
            #     ax7.spines['bottom'].set_color('red')
            #     ax7.spines['top'].set_color('red')
            #     ax7.spines['right'].set_color('red')
            #     ax7.spines['left'].set_color('red')
            ax7.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
            ax7.text(0.5, 0.5, key_data[6], ha='center', va='center', fontsize=16, weight='bold', color=color)
            ax7.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
            ax7.text(0.5, 0.3, data[key_data[6]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
            ax7.set_xticks([])
            ax7.set_yticks([])

        if data[key_data[7]]["total_video_last_hour"] < 2:
            ax8 = fig.add_subplot(gs[1, 2])
            color = "red"
            # if data[key_data[7]]["total_video_last_hour"] < 2:
            #     color = "red"
            #     ax8.spines['bottom'].set_color('red')
            #     ax8.spines['top'].set_color('red')
            #     ax8.spines['right'].set_color('red')
            #     ax8.spines['left'].set_color('red')
            ax8.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
            ax8.text(0.5, 0.5, key_data[7], ha='center', va='center', fontsize=16, weight='bold', color=color)
            ax8.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
            ax8.text(0.5, 0.3, data[key_data[7]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
            ax8.set_xticks([])
            ax8.set_yticks([])

        if data[key_data[8]]["total_video_last_hour"] < 2:
            ax9 = fig.add_subplot(gs[1, 3])
            color = "red"
            # if data[key_data[8]]["total_video_last_hour"] < 2:
            #     color = "red"
            #     ax9.spines['bottom'].set_color('red')
            #     ax9.spines['top'].set_color('red')
            #     ax9.spines['right'].set_color('red')
            #     ax9.spines['left'].set_color('red')
            ax9.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
            ax9.text(0.5, 0.5, key_data[8], ha='center', va='center', fontsize=16, weight='bold', color=color)
            ax9.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
            ax9.text(0.5, 0.3, data[key_data[8]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
            ax9.set_xticks([])
            ax9.set_yticks([])

        filename = F"notif-{datetime.now().strftime('%Y-%m-%d-%H-%M')}.png"

        # Adjust the layout and spacing
        fig.tight_layout()
        fig.savefig(F"static/{filename}", dpi=300)

        url = F"https://api.telegram.org/bot{self.TOKEN}/sendPhoto?chat_id={self.CHAT_ID}"
        response = requests.post(url, files={"photo": open(F"static/{filename}", "rb")})
        if response.ok:
            os.remove(F"static/{filename}")
            logging.info("Send chart to telegram")


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
    CONFIG = Config().OPSV2
    ops = Ops(
        TOKEN=CONFIG["TELE_TOKEN"],
        CHAT_ID=CONFIG["TELE_CHAT_ID"],
        delay_proses=CONFIG["SEND_TIME"],
        storage_path_mp4=CONFIG["STORAGE_PATH"],
    )
    ops.StartEngine()
