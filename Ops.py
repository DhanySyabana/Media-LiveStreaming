import os
import time
import tqdm
import logging
import datetime
from libs.Loggers import Loggers
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest

class Ops:

    def __init__(self, TOKEN:str, CHAT_ID:str, delay_proses:int, storage_path_mp4:dict) -> None:
        self.TOKEN:str= TOKEN,
        self.CHAT_ID:str = CHAT_ID,
        self.start_time = 0
        self.start_proses = True
        self.delay_proses:int = delay_proses
        self.storage_path_mp4:dict = storage_path_mp4
        Loggers()
        super().__init__()

    def send_message(self, message:str) -> int:
        url = F"https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={self.CHAT_ID}&text={message}&parse_mode=html"
        response = HTTPRequest("get", url, headers=None).Hit()
        return response.ok
    
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
                "last_video_filename": os.listdir(value)[-1]
            }

        return data
    
    def parse_message(self, data:dict) -> str:
        key_data = list(data.keys())
        
        cpu_usage_0 = os.popen("ps aux | grep INews.py | grep -v grep | awk '{print $3}'").read()
        memory_usage_0 = os.popen("ps aux | grep INews.py | grep -v grep | awk '{print $4}'").read()
        if cpu_usage_0 == "" : cpu_usage_0 = 0
        if memory_usage_0 == "" : memory_usage_0 = 0

        cpu_usage_1 = os.popen("ps aux | grep CNNIndonesia.py | grep -v grep | awk '{print $3}'").read()
        memory_usage_1 = os.popen("ps aux | grep CNNIndonesia.py | grep -v grep | awk '{print $4}'").read()
        if cpu_usage_1 == "" : cpu_usage_1 = 0
        if memory_usage_1 == "" : memory_usage_1 = 0

        cpu_usage_2 = os.popen("ps aux | grep MetroTV.py | grep -v grep | awk '{print $3}'").read() 
        memory_usage_2 = os.popen("ps aux | grep MetroTV.py | grep -v grep | awk '{print $4}'").read()
        if cpu_usage_2 == "" : cpu_usage_2 = 0
        if memory_usage_2 == "" : memory_usage_2 = 0

        cpu_usage_3 = os.popen("ps aux | grep KompasTV.py | grep -v grep | awk '{print $3}'").read()
        memory_usage_3 = os.popen("ps aux | grep KompasTV.py | grep -v grep | awk '{print $4}'").read()
        if cpu_usage_3 == "" : cpu_usage_3 = 0
        if memory_usage_3 == "" : memory_usage_3 = 0

        cpu_usage_4 = os.popen("ps aux | grep ServerConverter.py | grep -v grep | awk '{print $3}'").read()
        memory_usage_4 = os.popen("ps aux | grep ServerConverter.py | grep -v grep | awk '{print $4}'").read()
        if cpu_usage_4 == "" : cpu_usage_4 = 0
        if memory_usage_4 == "" : memory_usage_4 = 0

        return F"""
            <b>Ops - Live Streaming Status</b>

            {key_data[0]}
            Total Video: {data[key_data[0]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[0]]["total_video_last_hour"]}
            Last Video: {data[key_data[0]]["last_video_filename"]}
            CPU Usage: {float(cpu_usage_0):.2f}%
            Memory Usage: {float(memory_usage_0) * 1024:.2f} MB
            Storage Usage: {data[key_data[0]]["total_size"]:.2f} MB

            {key_data[1]}
            Total Video: {data[key_data[1]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[1]]["total_video_last_hour"]}
            Last Video: {data[key_data[1]]["last_video_filename"]}
            CPU Usage: {float(cpu_usage_1):.2f}%
            Memory Usage: {float(memory_usage_1) * 1024:.2f} MB
            Storage Usage: {data[key_data[1]]["total_size"]:.2f} MB

            {key_data[2]}
            Total Video: {data[key_data[2]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[2]]["total_video_last_hour"]}
            Last Video: {data[key_data[1]]["last_video_filename"]}
            CPU Usage: {float(cpu_usage_2):.2f}%
            Memory Usage: {float(memory_usage_2) * 1024:.2f} MB
            Storage Usage: {data[key_data[2]]["total_size"]:.2f} MB

            {key_data[3]}
            Total Video: {data[key_data[3]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[3]]["total_video_last_hour"]}
            Last Video: {data[key_data[3]]["last_video_filename"]}
            CPU Usage: {float(cpu_usage_3):.2f}%
            Memory Usage: {float(memory_usage_3) * 1024:.2f} MB
            Storage Usage: {data[key_data[3]]["total_size"]:.2f} MB

            ---------------------------------------------

            <b>Server Converter</b>
            CPU Usage: {float(cpu_usage_4):.2f}%
            Memory Usage: {float(memory_usage_4) * 1024:.2f} MB

        """


    def StartEngine(self):
        progress_bar = tqdm.tqdm(total=self.delay_proses, desc="Waiting for next task")
        while self.start_proses:
            try:
                if self.start_time == 0 or time.time() - self.start_time >= self.delay_proses:
                    self.start_time = time.time()
                    data = self.get_file_data()
                    message = self.parse_message(data)
                    self.send_message(message)  
                    logging.info("Success execute task")
                    progress_bar.reset()
                    # os.system('cls' if os.name == 'nt' else 'clear')
                       
                progress_bar.update(1)
                time.sleep(1)       
            except KeyboardInterrupt:
                progress_bar.reset()
                logging.info("Close Ops")
                self.start_proses = False
                break
        progress_bar.close()


if __name__ == "__main__":
    CONFIG = Config()
    OPS_CONFIG = CONFIG.OPS
    ops = Ops(
        TOKEN=OPS_CONFIG["TELE_TOKEN"],
        CHAT_ID=OPS_CONFIG["TELE_CHAT_ID"],
        delay_proses=OPS_CONFIG["SEND_TIME"],
        storage_path_mp4=OPS_CONFIG["STORAGE_PATH"],
    )
    ops.StartEngine()
