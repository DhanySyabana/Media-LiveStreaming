import os
import re
import logging


class VideoProsessor:

    def __init__(
        self,
        environment: str,
        storage_path: str = None,
    ) -> None:

        self.environment = environment

        # normalize storage path
        if os.path.isabs(storage_path):
            self.storage_path = os.path.normpath(storage_path)
        else:
            self.storage_path = os.path.normpath(
                os.path.join(os.getcwd(), storage_path)
            )

        logging.info(f"Storage Path: {self.storage_path}")

        super().__init__()

    def OptimizeVideo(self, path, filename, extension=".mp4"):
        try:

            convert_name = "_converted"

            input_file = os.path.join(
                path,
                f"{filename}{extension}"
            )

            output_temp = os.path.join(
                path,
                f"{filename.split('.')[0]}{convert_name}{extension}"
            )

            output_final = os.path.join(
                path,
                f"{filename}{extension}"
            )

            command = (
                f'ffmpeg -i "{input_file}" '
                f'-c:v libx264 '
                f'-c:a aac '
                f'-strict experimental '
                f'-b:a 98k '
                f'-ar 44100 '
                f'-movflags faststart '
                f'-f mp4 "{output_temp}"'
            )

            os.system(command)

            if os.path.exists(input_file):
                os.remove(input_file)

            if os.path.exists(output_temp):
                os.rename(output_temp, output_final)

            logging.info("Success Optimize Video")

        except Exception as e:
            logging.error(f"Error Optimize Video: {e}")

    def WriteFile(self, file_name: str, content, mode: str, folder: str) -> dict:

        try:

            path = os.path.normpath(
                os.path.join(self.storage_path, folder)
            )

            if not os.path.exists(path):
                os.makedirs(path)

            temp_file = os.path.join(
                path,
                f"{file_name}.part"
            )

            final_file = os.path.join(
                path,
                file_name
            )

            with open(temp_file, mode) as file:
                file.write(content)

            # atomic replace
            os.replace(temp_file, final_file)

            logging.info(f"Success Write File: {file_name}")

            return {
                "status": True,
                "message": f"Success Write File: {file_name}",
                "sequence": file_name.split(".")[0]
            }

        except Exception as e:

            logging.error(f"Error Write File: {e}")

            return {
                "status": False,
                "message": f"Error Write File: {e}",
                "sequence": None
            }

    def ConcatTS(self, filename: str, mode: str, optimize_video: bool = False) -> dict:

        try:

            ts_files = []

            path_ts = os.path.normpath(
                os.path.join(self.storage_path, "ts")
            )

            path_mp4 = os.path.normpath(self.storage_path)

            if not os.path.exists(path_mp4):
                os.makedirs(path_mp4)

            if not os.path.exists(path_ts):
                return {
                    "status": False,
                    "message": "TS folder not found",
                    "path": None
                }

            for file in os.listdir(path_ts):

                if file.endswith(".ts"):

                    ts_files.append(
                        os.path.join(path_ts, file)
                    )

            ts_files.sort()

            txt_file = os.path.join(
                path_ts,
                f"{filename}.txt"
            )

            with open(txt_file, mode) as file:

                for ts in ts_files:
                    file.write(f"file '{ts}'\n")

            output_mp4 = os.path.join(
                path_mp4,
                f"{filename}.mp4"
            )

            command = (
                f'ffmpeg -f concat '
                f'-safe 0 '
                f'-i "{txt_file}" '
                f'-c copy '
                f'"{output_mp4}"'
            )

            os.system(command)

            logging.info("Success Concat TS to MP4")

            if optimize_video:

                self.OptimizeVideo(
                    path_mp4,
                    filename
                )

            return {
                "status": True,
                "message": "Success Concat TS to MP4",
                "path": output_mp4
            }

        except Exception as e:

            logging.error(f"Error Concat TS to MP4: {e}")

            return {
                "status": False,
                "message": f"Error Concat TS to MP4: {e}",
                "path": None
            }

    def CleanUPTSFolder(
        self,
        list_ts: list = [],
        metadata: str = None
    ) -> None:

        try:

            path_ts = os.path.normpath(
                os.path.join(self.storage_path, "ts")
            )

            if not os.path.exists(path_ts):
                logging.warning(f"TS Folder Not Found: {path_ts}")
                return

            for file in os.listdir(path_ts):

                file_path = os.path.join(
                    path_ts,
                    file
                )

                if len(list_ts) > 0:

                    if file in list_ts or file == f"{metadata}.txt":

                        if os.path.exists(file_path):
                            os.remove(file_path)

                else:

                    if file.endswith(".txt") or file.endswith(".ts"):

                        if os.path.exists(file_path):
                            os.remove(file_path)

            logging.info("Success Cleanup TS")

        except Exception as e:
            logging.error(f"Error Cleanup TS: {e}")

    def GetTotalFiles(
        self,
        folder: str,
        last_ts: str
    ) -> int:

        try:

            path = os.path.normpath(
                os.path.join(self.storage_path, folder)
            )

            if not os.path.exists(path):
                return 0

            files = sorted(os.listdir(path))

            files.sort(
                key=lambda x: int(re.sub(r'\D', '', x) or 0)
            )

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

    def ListFiles(
        self,
        folder: str,
        last_ts: str
    ) -> list:

        try:

            path = os.path.normpath(
                os.path.join(self.storage_path, folder)
            )

            if not os.path.exists(path):
                return []

            files = sorted(os.listdir(path))

            files.sort(
                key=lambda x: int(re.sub(r'\D', '', x) or 0)
            )

            files_list = []

            for file in files:

                if file.endswith(".ts"):

                    files_list.append(file)

                    if file == last_ts:
                        break

            return files_list

        except Exception as e:

            logging.error(f"Error List Files: {e}")

            return []