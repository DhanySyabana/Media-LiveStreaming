import os
import glob
import time
import tqdm
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

            # total video last 60 minutes
            total_video_last_hour = len([name for name in os.listdir(value) if name.endswith(".mp4") and (time.time() - os.path.getmtime(F"{value}/{name}")) < 3600])
            data[key] = {
                "total_video": total_video,
                "total_size": sum(os.path.getsize(F"{value}/{name}") for name in os.listdir(value) if name.endswith(".mp4")) / 1024 / 1024,
                "total_video_last_hour": total_video_last_hour,
                "last_video_filename": "-",
            }

            if total_video_last_hour > 0:
                data[key]["last_video_filename"] = max(glob.iglob(F"{value}/*.mp4"), key=os.path.getctime).split("/")[-1]

        return data
    
    def generate_send_chart(self, data:dict) -> None:
        key_data = list(data.keys())

        # Create a figure and GridSpec object
        fig = plt.figure(figsize=(23, 7))
        gs = GridSpec(nrows=2, ncols=6, figure=fig)

        # update margin 
        plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.1, hspace=0.1)

        # Add a line plot to the upper left subplot
        ax1 = fig.add_subplot(gs[0, 0])

        ax1.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax1.text(0.5, 0.5, key_data[0], ha='center', va='center', fontsize=16, weight='bold')
        ax1.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax1.text(0.5, 0.3, data[key_data[0]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax1.set_xticks([])
        ax1.set_yticks([])

        # Add a bar plot to the upper right subplot
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax2.text(0.5, 0.5, key_data[1], ha='center', va='center', fontsize=16, weight='bold')
        ax2.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax2.text(0.5, 0.3, data[key_data[1]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax2.set_xticks([])
        ax2.set_yticks([])

        # Add a scatter plot to the lower left subplot
        ax3 = fig.add_subplot(gs[0, 2])
        ax3.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax3.text(0.5, 0.5, key_data[2], ha='center', va='center', fontsize=16, weight='bold')
        ax3.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax3.text(0.5, 0.3, data[key_data[2]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax3.set_xticks([])
        ax3.set_yticks([])

        # Add a text box to the lower right subplot
        ax4 = fig.add_subplot(gs[0, 3])
        ax4.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax4.text(0.5, 0.5, key_data[3], ha='center', va='center', fontsize=16, weight='bold')
        ax4.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax4.text(0.5, 0.3, data[key_data[3]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax4.set_xticks([])
        ax4.set_yticks([])

        ax5 = fig.add_subplot(gs[0, 4])
        ax5.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax5.text(0.5, 0.5, key_data[4], ha='center', va='center', fontsize=16, weight='bold')
        ax5.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax5.text(0.5, 0.3, data[key_data[4]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax5.set_xticks([])
        ax5.set_yticks([])

        ax6 = fig.add_subplot(gs[0, 5])
        ax6.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax6.text(0.5, 0.5, key_data[5], ha='center', va='center', fontsize=16, weight='bold')
        ax6.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax6.text(0.5, 0.3, data[key_data[5]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax6.set_xticks([])
        ax6.set_yticks([])

        total_video = [data[key_data[0]]["total_video"], data[key_data[1]]["total_video"], data[key_data[2]]["total_video"], data[key_data[3]]["total_video"], data[key_data[4]]["total_video"], data[key_data[5]]["total_video"]]
        labels = [key_data[0], key_data[1], key_data[2], key_data[3], key_data[4], key_data[5]]
        colors = plt.cm.Set2(np.linspace(0, 1, len(labels)))
        
        # explode with a bigger value of total_video
        explode = [0.1 if i == max(total_video) else 0 for i in total_video]

        # Add a pie plot to the lower row
        ax_total_video = fig.add_subplot(gs[1, 2:4])
        _, _, autotexts = ax_total_video.pie(total_video, radius=1, colors=colors, autopct='%1.1f%%', pctdistance=0.8, startangle=90, explode=explode, wedgeprops = { 'linewidth': 2, "edgecolor" :"k" })
        for autotext in autotexts:
            autotext.set_color('white')
        handles = []
        for i, l in enumerate(labels):
            handles.append(mpatches.Patch(color=colors[i], label=l))
        # use a list comprehension to update the labels
        labels = [f'{l}: {s}' for l, s in zip(labels, total_video)]
        ax_total_video.legend(handles,labels, bbox_to_anchor=(0.85, 1.025), loc="upper left", fontsize=10, frameon=False)
        ax_total_video.set_title('TOTAL VIDEO', weight='bold', fontsize=16)

        # total last video
        total_video_last_hour = [data[key_data[0]]["total_video_last_hour"], data[key_data[1]]["total_video_last_hour"], data[key_data[2]]["total_video_last_hour"], data[key_data[3]]["total_video_last_hour"], data[key_data[4]]["total_video_last_hour"], data[key_data[5]]["total_video_last_hour"]]
        labels = [key_data[0], key_data[1], key_data[2], key_data[3], key_data[4], key_data[5]]

        # explode with a bigger value of total_video_last_hour
        explode = [0.1 if i == min(total_video_last_hour) else 0 for i in total_video_last_hour]

        # Add a pie plot to the lower row
        ax_total_video_1_hour = fig.add_subplot(gs[1, 4:6])
        _, _, autotexts = ax_total_video_1_hour.pie(total_video_last_hour, radius=1, colors=colors, autopct='%1.1f%%', pctdistance=0.8, startangle=90, explode=explode, wedgeprops = { 'linewidth': 2, "edgecolor" :"k" })
        for autotext in autotexts:
            autotext.set_color('white')
        handles = []
        for i, l in enumerate(labels):
            handles.append(mpatches.Patch(color=colors[i], label=l))
        # use a list comprehension to update the labels
        labels = [f'{l}: {s}' for l, s in zip(labels, total_video_last_hour)]
        ax_total_video_1_hour.legend(handles,labels, bbox_to_anchor=(0.85, 1.025), loc="upper left", fontsize=10, frameon=False)
        ax_total_video_1_hour.set_title('TOTAL VIDEO LAST ONE HOUR', weight='bold', fontsize=16)

        # total last video
        total_storage = [data[key_data[0]]["total_storage"], data[key_data[1]]["total_storage"], data[key_data[2]]["total_storage"], data[key_data[3]]["total_storage"], data[key_data[4]]["total_storage"], data[key_data[5]]["total_storage"]]
        labels = [key_data[0], key_data[1], key_data[2], key_data[3], key_data[4], key_data[5]]

        # explode with a bigger value of total_video_last_hour
        explode = [0.1 if i == min(total_storage) else 0 for i in total_storage]

        # Add a pie plot to the lower row
        ax_storage = fig.add_subplot(gs[1, 0:2])
        _, _, autotexts = ax_storage.pie(total_storage, radius=1, colors=colors, autopct='%1.1f%%', pctdistance=0.8, startangle=90, explode=explode, wedgeprops = { 'linewidth': 2, "edgecolor" :"k" })
        for autotext in autotexts:
            autotext.set_color('white')
        handles = []
        for i, l in enumerate(labels):
            handles.append(mpatches.Patch(color=colors[i], label=l))

        # use a list comprehension to update the labels
        labels = [f'{l}: {s} MB' for l, s in zip(labels, total_storage)]
        ax_storage.legend(handles,labels, bbox_to_anchor=(0.85, 1.025), loc="upper left", fontsize=10, frameon=False)
        ax_storage.set_title('STORAGE USAGE', weight='bold', fontsize=16)

        filename = F"chart-{datetime.now().strftime('%Y-%m-%d-%H-%M')}.png"

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
    CONFIG = Config().OPS
    ops = Ops(
        TOKEN=CONFIG["TELE_TOKEN"],
        CHAT_ID=CONFIG["TELE_CHAT_ID"],
        delay_proses=CONFIG["SEND_TIME"],
        storage_path_mp4=CONFIG["STORAGE_PATH"],
    )
    ops.StartEngine()
