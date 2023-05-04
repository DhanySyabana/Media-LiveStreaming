class Config(object):

    ENGINE = dict(
        INEWSSTREAMING = dict(
            ENVIRONMENT = "prod",
            URLV1 = "https://tv.inews.id/live",
            RESOLUTIONV1 = "640x360",
            HOST_DIRECTORYV1 = "https://inews-linier.rctiplus.id",
            RESOLUTION = "426x240",
            HOST_DIRECTORY = "https://midcache.rctiplus.com/live",
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
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
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
            URL = "https://www.youtube.com/watch?v=a_PTnruagQ0",
            QUALITY = "360p",
            UPLOAD_LOCATION = "/home/kabayangroup/www/produksi-tv/public/video_list/METROTVSTREAMING",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        CNBCSTREAMING = dict(
            ENVIRONMENT = "prod",
            HOST_DIRECTORY = "https://live.cnbcindonesia.com/livecnbc/smil:cnbctv.smil",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = "/home/kabayangroup/www/produksi-tv/public/video_list/CNBCSTREAMING",
            HEADERS = {
                'referer': 'https://www.cnbcindonesia.com/',
                'origin': 'https://www.cnbcindonesia.com',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        IDXSTREAMING = dict(
            ENVIRONMENT = "prod",
            URLV1 = "https://www.indihometv.com/livetv/idx",
            RESOLUTIONV1 = "640x360",
            PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/joss/134/idx/playlist.m3u8",
            HOST_DIRECTORYV1 = "https://cdnkbl2.indihometv.com/joss/134/idx",
            UPLOAD_LOCATION = "/home/kabayangroup/www/produksi-tv/public/video_list/IDXSTREAMING",
            HEADERS = {
                'origin': 'https://www.indihometv.com',
                'referer': 'https://www.indihometv.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            }
        )
    )

    ENGINE_KEYS = list(ENGINE.keys())

    OPS = dict(
        TELE_TOKEN = "5932299476:AAG4YmekrMEVMHaljj01xOqZX1LuBpjEyBw",
        TELE_CHAT_ID = "-912205350",
        SEND_TIME = 60 * 30,
        STORAGE_PATH = {
            ENGINE_KEYS[0]: ENGINE[ENGINE_KEYS[0]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[1]: ENGINE[ENGINE_KEYS[1]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[2]: ENGINE[ENGINE_KEYS[2]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[3]: ENGINE[ENGINE_KEYS[3]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[4]: ENGINE[ENGINE_KEYS[4]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[5]: ENGINE[ENGINE_KEYS[5]]["UPLOAD_LOCATION"]
        }
    )

    SOCKET_SERVER = dict(
        HOST = "127.0.0.1",
        PORT = 6969,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_NOTIFICATIONS = dict(
        HOST = "36.88.248.50",
        PORT = 8888,
        BUFFER_SIZE = 1024,
        DELAY_CLIENT = 5
    )
