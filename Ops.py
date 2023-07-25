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
        gs = GridSpec(nrows=4, ncols=5, figure=fig)

        # update margin 
        plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.1, hspace=0.1)

        # Add a line plot to the upper left subplot
        ax1 = fig.add_subplot(gs[0, 0])

        color = "black"
        if data[key_data[0]]["total_video_last_hour"] < 6:
            color = "red"
            ax1.spines['bottom'].set_color('red')
            ax1.spines['top'].set_color('red')
            ax1.spines['right'].set_color('red')
            ax1.spines['left'].set_color('red')

        ax1.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax1.text(0.5, 0.5, key_data[0], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax1.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax1.text(0.5, 0.3, data[key_data[0]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax1.set_xticks([])
        ax1.set_yticks([])

        # Add a bar plot to the upper right subplot
        ax2 = fig.add_subplot(gs[0, 1])
        color = "black"
        if data[key_data[1]]["total_video_last_hour"] < 6:
            color = "red"
            ax2.spines['bottom'].set_color('red')
            ax2.spines['top'].set_color('red')
            ax2.spines['right'].set_color('red')
            ax2.spines['left'].set_color('red')
        
        ax2.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax2.text(0.5, 0.5, key_data[1], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax2.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax2.text(0.5, 0.3, data[key_data[1]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax2.set_xticks([])
        ax2.set_yticks([])

        # Add a scatter plot to the lower left subplot
        ax3 = fig.add_subplot(gs[0, 2])
        color = "black"
        if data[key_data[2]]["total_video_last_hour"] < 6:
            color = "red"
            ax3.spines['bottom'].set_color('red')
            ax3.spines['top'].set_color('red')
            ax3.spines['right'].set_color('red')
            ax3.spines['left'].set_color('red')

        ax3.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax3.text(0.5, 0.5, key_data[2], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax3.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax3.text(0.5, 0.3, data[key_data[2]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax3.set_xticks([])
        ax3.set_yticks([])

        # Add a text box to the lower right subplot
        ax4 = fig.add_subplot(gs[0, 3])
        color = "black"
        if data[key_data[3]]["total_video_last_hour"] < 6:
            color = "red"
            ax4.spines['bottom'].set_color('red')
            ax4.spines['top'].set_color('red')
            ax4.spines['right'].set_color('red')
            ax4.spines['left'].set_color('red')
        ax4.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax4.text(0.5, 0.5, key_data[3], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax4.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax4.text(0.5, 0.3, data[key_data[3]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax4.set_xticks([])
        ax4.set_yticks([])

        ax5 = fig.add_subplot(gs[0, 4])
        color = "black"
        if data[key_data[4]]["total_video_last_hour"] < 6:
            color = "red"
            ax5.spines['bottom'].set_color('red')
            ax5.spines['top'].set_color('red')
            ax5.spines['right'].set_color('red')
            ax5.spines['left'].set_color('red')

        ax5.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax5.text(0.5, 0.5, key_data[4], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax5.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax5.text(0.5, 0.3, data[key_data[4]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax5.set_xticks([])
        ax5.set_yticks([])

        ax6 = fig.add_subplot(gs[1, 0])
        color = "black"
        if data[key_data[5]]["total_video_last_hour"] < 6:
            color = "red"
            ax6.spines['bottom'].set_color('red')
            ax6.spines['top'].set_color('red')
            ax6.spines['right'].set_color('red')
            ax6.spines['left'].set_color('red')
        ax6.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax6.text(0.5, 0.5, key_data[5], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax6.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax6.text(0.5, 0.3, data[key_data[5]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax6.set_xticks([])
        ax6.set_yticks([])

        ax7 = fig.add_subplot(gs[1, 1])
        color = "black"
        if data[key_data[6]]["total_video_last_hour"] < 6:
            color = "red"
            ax7.spines['bottom'].set_color('red')
            ax7.spines['top'].set_color('red')
            ax7.spines['right'].set_color('red')
            ax7.spines['left'].set_color('red')
        ax7.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax7.text(0.5, 0.5, key_data[6], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax7.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax7.text(0.5, 0.3, data[key_data[6]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax7.set_xticks([])
        ax7.set_yticks([])

        ax8 = fig.add_subplot(gs[1, 2])
        color = "black"
        if data[key_data[7]]["total_video_last_hour"] < 6:
            color = "red"
            ax8.spines['bottom'].set_color('red')
            ax8.spines['top'].set_color('red')
            ax8.spines['right'].set_color('red')
            ax8.spines['left'].set_color('red')
        ax8.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax8.text(0.5, 0.5, key_data[7], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax8.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax8.text(0.5, 0.3, data[key_data[7]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax8.set_xticks([])
        ax8.set_yticks([])

        ax9 = fig.add_subplot(gs[1, 3])
        color = "black"
        if data[key_data[8]]["total_video_last_hour"] < 6:
            color = "red"
            ax9.spines['bottom'].set_color('red')
            ax9.spines['top'].set_color('red')
            ax9.spines['right'].set_color('red')
            ax9.spines['left'].set_color('red')
        ax9.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax9.text(0.5, 0.5, key_data[8], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax9.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax9.text(0.5, 0.3, data[key_data[8]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax9.set_xticks([])
        ax9.set_yticks([])

        ax10 = fig.add_subplot(gs[1, 4])
        color = "black"
        if data[key_data[9]]["total_video_last_hour"] < 6:
            color = "red"
            ax10.spines['bottom'].set_color('red')
            ax10.spines['top'].set_color('red')
            ax10.spines['right'].set_color('red')
            ax10.spines['left'].set_color('red')
        ax10.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax10.text(0.5, 0.5, key_data[9], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax10.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax10.text(0.5, 0.3, data[key_data[9]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax10.set_xticks([])
        ax10.set_yticks([])

        ax11 = fig.add_subplot(gs[2, 0])
        color = "black"
        if data[key_data[10]]["total_video_last_hour"] < 6:
            color = "red"
            ax11.spines['bottom'].set_color('red')
            ax11.spines['top'].set_color('red')
            ax11.spines['right'].set_color('red')
            ax11.spines['left'].set_color('red')
        ax11.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax11.text(0.5, 0.5, key_data[10], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax11.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax11.text(0.5, 0.3, data[key_data[10]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax11.set_xticks([])
        ax11.set_yticks([])

        ax12 = fig.add_subplot(gs[2, 1])
        color = "black"
        if data[key_data[11]]["total_video_last_hour"] < 6:
            color = "red"
            ax12.spines['bottom'].set_color('red')
            ax12.spines['top'].set_color('red')
            ax12.spines['right'].set_color('red')
            ax12.spines['left'].set_color('red')
        ax12.text(0.5, 0.6, 'CHANNEL', ha='center', va='center', fontsize=10, weight='bold')
        ax12.text(0.5, 0.5, key_data[11], ha='center', va='center', fontsize=16, weight='bold', color=color)
        ax12.text(0.5, 0.4, 'LAST VIDEO', ha='center', va='center', fontsize=10, weight='bold')
        ax12.text(0.5, 0.3, data[key_data[11]]["last_video_filename"], ha='center', va='center', fontsize=10, weight='bold')
        ax12.set_xticks([])
        ax12.set_yticks([])

        total_video = [data[key_data[0]]["total_video"], data[key_data[1]]["total_video"], data[key_data[2]]["total_video"], data[key_data[3]]["total_video"], data[key_data[4]]["total_video"], data[key_data[5]]["total_video"], data[key_data[6]]["total_video"], data[key_data[7]]["total_video"], data[key_data[8]]["total_video"], data[key_data[9]]["total_video"], data[key_data[10]]["total_video"], data[key_data[11]]["total_video"]]
        labels = [key_data[0], key_data[1], key_data[2], key_data[3], key_data[4], key_data[5], key_data[6], key_data[7],  key_data[8], key_data[9],key_data[10],key_data[11]]
        colors = plt.cm.Set2(np.linspace(0, 1, len(labels)))
        
        # explode with a bigger value of total_video
        explode = [0.1 if i == max(total_video) else 0 for i in total_video]

        # Add a pie plot to the lower row
        if max(total_video) > 0:
            ax_total_video = fig.add_subplot(gs[3, 2:4])
            # handle autopct, cannot convert float NaN to integer
            autopct = lambda p: '{:.0f}'.format(p * sum(total_video) / 100) if p > 0 else ''
            _, _, autotexts = ax_total_video.pie(total_video, radius=1, colors=colors, autopct=autopct, pctdistance=0.8, startangle=90, explode=explode, wedgeprops = { 'linewidth': 2, "edgecolor" :"k" })
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
        total_video_last_hour = [data[key_data[0]]["total_video_last_hour"], data[key_data[1]]["total_video_last_hour"], data[key_data[2]]["total_video_last_hour"], data[key_data[3]]["total_video_last_hour"], data[key_data[4]]["total_video_last_hour"], data[key_data[5]]["total_video_last_hour"], data[key_data[6]]["total_video_last_hour"], data[key_data[7]]["total_video_last_hour"],  data[key_data[8]]["total_video_last_hour"], data[key_data[9]]["total_video_last_hour"], data[key_data[10]]["total_video_last_hour"], data[key_data[11]]["total_video_last_hour"]]
        labels = [key_data[0], key_data[1], key_data[2], key_data[3], key_data[4], key_data[5], key_data[6], key_data[7], key_data[8], key_data[9], key_data[10], key_data[11]]

        # explode with a bigger value of total_video_last_hour
        explode = [0.1 if i == max(total_video_last_hour) else 0 for i in total_video_last_hour]

        # Add a pie plot to the lower row
        if max(total_video_last_hour) > 0:
            ax_total_video_1_hour = fig.add_subplot(gs[3, 4:6])
            autopct = lambda p: '{:.0f}'.format(p * sum(total_video_last_hour) / 100) if p > 0 else ''
            _, _, autotexts = ax_total_video_1_hour.pie(total_video_last_hour, radius=1, colors=colors, autopct=autopct, pctdistance=0.8, startangle=90, explode=explode, wedgeprops = { 'linewidth': 2, "edgecolor" :"k" })
            for autotext in autotexts:
                autotext.set_color('white')
            handles = []
            for i, l in enumerate(labels):
                handles.append(mpatches.Patch(color=colors[i], label=l))
            # use a list comprehension to update the labels
            labels = [f'{l}: {s}' for l, s in zip(labels, total_video_last_hour)]
            ax_total_video_1_hour.legend(handles,labels, bbox_to_anchor=(0.85, 1.025), loc="upper left", fontsize=10, frameon=False)
            ax_total_video_1_hour.set_title('TOTAL VIDEO LAST ONE HOUR', weight='bold', fontsize=16)

        # total storage
        total_size = [data[key_data[0]]["total_size"], data[key_data[1]]["total_size"], data[key_data[2]]["total_size"], data[key_data[3]]["total_size"], data[key_data[4]]["total_size"], data[key_data[5]]["total_size"], data[key_data[6]]["total_size"], data[key_data[7]]["total_size"], data[key_data[8]]["total_size"], data[key_data[9]]["total_size"], data[key_data[10]]["total_size"], data[key_data[11]]["total_size"]]
        labels = [key_data[0], key_data[1], key_data[2], key_data[3], key_data[4], key_data[5], key_data[6], key_data[7], key_data[8],  key_data[9], key_data[10], key_data[11]]

        # explode with a bigger value of total_video_last_hour
        explode = [0.1 if i == min(total_size) else 0 for i in total_size]

        # Add a pie plot to the lower row
        if max(total_size) > 0:
            ax_storage = fig.add_subplot(gs[3, 0:2])
            autopct = lambda p: '{:.0f}'.format(p * sum(total_size) / 100) if p > 0 else ''
            _, _, autotexts = ax_storage.pie(total_size, radius=1, colors=colors, autopct=autopct, pctdistance=0.8, startangle=90, explode=explode, wedgeprops = { 'linewidth': 2, "edgecolor" :"k" })
            for autotext in autotexts:
                autotext.set_color('white')
            handles = []
            for i, l in enumerate(labels):
                handles.append(mpatches.Patch(color=colors[i], label=l))

            # use a list comprehension to update the labels
            labels = [f'{l}: {s} MB' for l, s in zip(labels, total_size)]
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
