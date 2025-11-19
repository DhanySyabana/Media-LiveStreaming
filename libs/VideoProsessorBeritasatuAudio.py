import os
import re
import logging

class VideoProsessor:

    def __init__(self, environment: str, storage_path: str = None) -> None:
        self.environment: str = environment
        self.storage_path: str = storage_path
        super().__init__()

    def OptimizeVideo(self, path, filename, extension=".mp3"):
        try:
            convert_name = "_converted"
            os.system(
                f'ffmpeg -i "{path}/{filename}{extension}" -c:v libx264 -c:a aac -b:a 98k -ar 44100 '
                f'-movflags faststart -f mp4 "{path}/{filename.split(".")[0]}{convert_name}{extension}"'
            )
            os.remove(f"{path}/{filename}{extension}")
            os.rename(
                f"{path}/{filename}{convert_name}{extension}",
                f"{path}/{filename}{extension}"
            )
        except Exception as e:
            logging.error(f"Error Optimize Video: {e}")

    def WriteFile(self, file_name: str, content, mode: str, folder: str) -> dict:
        try:
            if self.environment == "dev":
                path = f"{os.getcwd()}/{self.storage_path}/{folder}"
            else:
                path = f"{self.storage_path}/{folder}"

            if not os.path.exists(path):
                os.makedirs(path)
            
            with open(f"{path}/{file_name}", mode) as file:
                file.write(content)
            logging.info(f"Success Write File: {file_name}")
            return {"status": True, "message": f"Success Write File: {file_name}", "sequence": file_name.split(".")[0]}
        except Exception as e:
            logging.error(f"Error Write File: {e}")
            return {"status": False, "message": f"Error Write File: {e}", "sequence": None}

    def ConcatTS(self, filename:str, mode:str, optimize_video:bool = False) -> dict:
        try:
            ts_files = list()
            if self.environment == "dev":
                cwd = os.getcwd()
                path_ts = f"{cwd}/{self.storage_path}/audio" if "audio" in self.storage_path or "audio" in filename.lower() else f"{cwd}/{self.storage_path}/video"
                path_mp4 = f"{cwd}/{self.storage_path}/ts"
            else:
                path_ts = f"{self.storage_path}/audio" if "audio" in self.storage_path or "audio" in filename.lower() else f"{self.storage_path}/video"
                path_mp4 = f"{self.storage_path}/ts"

            if not os.path.exists(path_mp4):
                os.makedirs(path_mp4)

            # ambil semua ts
            for file in os.listdir(path_ts):
                if file.endswith(".ts"):
                    ts_files.append(os.path.join(path_ts, file))

            ts_files.sort()

            # buat daftar file .txt (ffmpeg concat list)
            txt_path = os.path.join(path_ts, f"{filename}.txt")
            with open(txt_path, mode) as file:
                for ts in ts_files:
                    # convert path → absolute + forward slash agar aman di ffmpeg
                    ts_path = os.path.abspath(ts).replace("\\", "/")
                    file.write(f"file '{ts_path}'\n")

            # tentukan output
            if "audio" in path_ts:
                output_path = f"{path_mp4}/{filename}.mp3"
                cmd = f'ffmpeg -f concat -safe 0 -i "{txt_path}" -codec:a libmp3lame -q:a 2 "{output_path}"'
            else:
                output_path = f"{path_mp4}/{filename}.mp4"
                cmd = f'ffmpeg -f concat -safe 0 -i "{txt_path}" -c copy "{output_path}"'

            # jalanin ffmpeg
            os.system(cmd)
            logging.info(f"Success Concat TS → {output_path}")

            # optional: optimize
            if optimize_video and output_path.endswith(".mp4"):
                self.OptimizeVideo(path_mp4, filename)
                logging.info("Success Optimize Video")

            return {
                "status": True,
                "message": f"Success Concat TS → {output_path}",
                "path": output_path
            }

        except Exception as e:
            logging.error(f"Error Concat TS: {e}")
            return {
                "status": False,
                "message": f"Error Concat TS: {e}",
                "path": None
            }


    def CleanUPTSFolder(self):
        try:
            if self.environment == "dev":
                path_ts = f"{os.getcwd()}/{self.storage_path}/ts"
            else:
                path_ts = f"{self.storage_path}/ts"
            
            if not os.path.exists(path_ts):
                return
            for file in os.listdir(path_ts):
                if file.endswith(".txt") or file.endswith(".ts"):
                    os.remove(f"{path_ts}/{file}")
            logging.info("Success Cleanup TS")
        except Exception as e:
            logging.error(f"Error Cleanup TS: {e}")

    def GetTotalFiles(self, folder: str, last_ts: str) -> int:
        try:
            if self.environment == "dev":
                path = f"{os.getcwd()}/{self.storage_path}/{folder}"
            else:
                path = f"{self.storage_path}/{folder}"

            files = sorted(os.listdir(path))
            files.sort(key=lambda x: int(re.sub(r'\D', '', x)))
            total_files = 0
            for file in files:
                if file.endswith(".ts"):
                    total_files += 1
                    if file == last_ts:
                        break
            logging.info(f"Total Files: {total_files}")
            return total_files
        except Exception as e:
            logging.error(f"Error Get Total Files: {e}")
            return 0
