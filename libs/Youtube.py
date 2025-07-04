import yt_dlp
import os, sys, random


def get_youtube(data):
    # proxy_list = list({
    #     'socks5://trkcytfh:xtfqu68rlqwr@130.180.228.85:6369',
    #     'socks5://trkcytfh:xtfqu68rlqwr@46.203.43.196:6183',
    #     'socks5://trkcytfh:xtfqu68rlqwr@46.203.43.196:6183'
    #     })
    # proxy_url = random.choice(proxy_list)
    # Konfigurasi yt_dlp
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'force_generic_extractor': False,
        'extract_flat': True,
        # 'proxy': proxy_url,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            url = f"https://www.youtube.com/channel/{data}/live"
            # print(f"Memeriksa siaran langsung untuk {data}...")
            # Mengambil informasi siaran langsung
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
            # info = ydl.extract_info(url, download=False)
            if '_type' in info and info['_type'] == 'url':
                # print("Live URL:", info['url'])
                return info['url']
            else:
                print("Tidak ada siaran langsung aktif saat ini.") 
                return None
        except Exception as e:
            print("Error:", str(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None
