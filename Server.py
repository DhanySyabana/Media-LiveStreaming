import socket
import struct
import logging
from datetime import datetime
from libs.Loggers import Loggers
from settings.Config import Config

class Server:

    def __init__(self, host:str, port:int, buffer_size:int) -> None:
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        Loggers()
        super().__init__()

    def StartServer(self) -> None:
        logging.info("Starting Server notifications...")
        logging.info(F"Server Host: {self.host}")
        logging.info(F"Server Port: {self.port}")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen()

        logging.info("Server is Running...")
        try:
            while True:
                conn, addr = s.accept()
                logging.info(F"Connected by {addr}")
                while True:
                    data_format = struct.Struct('I')
                    data_length = conn.recv(data_format.size)

                    if not data_length:
                        break
                    logging.info(F"Received request from {addr}")

                    
                    data_length = data_format.unpack(data_length)[0]

                    data = bytearray()
                    while len(data) < data_length:
                        chunk = conn.recv(self.buffer_size)
                        if not chunk:
                            break
                        data += chunk

                    data = data.decode("utf-8")
                    data = eval(data)

                    if isinstance(data, dict):
                        logging.info(data['message'])

                    response = {
                        "message": "OK",
                        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }

                    response = bytes(str(response), "utf-8")
                    conn.sendall(response)
        except KeyboardInterrupt:
            logging.info("Closing Server Connection...")
            logging.info("Server Closed")
            s.close()

    
if __name__ == "__main__":
    server = Server(
        host=Config.SOCKET_NOTIFICATIONS["HOST_SERVER"],
        port=Config.SOCKET_NOTIFICATIONS["PORT"],
        buffer_size=Config.SOCKET_NOTIFICATIONS["BUFFER_SIZE"]
    )
    server.StartServer()