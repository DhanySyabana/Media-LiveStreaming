import os
import logging

class VideoProsessor:

    def __init__(
            self,
            environment:str,
            storage_path:str = None,
        ) -> None:
        self.environment:str = environment
        self.storage_path:str = storage_path
        super().__init__()

    def WriteFile(self, file_name:str, content, mode:str, folder:str) -> None:
        try:
            path = F"{self.storage_path}/{folder}"
            if not os.path.exists(path):
                os.makedirs(path)
            
            with open(F"{path}/{file_name}", mode) as file:
                file.write(content)
            logging.info(F"Success Write File: {file_name}")
        except Exception as e:
            logging.error(F"Error Write File: {e}")

    def ConcatTS(self, filename:str, mode:str) -> None:
        try:
            ts_files = list()
            if self.environment == "dev":
                cwd = os.getcwd()
                path_ts = F"{cwd}/{self.storage_path}/ts"
                path_mp4 = F"{cwd}/{self.storage_path}/mp4"
            else:
                path_ts = F"{self.storage_path}/ts"
                path_mp4 = F"{self.storage_path}"

            if not os.path.exists(path_mp4):
                os.makedirs(path_mp4)

            for file in os.listdir(path_ts):
                if file.endswith(".ts"):
                    ts_files.append(F"{path_ts}/{file}")

            ts_files.sort()
            with open(F"{path_ts}/merged.txt", mode) as file:
                for ts in ts_files:
                    file.write(F"file '{ts}'\n")

            os.system(F"ffmpeg -f concat -safe 0 -i {path_ts}/merged.txt -c copy {path_mp4}/{filename}.mp4")
            logging.info("Success Concate TS to MP4")
        except Exception as e:
            logging.error(F"Error Concate TS to MP4: {e}")


    def CleanUPTSFolder(self) -> None:
        try:
            if self.environment == "dev":
                cwd = os.getcwd()
                path_ts = F"{cwd}/{self.storage_path}/ts"
            else:
                path_ts = F"{self.storage_path}/ts"
            
            for file in os.listdir(path_ts):
                if file.endswith(".ts") or file.endswith(".txt"):
                    os.remove(F"{path_ts}/{file}")
            logging.info("Success Cleanup TS")
        except Exception as e:
            logging.error(F"Error Cleanup TS: {e}")


    