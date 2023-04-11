import socket
import logging
from libs.Loggers import Loggers
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessor import VideoProsessor
from settings.TypeDataConverter import TypeDataConverter

class ServerConverter:

    def __init__(self, host:str, port:int, max_connection:int, buffer_size:int) -> None:
        Loggers()
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.max_connection = max_connection
        super().__init__()

    def Start(self) -> None:
        logging.info("Starting Server...")
        logging.info(F"Server Host: {self.host}")
        logging.info(F"Server Port: {self.port}")
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(self.max_connection)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        logging.info("Server is Running...")
        try:
            while True:
                conn, addr = s.accept()
                with conn:
                    logging.info(F"Connected by {addr}")
                    while True:
                        data = conn.recv(self.buffer_size)

                        if not data:
                            break
                        logging.info(F"Received request convert video from {addr}")
                        
                        data = TypeDataConverter(data).binary_to_dict()

                        response = None

                        video_prosessor = VideoProsessor(
                            environment=data["environment"],
                            storage_path=data["storage_path"]
                        )

                        if data["event"] == "concat":
                            response = video_prosessor.ConcatTS(
                                filename=data["filename"],
                                mode=data["mode"],
                            )
                        elif data["event"] == "download":
                            response_http = HTTPRequest(data["method"], data["url"], data["headers"]).Hit()
                            if response_http.status_code == 200:
                                file_name = F"{data['sequence']}.ts"
                                
                                response = video_prosessor.WriteFile(
                                    file_name=file_name,
                                    content=response_http.content,
                                    mode="wb",
                                    folder="ts"
                                )
                                logging.info(F"Success Download Segment: {file_name}")
                            else:
                                logging.error(F"Error Download Segment: {response_http.status_code}")
                            logging.info(F"Succes Download Segment")
                        else:
                            logging.error(F"Error Event: {data['event']}")
                        
                        response = bytes(str(response), "utf-8")
                        conn.sendall(response)

        except KeyboardInterrupt:
            logging.info("Closing Server Connection...")
            logging.info("Server Closed")
            s.close()

if __name__ == "__main__":
    CONFIG_SERVER = Config().SOCKET_SERVER
    server_converter = ServerConverter(
        host=CONFIG_SERVER["HOST"],
        port=CONFIG_SERVER["PORT"],
        max_connection=CONFIG_SERVER["MAX_CONNECTION"],
        buffer_size=CONFIG_SERVER["BUFFER_SIZE"]
    )
    server_converter.Start()
