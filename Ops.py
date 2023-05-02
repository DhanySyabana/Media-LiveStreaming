import os
import glob
import time
import tqdm
import logging
from libs.Loggers import Loggers
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest

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

    def send_message(self, message:str) -> int:
        try:
            url = F"https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={self.CHAT_ID}&text={message}&parse_mode=html"
            response = HTTPRequest("get", url, headers=None).Hit()
            return response.ok
        except Exception as e:
            logging.error(F"Error send message: {e}")
            return 0
    
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
                "last_video_filename": max(glob.iglob(F"{value}/*.mp4"), key=os.path.getctime).split("/")[-1],
            }

        return data
    
    def parse_message(self, data:dict) -> str:
        key_data = list(data.keys())

        cpu_usage_0 = os.popen("ps aux | grep INewsV1.py | grep -v grep | awk '{print $3}'").read()
        if cpu_usage_0.find("\n") != -1:
            cpu_usage_0 = cpu_usage_0.split("\n")[0]
        memory_usage_0 = os.popen("ps aux | grep INewsV1.py | grep -v grep | awk '{print $4}'").read()
        if memory_usage_0.find("\n") != -1:
            memory_usage_0 = memory_usage_0.split("\n")[0]
        if cpu_usage_0 == "" : cpu_usage_0 = 0
        if memory_usage_0 == "" : memory_usage_0 = 0

        cpu_usage_1 = os.popen("ps aux | grep CNNIndonesia.py | grep -v grep | awk '{print $3}'").read()
        if cpu_usage_1.find("\n") != -1:
            cpu_usage_1 = cpu_usage_1.split("\n")[0]
        memory_usage_1 = os.popen("ps aux | grep CNNIndonesia.py | grep -v grep | awk '{print $4}'").read()
        if memory_usage_1.find("\n") != -1:
            memory_usage_1 = memory_usage_1.split("\n")[0]
        if cpu_usage_1 == "" : cpu_usage_1 = 0
        if memory_usage_1 == "" : memory_usage_1 = 0

        cpu_usage_2 = os.popen("ps aux | grep MetroTV.py | grep -v grep | awk '{print $3}'").read() 
        if cpu_usage_2.find("\n") != -1:
            cpu_usage_2 = cpu_usage_2.split("\n")[0]
        memory_usage_2 = os.popen("ps aux | grep MetroTV.py | grep -v grep | awk '{print $4}'").read()
        if memory_usage_2.find("\n") != -1:
            memory_usage_2 = memory_usage_2.split("\n")[0]
        if cpu_usage_2 == "" : cpu_usage_2 = 0
        if memory_usage_2 == "" : memory_usage_2 = 0

        cpu_usage_3 = os.popen("ps aux | grep KompasTV.py | grep -v grep | awk '{print $3}'").read()
        if cpu_usage_3.find("\n") != -1:
            cpu_usage_3 = cpu_usage_3.split("\n")[0]
        memory_usage_3 = os.popen("ps aux | grep KompasTV.py | grep -v grep | awk '{print $4}'").read()
        if memory_usage_3.find("\n") != -1:
            memory_usage_3 = memory_usage_3.split("\n")[0]
        if cpu_usage_3 == "" : cpu_usage_3 = 0
        if memory_usage_3 == "" : memory_usage_3 = 0

        cpu_usage_4 = os.popen("ps aux | grep ServerConverter.py | grep -v grep | awk '{print $3}'").read()
        if cpu_usage_4.find("\n") != -1:
            cpu_usage_4 = cpu_usage_4.split("\n")[0]
        memory_usage_4 = os.popen("ps aux | grep ServerConverter.py | grep -v grep | awk '{print $4}'").read()
        if memory_usage_4.find("\n") != -1:
            memory_usage_4 = memory_usage_4.split("\n")[0]
        if cpu_usage_4 == "" : cpu_usage_4 = 0
        if memory_usage_4 == "" : memory_usage_4 = 0

        cpu_usage_5 = os.popen("ps aux | grep CNBCIndonesia.py | grep -v grep | awk '{print $3}'").read()
        if cpu_usage_5.find("\n") != -1:
            cpu_usage_5 = cpu_usage_5.split("\n")[0]
        memory_usage_5 = os.popen("ps aux | grep CNBCIndonesia.py | grep -v grep | awk '{print $4}'").read()
        if memory_usage_5.find("\n") != -1:
            memory_usage_5 = memory_usage_5.split("\n")[0]
        if cpu_usage_5 == "" : cpu_usage_5 = 0
        if memory_usage_5 == "" : memory_usage_5 = 0

        cpu_usage_6 = os.popen("ps aux | grep IDXIndonesiaV1.py | grep -v grep | awk '{print $3}'").read()
        if cpu_usage_6.find("\n") != -1:
            cpu_usage_6 = cpu_usage_6.split("\n")[0]
        memory_usage_6 = os.popen("ps aux | grep IDXIndonesiaV1.py | grep -v grep | awk '{print $4}'").read()
        if memory_usage_6.find("\n") != -1:
            memory_usage_6 = memory_usage_6.split("\n")[0]
        if cpu_usage_6 == "" : cpu_usage_6 = 0
        if memory_usage_6 == "" : memory_usage_6 = 0

        return F"""
        
            <b>Ops - Live Streaming Status</b>

            <b>{key_data[0]}</b>
            Total Video: {data[key_data[0]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[0]]["total_video_last_hour"]}
            Last Video: {data[key_data[0]]["last_video_filename"]}

            CPU Usage: {float(cpu_usage_0):.2f}%
            Memory Usage: {float(memory_usage_0):.2f} MB
            Storage Usage: {data[key_data[0]]["total_size"]:.2f} MB

            <b>{key_data[1]}</b>
            Total Video: {data[key_data[1]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[1]]["total_video_last_hour"]}
            Last Video: {data[key_data[1]]["last_video_filename"]}

            CPU Usage: {float(cpu_usage_1):.2f}%
            Memory Usage: {float(memory_usage_1):.2f} MB
            Storage Usage: {data[key_data[1]]["total_size"]:.2f} MB

            <b>{key_data[2]}</b>
            Total Video: {data[key_data[2]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[2]]["total_video_last_hour"]}
            Last Video: {data[key_data[2]]["last_video_filename"]}

            CPU Usage: {float(cpu_usage_2):.2f}%
            Memory Usage: {float(memory_usage_2):.2f} MB
            Storage Usage: {data[key_data[2]]["total_size"]:.2f} MB

            <b>{key_data[3]}</b>
            Total Video: {data[key_data[3]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[3]]["total_video_last_hour"]}
            Last Video: {data[key_data[3]]["last_video_filename"]}

            CPU Usage: {float(cpu_usage_3):.2f}%
            Memory Usage: {float(memory_usage_3):.2f} MB
            Storage Usage: {data[key_data[3]]["total_size"]:.2f} MB

            <b>{key_data[4]}</b>
            Total Video: {data[key_data[4]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[4]]["total_video_last_hour"]}
            Last Video: {data[key_data[4]]["last_video_filename"]}

            CPU Usage: {float(cpu_usage_5):.2f}%
            Memory Usage: {float(memory_usage_5):.2f} MB
            Storage Usage: {data[key_data[4]]["total_size"]:.2f} MB

            <b>{key_data[5]}</b>
            Total Video: {data[key_data[5]]["total_video"]}
            Total Video Last 1 Hour: {data[key_data[5]]["total_video_last_hour"]}
            Last Video: {data[key_data[5]]["last_video_filename"]}

            CPU Usage: {float(cpu_usage_6):.2f}%
            Memory Usage: {float(memory_usage_6):.2f} MB
            Storage Usage: {data[key_data[5]]["total_size"]:.2f} MB

            --------------------------------------------------------------

            <b>Server Converter</b>
            CPU Usage: {float(cpu_usage_4):.2f}%
            Memory Usage: {float(memory_usage_4):.2f} MB


        """


    def execute(self) -> None:
        try:
            self.start_time = time.time()
            data = self.get_file_data()
            message = self.parse_message(data)
            self.send_message(message)
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
