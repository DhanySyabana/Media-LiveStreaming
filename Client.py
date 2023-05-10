import os
import time
import socket
import struct
import logging
import requests
import matplotlib.pyplot as plt
from datetime import datetime
from libs.Loggers import Loggers
from libs.Database import Database
from settings.Config import Config

class Client:

    def __init__(self, host:str, port:int, buffer_size:int, delay:int, token:str, chat_id:str) -> None:
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.delay = delay
        self.token = token
        self.chat_id = chat_id
        self.start_time = time.time()
        self.start_proses = True
        self.database = Database()
        self.request_time = 5
        self.chart_time = 300
        Loggers()
        super().__init__()
        
    def InsertLog(self, status:str) -> None:
        self.database.insert(
            fields=["status", "timestamp"],
            data={
                "status": status,
                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        )

    def GetLog(self) -> list:
        interval = self.chart_time / 60
        data, message = self.database.select(self.database.query_log(interval))
        if message:
            logging.error(message)
        return data
        
    def Check(self) -> None:
        logging.info("Checking server...")
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((self.host, self.port))
            self.InsertLog("Connected")

            to_server = {
                "message": F"From client at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            }
            
            to_server = str(to_server).encode("utf-8")
            data_format = struct.Struct('I')
            data_length = len(to_server)
            s.sendall(data_format.pack(data_length))

            offset = 0
            while offset < data_length:
                sent_bytes = s.send(to_server[offset:])
                offset += sent_bytes

            response = s.recv(self.buffer_size)
            response = eval(response)

            if response:
                logging.info(F"From server: {response['message']}")
                self.InsertLog("Success Received")
            else:
                self.InsertLog("Failed Received")

        except socket.timeout:
            self.InsertLog("TimeoutError")
        except ConnectionRefusedError:
            self.InsertLog("ConnectionRefusedError")
        except BrokenPipeError:
            self.InsertLog("BrokenPipeError")
        except ConnectionResetError:
            self.InsertLog("ConnectionResetError")
        except SyntaxError:
            self.InsertLog("SyntaxError")
            
        s.close()
        return None
    
    def CreateChart(self) -> None:
        data = self.GetLog()
        labels = [data['status'] for data in data]
        values = [data['total'] for data in data]

        color = []
        for label in labels:
            if label == "Connected":
                color.append("green")
            elif label == "Success Received":
                color.append("blue")
            else:
                color.append("red")

        time_label = int(self.chart_time / 60)

        _,ax = plt.subplots(figsize=(16,4))
        ax.bar(labels, values, color=color)
        ax.set_title(f'Server - Connection Status in {time_label} Minutes {self.request_time}s/req')
        ax.set_xlabel('Status Connection')
        ax.set_ylabel(f'Total in {time_label} minutes')
        
        for i, v in enumerate(values):
            ax.text(i, v/2, str(v), color='white', fontweight='bold', ha='center', va='center', fontsize=12)

        filename = F"chart-{datetime.now().strftime('%Y-%m-%d-%H-%M')}.png"
    
        plt.savefig(F"static/{filename}")
        plt.close()

        url = F"https://api.telegram.org/bot{self.token}/sendPhoto?chat_id={self.chat_id}"
        response = requests.post(url, files={"photo": open(F"static/{filename}", "rb")})
        if response.ok:
            os.remove(F"static/{filename}")
            logging.info("Send chart to telegram")

        return None

    def StartClient(self) -> None:
        while self.start_proses:
            try:
                self.Check()
                time.sleep(self.request_time)
                if time.time() - self.start_time > self.chart_time:
                    self.CreateChart()
                    self.start_time = time.time()
            except KeyboardInterrupt:
                self.start_proses = False
                logging.info("Close client")
                break

if __name__ == "__main__":
    client = Client(
        host=Config.SOCKET_NOTIFICATIONS["HOST_CLIENT"],
        port=Config.SOCKET_NOTIFICATIONS["PORT"],
        buffer_size=Config.SOCKET_NOTIFICATIONS["BUFFER_SIZE"],
        delay=Config.SOCKET_NOTIFICATIONS["DELAY_CLIENT"],
        token=Config.OPS["TELE_TOKEN"],
        chat_id=Config.OPS["TELE_CHAT_ID"]
    )
    client.StartClient()