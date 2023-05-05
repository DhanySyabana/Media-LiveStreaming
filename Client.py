import time
import socket
import struct
import logging
from datetime import datetime
from libs.Loggers import Loggers
from libs.HTTPRequest import HTTPRequest
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
        Loggers()
        super().__init__()

    def SendMessage(self) -> int:
        try:
            message = F"<b>Server is died at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</b>"
            url = F"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={message}&parse_mode=html"
            response = HTTPRequest("get", url, headers=None).Hit()
            return response.ok
        except Exception as e:
            logging.error(F"Error send message: {e}")
            return 0
        
    def Check(self) -> bool:
        logging.info("Checking server...")
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.delay)
            s.connect((self.host, self.port))
        except Exception:
            return False

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
        else:
            return False
        
        s.close()

        return True

    def StartClient(self) -> None:
        while self.start_proses:
            try:
                if not self.Check():
                    logging.info("Server is died")
                    if self.SendMessage():
                        logging.info("Send message to telegram")
                    else:
                        logging.info("Failed send message to telegram")
                    continue
                time.sleep(self.delay)
            except TimeoutError:
                if self.SendMessage():
                    logging.info("Send message to telegram")
                time.sleep(self.delay)
                continue
            except KeyboardInterrupt:
                logging.info("Close client")
                self.start_proses = False
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