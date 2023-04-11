class Config(object):

    ENGINE = dict(
        INEWSSTREAMING = dict(
            ENVIRONMENT = "prod",
            URL = "https://www.inews.id/streaming",
            SDI = "inews-sdi.m3u8",
            AUTH_KEY = "auth_key",
            RESOLUTION = "640x360",
            HOST_DIRECTORY = "https://d-inews.rctiplus.id",
            UPLOAD_LOCATION = "/home/kabayangroup/www/produksi-tv/public/video_list/INEWSSTREAMING",
            HEADERS = {
                'origin': 'https://embed.rctiplus.com',
                'referer': 'https://embed.rctiplus.com',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        CNNSTREAMING = dict(
            ENVIRONMENT = "prod",
            HOST_DIRECTORY = "https://live.cnnindonesia.com/livecnn/smil:cnntv.smil",
            URL_SEGMENT = "chunklist_w1002049210_b192000_sleng.m3u8",
            UPLOAD_LOCATION = "/home/kabayangroup/www/produksi-tv/public/video_list/CNNSTREAMING",
            HEADERS = {
                'referer': 'https://www.cnnindonesia.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        KOMPASSTREAMING = dict(
            ENVIRONMENT = "prod",
            URL = "https://www.youtube.com/watch?v=4rmf-lk3ito",
            QUALITY = "360p",
            UPLOAD_LOCATION = "/home/kabayangroup/www/produksi-tv/public/video_list/KOMPASSTREAMING",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        METROTVSTREAMING = dict(
            ENVIRONMENT = "prod",
            URL = "https://www.youtube.com/watch?v=IsXMe-W04os",
            QUALITY = "360p",
            UPLOAD_LOCATION = "/home/kabayangroup/www/produksi-tv/public/video_list/METROTVSTREAMING",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
    )

    ENGINE_KEYS = list(ENGINE.keys())

    OPS = dict(
        TELE_TOKEN = "5932299476:AAG4YmekrMEVMHaljj01xOqZX1LuBpjEyBw",
        TELE_CHAT_UD = "-912205350",
        SEND_TIME = 60 * 60,
        STORAGE_PATH = {
            ENGINE_KEYS[0]: ENGINE[ENGINE_KEYS[0]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[1]: ENGINE[ENGINE_KEYS[1]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[2]: ENGINE[ENGINE_KEYS[2]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[3]: ENGINE[ENGINE_KEYS[3]]["UPLOAD_LOCATION"],
        }
    )

    SOCKET_SERVER = dict(
        HOST = "127.0.0.1",
        PORT = 6969,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )