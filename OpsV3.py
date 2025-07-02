import os
import subprocess
import docker
import sys
import glob
import time
import tqdm
import math
import logging
import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime
from libs.Loggers import Loggers
from settings.Config import Config
from matplotlib.gridspec import GridSpec

class Ops:

    def __init__(self, TOKEN:str, CHAT_ID:str, delay_proses:int, storage_path_mp4:dict) -> None:
        self.TOKEN:str= TOKEN
        self.CHAT_ID:str = CHAT_ID
        self.start_time = 0
        self.start_proses = True
        self.delay_proses:int = delay_proses
        self.storage_path_mp4:dict = storage_path_mp4
        Loggers()
        super().__init__()
    
    def get_file_data(self) -> dict:
        data = {}
        for key, value in self.storage_path_mp4.items():
            total_video = len([name for name in os.listdir(value) if name.endswith(".mp4")])
            if math.isnan(total_video):
                total_video = 0
            else:
                total_video = int(total_video)

            # total video last 60 minutes
            total_video_last_hour = len([name for name in os.listdir(value) if name.endswith(".mp4") and (time.time() - os.path.getmtime(F"{value}/{name}")) < 3600])
            if math.isnan(total_video_last_hour):
                total_video_last_hour = 0
            else:
                total_video_last_hour = int(total_video_last_hour)
            # # total video last 90 minutes
            # total_video_last_hour_idx = len([name for name in os.listdir(value) if name.endswith(".mp4") and (time.time() - os.path.getmtime(F"{value}/{name}")) < 5400])
            # if math.isnan(total_video_last_hour_idx):
            #     total_video_last_hour_idx = 0
            # else:
            #     total_video_last_hour_idx = int(total_video_last_hour_idx)

            total_size = sum(os.path.getsize(F"{value}/{name}") for name in os.listdir(value) if name.endswith(".mp4")) / 1024 / 1024
            if math.isnan(total_size):
                total_size = 0
            else:
                total_size = int(total_size)

            data[key] = {
                "total_video": total_video,
                "total_size": total_size,
                # "total_video_last_hour_idx": total_video_last_hour_idx,
                "total_video_last_hour": total_video_last_hour,
                "last_video_filename": "-",
            }

            if total_video_last_hour > 0:
                data[key]["last_video_filename"] = max(glob.iglob(F"{value}/*.mp4"), key=os.path.getctime).split("/")[-1]

        return data
    
    def generate_send_chart(self, data:dict) -> None:
        key_data = list(data.keys())
        no = 0
        for key, channel in enumerate(key_data):
            if data[key_data[key]]["total_video_last_hour"] < 2:
                if channel == "INEWSSTREAMING":
                    containers_to_restart = ["engine_server_converter_inews", "engine_inews_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "TVONESTREAMING":
                    logging.info(F"Start : {str(channel)}")
                    # # nama container yang mau di restart
                    containers_to_restart = ["engine_server_converter_tvone", "engine_tvone_v1"]

                    for name_containers in containers_to_restart:
                         try:
                             # Membuat koneksi dengan Docker daemon
                             # Menentukan URL Docker API
                             docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                             # Membuat objek klien Docker dengan URL yang ditentukan
                             client = docker.DockerClient(base_url=docker_api_url)

                             # Mengambil objek container berdasarkan nama atau ID
                             container = client.containers.get(name_containers)

                             # Memulai ulang (restart) container
                             container.restart()

                             logging.info(f"Container '{name_containers}' berhasil di-restart.")
                         except docker.errors.NotFound as e:
                             logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                             continue
                         except docker.errors.APIError as e:
                             logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                             continue
                         except Exception as e:
                             logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                             continue
                elif channel == "BERITASATUSTREAMING":
                    # nama container yang mau di restart
                    containers_to_restart = ["engine_server_converter_beritasatu", "engine_beritasatu_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "TVRISTREAMING":
                    # nama container yang mau di restart
                    containers_to_restart = ["engine_server_converter_v1", "engine_tvri_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "RCTISTREAMING":
                    containers_to_restart = ["engine_server_converter_rcti","engine_rcti_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "TRANS7STREAMING":
                    containers_to_restart = ["engine_server_converter_trans", "engine_trans7_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "TRANSTVSTREAMING":
                    containers_to_restart = ["engine_server_converter_transtv", "engine_transtv_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "NUSANTARATVSTREAMING":
                    containers_to_restart = ["engine_server_converter_nusantara", "engine_nusantara_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "MNCSTREAMING":
                    containers_to_restart = ["engine_server_converter_mnc", "engine_mnc_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                # elif channel == "SEATODAYSTREAMING":
                #     containers_to_restart = ["engine_server_converter_seatoday", "engine_seatoday_v1"]

                #     for name_containers in containers_to_restart:
                #         try:
                #             # Membuat koneksi dengan Docker daemon
                #             # Menentukan URL Docker API
                #             docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                #             # Membuat objek klien Docker dengan URL yang ditentukan
                #             client = docker.DockerClient(base_url=docker_api_url)

                #             # Mengambil objek container berdasarkan nama atau ID
                #             container = client.containers.get(name_containers)

                #             # Memulai ulang (restart) container
                #             container.restart()

                #             logging.info(f"Container '{name_containers}' berhasil di-restart.")
                #         except docker.errors.NotFound as e:
                #             logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                #             continue
                #         except docker.errors.APIError as e:
                #             logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                #             continue
                #         except Exception as e:
                #             logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                #             continue
                
            
            if data[key_data[key]]["total_video_last_hour"] < 3:
                if channel == "METROTVSTREAMING":
                    containers_to_restart = ["engine_server_converter_metro", "engine_metro_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "KOMPASSTREAMING":
                    containers_to_restart = ["engine_server_converter_kompas", "engine_kompas_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "CNBCSTREAMING":
                    containers_to_restart = ["engine_server_converter_cnbc", "engine_cnbc_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "CNNSTREAMING":
                    containers_to_restart = ["engine_server_converter_cnn", "engine_cnn_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
            if data[key_data[key]]["total_video_last_hour"] < 2:
                if channel == "IDXSTREAMING":
                    containers_to_restart = ["engine_server_converter_idx","engine_server_converter_idx_audio","engine_server_converter_idx_video"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                elif channel == "GARUDASTREAMING":
                    containers_to_restart = ["engine_server_converter_garuda","engine_garuda_v1"]

                    for name_containers in containers_to_restart:
                        try:
                            # Membuat koneksi dengan Docker daemon
                            # Menentukan URL Docker API
                            docker_api_url = 'unix://var/run/docker.sock'  # Ganti dengan URL yang sesuai

                            # Membuat objek klien Docker dengan URL yang ditentukan
                            client = docker.DockerClient(base_url=docker_api_url)

                            # Mengambil objek container berdasarkan nama atau ID
                            container = client.containers.get(name_containers)

                            # Memulai ulang (restart) container
                            container.restart()

                            logging.info(f"Container '{name_containers}' berhasil di-restart.")
                        except docker.errors.NotFound as e:
                            logging.error(f"Error: Container '{name_containers}' tidak ditemukan.")
                            continue
                        except docker.errors.APIError as e:
                            logging.error(f"Error: Terjadi kesalahan API Docker - {e}")
                            continue
                        except Exception as e:
                            logging.error(f"Error: Terjadi kesalahan yang tidak terduga - {e}")
                            continue
                else:
                    print('tidak ada')
                            

    def execute(self) -> None:
        try:
            self.start_time = time.time()
            data = self.get_file_data()
            self.generate_send_chart(data)
            logging.info("Success execute task")
        except Exception as e:
            logging.error(f"Error: {e}")
            self.start_proses = False
        return None


    def StartEngine(self):
        progress_bar = tqdm.tqdm(total=self.delay_proses, desc="Waiting for next task")
        while self.start_proses:
            try:

                if self.start_time == 0 or time.time() - self.start_time >= self.delay_proses:
                    self.execute()
                    progress_bar.reset()
                    os.system('cls' if os.name == 'nt' else 'clear')
                progress_bar.update(1)
                time.sleep(1)       
            except Exception as e:
                logging.error(f"Error: {e}")
                progress_bar.reset()
                self.start_proses = False
                break
            except KeyboardInterrupt:
                progress_bar.reset()
                logging.info("Close Ops")
                self.start_proses = False
                break
        progress_bar.close()


if __name__ == "__main__":
    CONFIG = Config().OPSV3
    ops = Ops(
        TOKEN=CONFIG["TELE_TOKEN"],
        CHAT_ID=CONFIG["TELE_CHAT_ID"],
        delay_proses=CONFIG["SEND_TIME"],
        storage_path_mp4=CONFIG["STORAGE_PATH"],
    )
    ops.StartEngine()
