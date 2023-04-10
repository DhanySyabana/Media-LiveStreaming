import os
import time
import tqdm
import logging
import datetime
from libs.Loggers import Loggers
from libs.HTTPRequest import HTTPRequest

class Ops:

    def __init__(self) -> None:
        self.TOKEN = "5932299476:AAG4YmekrMEVMHaljj01xOqZX1LuBpjEyBw"
        self.CHAT_ID = "-912205350"
        self.start_time = time.time()
        self.start_proses = True
        self.delay_proses = 60 * 60
        self.storage_path_mp4 = {
            "INEWSSTREAMING": "/home/kabayangroup/www/produksi-tv/public/video_list/INEWSSTREAMING",
            "CNNSTREAMING": "/home/kabayangroup/www/produksi-tv/public/video_list/CNNSTREAMING",
            "METROSTREAMING": "/home/kabayangroup/www/produksi-tv/public/video_list/METROTVSTREAMING",
            "KOMPASSTREAMING": "/home/kabayangroup/www/produksi-tv/public/video_list/KOMPASSTREAMING",
        }
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
            total_video_last_hour = len([name for name in os.listdir(value) if name.endswith(".mp4") and datetime.datetime.fromtimestamp(os.path.getmtime(F"{value}/{name}")).hour == datetime.datetime.now().hour])
            data[key] = {
                "total_video": total_video,
                "total_video_last_hour": total_video_last_hour,
                "last_video_filename": sorted(os.listdir(value), key=lambda x: os.path.getmtime(F"{value}/{x}"))[-1],
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

        return F"""
            <b>Ops - Live Streaming Status</b>

            {key_data[0]}
            Total Video: {data[key_data[0]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[0]]["total_video_last_hour"]}
            Last Video: {data[key_data[0]]["last_video_filename"]}
            CPU Usage: {float(cpu_usage_0):.2f}%
            Memory Usage: {float(memory_usage_0)/1024:.2f} MB

            {key_data[1]}
            Total Video: {data[key_data[1]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[1]]["total_video_last_hour"]}
            Last Video: {data[key_data[1]]["last_video_filename"]}
            CPU Usage: {float(cpu_usage_1):.2f}%
            Memory Usage: {float(memory_usage_1)/1024:.2f} MB

            {key_data[2]}
            Total Video: {data[key_data[2]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[2]]["total_video_last_hour"]}
            Last Video: {data[key_data[1]]["last_video_filename"]}
            CPU Usage: {float(cpu_usage_2):.2f}%
            Memory Usage: {float(memory_usage_2)/1024:.2f} MB

            {key_data[3]}
            Total Video: {data[key_data[3]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[3]]["total_video_last_hour"]}
            Last Video: {data[key_data[3]]["last_video_filename"]}
            CPU Usage: {float(cpu_usage_3):.2f}%
            Memory Usage: {float(memory_usage_3)/1024:.2f} MB

        """


    def StartEngine(self):
        progress_bar = tqdm.tqdm(total=self.delay_proses, desc="Waiting for next task")
        while self.start_proses:
            try:
                if time.time() - self.start_time >= self.delay_proses:
                    self.start_time = time.time()
                    data = self.get_file_data()
                    message = self.parse_message(data)
                    self.send_message(message)  
                    logging.info("Success execute task")
                    progress_bar.reset()
                    os.system("clear")
                       
                progress_bar.update(1)
                time.sleep(1)       
            except KeyboardInterrupt:
                progress_bar.reset()
                logging.info("Close Ops")
                self.start_proses = False
                break
        progress_bar.close()


if __name__ == "__main__":
    ops = Ops()
    ops.StartEngine()