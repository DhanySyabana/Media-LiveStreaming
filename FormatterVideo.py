import os
import logging
import multiprocessing as mp
from libs.Loggers import Loggers
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
        files = []

        for file in os.listdir(self.upload_location):
            if file.endswith(self.extension):
                files.append({
                    "path": F"{self.upload_location}",
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
    f = FormatterVideo(
        environment="dev",
        upload_location="/home/kabayangroup/www/produksi-tv/public/video_list/IDXSTREAMING",
        extension=".mp4"
    )
    f.Run()
