import os
import logging
import multiprocessing as mp
from libs.Loggers import Loggers
from settings.Config import Config
from libs.VideoProsessor import VideoProsessor

class FormatterVideo:

    def __init__(self, environment:str, upload_location:str, extension:str) -> None:
        self.environment = environment
        self.upload_location = upload_location
        self.extension = extension
        self.video_prosessor = VideoProsessor(environment=self.environment, storage_path=self.upload_location)
        Loggers()
        super().__init__()

    def GetAllFiles(self) -> list:
        path = F"{os.getcwd()}/{self.upload_location}"
        
        files = []

        for file in os.listdir(path):
            if file.endswith(self.extension):
                files.append({
                    "path": F"{path}",
                    "filename": file.split(".")[0],
                    "extension": self.extension
                })

        return files

    def Run(self):
        files = self.GetAllFiles()
        pool = mp.Pool(mp.cpu_count())
        pool.starmap(self.video_prosessor.OptimizeVideo, [(file["path"], file["filename"], file["extension"]) for file in files])
        pool.close()
        pool.join()

        logging.info("Success Formatter Video")

if __name__ == '__main__':
    ENGINE_NAME = "IDXSTREAMING"
    CONFIG = Config()
    ENGINE = CONFIG.ENGINE[ENGINE_NAME]
    f = FormatterVideo(
        environment=ENGINE["ENVIRONMENT"],
        upload_location=ENGINE["UPLOAD_LOCATION"],
        extension=".mp4"
    )
    f.Run()