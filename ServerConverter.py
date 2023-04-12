import struct
import logging
import asyncio
from libs.Loggers import Loggers
from settings.Config import Config
from libs.HTTPRequest import HTTPRequest
from libs.VideoProsessor import VideoProsessor

class ServerConverter:

    def __init__(self, host:str, port:int, max_connection:int, buffer_size:int) -> None:
        Loggers()
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.max_connection = max_connection
        self.server = None
        super().__init__()

    async def start(self):
        logging.info("Starting Server...")
        logging.info(F"Server Host: {self.host}")
        logging.info(F"Server Port: {self.port}")

        self.server = await asyncio.start_server(
            self.handle_client, self.host, self.port
        )

        async with self.server:
            await self.server.serve_forever()

    async def handle_client(self, client_reader, client_writer):
        try:
            while True:
                data_format = struct.Struct('I')
                data_length = await client_reader.read(data_format.size)

                if not data_length:
                    break
                logging.info(F"Received request convert video from {client_writer.get_extra_info('peername')}")

                data_length = data_format.unpack(data_length)[0]

                data = bytearray()
                while len(data) < data_length:
                    chunk = await client_reader.read(data_length - len(data))
                    if not chunk:
                        break
                    data += chunk
                
                data = data.decode("utf-8")
                data = eval(data)

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
                client_writer.write(response)

        except ConnectionResetError:
            pass

        finally:
            logging.info(F"Connection closed from {client_writer.get_extra_info('peername')}")
            client_writer.close()

async def main():
    CONFIG_SERVER = Config().SOCKET_SERVER
    server = ServerConverter(
        host=CONFIG_SERVER["HOST"],
        port=CONFIG_SERVER["PORT"],
        max_connection=CONFIG_SERVER["MAX_CONNECTION"],
        buffer_size=CONFIG_SERVER["BUFFER_SIZE"]
    )
    await server.start()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Server Stopped")
        pass
