import os
import re
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

    def OptimizeVideo(self, path: str, filename: str, extension: str = ".mp4"):
        try:
            convert_name = "_converted"
            os.system(F"ffmpeg -i {path}/{filename}{extension} -c:v libx264 -c:a aac -strict experimental -b:a 98k -ar 44100 -movflags faststart -f mp4 {path}/{filename.split('.')[0]}{convert_name}{extension}")
            os.remove(F"{path}/{filename}{extension}")
            os.rename(F"{path}/{filename}{convert_name}{extension}", F"{path}/{filename}{extension}")
            logging.info("Successfully Optimized Video")
        except Exception as e:
            logging.error(F"Error Optimize Video: {e}")

    def WriteFile(self, file_name:str, content, mode:str, folder:str) -> dict:
        try:
            if self.environment == "dev":
                path = F"{os.getcwd()}/{self.storage_path}/{folder}"
            else:
                path = F"{self.storage_path}/{folder}"

            if not os.path.exists(path):
                # oldmask = os.umask(000)
                os.makedirs(path)
                # os.umask(oldmask)
            
            with open(F"{path}/{file_name}", mode) as file:
                file.write(content)
                file.close()
            logging.info(F"Success Write File: {file_name}")
            return {
                "status": True,
                "message": F"Success Write File: {file_name}",
                "sequence": file_name.split(".")[0]
            }
        except Exception as e:
            logging.error(F"Error Write File: {e}")
            return {
                "status": False,
                "message": F"Error Write File: {e}",
                "sequence": None
            }


    def CompressVideo(self, filename: str):
        if self.environment == "dev":
            cwd = os.getcwd()
            path_ts = F"{cwd}/{self.storage_path}/ts"
            path_mp4 = F"{cwd}/{self.storage_path}"
        else:
            path_ts = F"{self.storage_path}/ts"
            path_mp4 = F"{self.storage_path}"
        input_path =F"{path_mp4}/{filename}.mp4"
        try:
            temp_output_path = F"{input_path}.temp.mp4"
            scale_option = "-vf scale=854:480"
            crf_value = 30 
            os.system(F"ffmpeg -i {input_path} -vcodec libx264 -crf {crf_value} {scale_option} -b:a 64k {temp_output_path}")

            os.remove(input_path)
            os.rename(temp_output_path, input_path)
            logging.info("Successfully Compressed MP4")
        except Exception as e:
            logging.error(F"Error Compressing MP4: {e}")

    def ConcatTS(self, filename: str, mode: str, optimize_video: bool = True, compress_video: bool = True) -> dict:
        try:
            ts_files = list()
            if self.environment == "dev":
                cwd = os.getcwd()
                path_ts = F"{cwd}/{self.storage_path}/ts"
                path_mp4 = F"{cwd}/{self.storage_path}"
            else:
                path_ts = F"{self.storage_path}/ts"
                path_mp4 = F"{self.storage_path}"

            if not os.path.exists(path_mp4):
                os.makedirs(path_mp4)

            for file in os.listdir(path_ts):
                if file.endswith(".ts"):
                    ts_files.append(F"{path_ts}/{file}")

            ts_files.sort()
            with open(F"{path_ts}/{filename}.txt", mode) as file:
                for ts in ts_files:
                    file.write(F"file '{ts}'\n")

            os.system(F"ffmpeg -f concat -safe 0 -i {path_ts}/{filename}.txt -c copy {path_mp4}/{filename}.mp4")
            logging.info("Success Concat TS to MP4")

            # self.OptimizeVideo(path_mp4, filename)
            # logging.info("Success Optimize Video")

            # self.CompressVideo(F"{path_mp4}/{filename}.mp4")
            logging.info("Success Compress MP4")

            return {
                "status": True,
                "message": "Success Concat TS to MP4",
                "path": F"{path_mp4}/{filename}.mp4"
            }

        except Exception as e:
            logging.error(F"Error Concat TS to MP4: {e}")
            return {
                "status": False,
                "message": F"Error Concat TS to MP4: {e}",
                "path": None
            }
    
    def CleanUPTSFolder(self, list_ts:list = [], metadata:str = None) -> None:
        try:
            if self.environment == "dev":
                path_ts = F"{os.getcwd()}/{self.storage_path}/ts"
            else:
                path_ts = F"{self.storage_path}/ts"
            
            for file in os.listdir(path_ts):
                if len(list_ts) > 0:
                    if file in list_ts or file == F"{metadata}.txt":
                        os.remove(F"{path_ts}/{file}")
                else:
                    if file.endswith(".txt") or file.endswith(".ts") : os.remove(F"{path_ts}/{file}")
                
            logging.info("Success Cleanup TS")
        except Exception as e:
            logging.error(F"Error Cleanup TS: {e}")

    
    def GetTotalFiles(self, folder:str, last_ts:str) -> int:
        try:
            if self.environment == "dev":
                path = F"{os.getcwd()}/{self.storage_path}/{folder}"
            else:
                path = F"{self.storage_path}/{folder}"
            
            #calculate total files in folder with last file ts
            files = sorted(os.listdir(path))
            files.sort(key=lambda x: int(re.sub('\D', '', x)))
            total_files = 0
            for file in files:
                if file.endswith(".ts"):
                    total_files += 1
                    if file == last_ts:
                        break
            logging.info(F"Total Files: {total_files}")
            return total_files
        except Exception as e:
            logging.error(F"Error Get Total Files: {e}")
            return 0
        
    def ListFiles(self, folder:str, last_ts:str) -> list:
        try:
            if self.environment == "dev":
                path = F"{os.getcwd()}/{self.storage_path}/{folder}"
            else:
                path = F"{self.storage_path}/{folder}"
            
            files = sorted(os.listdir(path))
            files.sort(key=lambda x: int(re.sub('\D', '', x)))
            files_list = list()
            for file in files:
                if file.endswith(".ts"):
                    files_list.append(file)
                    if file == last_ts:
                        break
            return files
        except Exception as e:
            logging.error(F"Error List Files: {e}")
            return []


    