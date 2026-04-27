import socket
import struct
import logging
import requests
from libs.Loggers import Loggers
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessorBeritasatu import VideoProsessor

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
        s.listen()

        logging.info("Server is Running...")
        try:
            while True:
                conn, addr = s.accept()
                with conn:
                    logging.info(F"Connected by {addr}")
                    while True:
                        data_format = struct.Struct('I')
                        data_length = conn.recv(data_format.size)

                        if not data_length:
                            break
                        logging.info(F"Received request convert video from {addr}")

                        
                        data_length = data_format.unpack(data_length)[0]

                        data = bytearray()
                        while len(data) < data_length:
                            chunk = conn.recv(self.buffer_size)
                            if not chunk:
                                break
                            data += chunk

                        data = data.decode("utf-8")
                        data = eval(data)

                        response = None

                        video_prosessor = VideoProsessor(
                            environment=data["environment"],
                            storage_path=data["storage_path"],
                        )

                        if data["event"] == "concat":
                            optimize_video = False

                            if "optimize_video" in data:    
                                optimize_video = data["optimize_video"]

                            response = video_prosessor.ConcatTS(
                                filename=data["filename"],
                                mode=data["mode"],
                                optimize_video=optimize_video
                            )
                        elif data["event"] == "download":
                            response = {
                                "sequence": None,
                                "message": None,
                            }

                            segments = data["segments"]

                            for segment in segments:
                                
                                try:
                                    response_http = HTTPRequest(data["method"], segment["url"], data["headers"]).Hit()
                                    #response_http = requests.get(url= segment["url"], headers=data["headers"], verify=False)
                                    logging.info(F"Status Request Segment: {response_http.status_code}")
                                    if response_http.status_code == 200:
                                        file_name = F"{segment['sequence']}.ts"
                                        
                                        write_file = video_prosessor.WriteFile(
                                            file_name=file_name,
                                            content=response_http.content,
                                            mode="wb",
                                            folder="ts"
                                        )
                                        response["sequence"] = write_file["sequence"]
                                        response["message"] = write_file["message"]
                                        logging.info(F"Success Download Segment: {file_name}")
                                    else:
                                        logging.error(F"Error Download Segment: {response_http.status_code}")
                                        continue
                                    logging.info(F"Succes Download Segment")
                                except AttributeError:
                                    logging.error(F"Error Download Segment: {segment['url']}")
                                    continue
                                    
                        else:
                            logging.error(F"Error Event: {data['event']}")
                        
                        response = bytes(str(response), "utf-8")
                        conn.sendall(response)

        except KeyboardInterrupt:
            logging.info("Closing Server Connection...")
            logging.info("Server Closed")
            s.close()

if __name__ == "__main__":
    CONFIG_SERVER = Config().SOCKET_SERVER_BERITASATU
    server_converter = ServerConverter(
        host=CONFIG_SERVER["HOST"],
        port=CONFIG_SERVER["PORT"],
        max_connection=CONFIG_SERVER["MAX_CONNECTION"],
        buffer_size=CONFIG_SERVER["BUFFER_SIZE"]
    )
    server_converter.Start()

