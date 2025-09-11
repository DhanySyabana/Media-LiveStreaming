# from settings.Connector import get_channel_data
class Config(object):
    ENGINE = dict(
        INEWSSTREAMING = dict(
            ENVIRONMENT = "dev",
            # URL = get_channel_data('TVONESTREAMING')[0].get('url', ''),
            # QUALITY = get_channel_data('TVONESTREAMING')[0].get('resolusi', ''),
            UPLOAD_LOCATION = "storage/inews",
            # COOKIES = get_channel_data('TVONESTREAMING')[0].get('cookies', ''),
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        # INEWSSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URLV1 = "https://www.indihometv.com/livetv/inews",
        #     RESOLUTIONV1 = "640x360",
        #     # PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/joss/134/inews/playlist.m3u8",
        #     PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/atm/hlsv3/inews/playlist.m3u8",
        #     HOST_DIRECTORYV1 = "https://cdnkbl2.indihometv.com/joss/134/inews",
        #     UPLOAD_LOCATION = "storage/inews",
        #     HEADERS = {
        #         'origin': 'https://www.indihometv.com',
        #         'referer': 'https://www.indihometv.com/',
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        #         'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114    ',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'cross-site',
        #         'accept': '*/*',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en-US,en;q=0.9,id;q=0.8'
        #     }
        # ),
        # INEWSSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URLV1 = "https://embed.rctiplus.com/live/inews/inewsid",
        #     RESOLUTIONV1 = "640x360",
        #     # HOST_DIRECTORYV1 = "https://inewscdn.rctiplus.id", #OLD
        #     HOST_DIRECTORYV1 = "https://icdn.rctiplus.id", #NEW
        #     RESOLUTION = "640x360",
        #     # HOST_DIRECTORY = "https://midcache.rctiplus.com/live",
        #     UPLOAD_LOCATION = "storage/inews",
        #     HEADERS = {
        #         'origin': 'https://embed.rctiplus.com',
        #         'referer': 'https://embed.rctiplus.com/',
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        #         'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'cross-site',
        #         'accept': '*/*',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en-US,en;q=0.9'
        #     }
        # ),
        KOMPASSTREAMING = dict(
            ENVIRONMENT = "dev",
            # URL = get_channel_data('KOMPASSTREAMING')[0].get('url', ''),
            # QUALITY = get_channel_data('KOMPASSTREAMING')[0].get('resolusi', ''),
            UPLOAD_LOCATION = "storage/kompas",
            # COOKIES = get_channel_data('KOMPASSTREAMING')[0].get('cookies', ''),
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        # KOMPASSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL ='https://www.youtube.com/watch?v=J9J1jJ1J1J1',
        #     QUALITY = "360p",
        #     UPLOAD_LOCATION = "storage/kompas",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        #     }
        # ),
        # METROTVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     HOST_DIRECTORY = "https://edge.medcom.id/live-edge/smil:metro.smil",
        #     PLAYLIST = "playlist.m3u8",
        #     RESOLUTION = "640x360",
        #     UPLOAD_LOCATION = "storage/metro",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        #     }
        # ),
        METROTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            # URL = get_channel_data('METROTVSTREAMING')[0].get('url', ''),
            # QUALITY = get_channel_data('METROTVSTREAMING')[0].get('resolusi', ''),
            UPLOAD_LOCATION = "storage/metro",
            # COOKIES = get_channel_data('METROTVSTREAMING')[0].get('cookies', ''),
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        # METROTVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     # URL = "https://www.youtube.com/watch?v=qA7_9fcCbZ8",
        #     URL = "https://www.youtube.com/watch?v=nfgnpM28xDA",
        #     QUALITY = "360p",
        #     UPLOAD_LOCATION = "storage/metro",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        #     }
        # ),
        # METROTVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.vidio.com/live/777/tokens",
        #     RESOLUTION = "640x360",
        #     PLAYLIST = "B1News_320x240.m3u8",
        #     HOST_DIRECTORY = "https://etslive-app.vidio.com/live/777/master.m3u8",
        #     UPLOAD_LOCATION = "storage/metro",
        #     HEADERS = {
        #         'origin': 'https://www.vidio.com',
        #         'referer': 'https://www.vidio.com/',
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        #         'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'cross-site',
        #         'accept': '*/*',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en-US,en;q=0.9'
        #     }
        # ),
        CNNSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://live.cnnindonesia.com/livecnn/smil:cnntv.smil",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = "storage/cnn",
            HEADERS = {
                'referer': 'https://www.cnnindonesia.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        CNBCSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://live.cnbcindonesia.com/livecnbc/smil:cnbctv.smil",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = "storage/cnbc",
            HEADERS = {
                'referer': 'https://www.cnbcindonesia.com/',
                'origin': 'https://www.cnbcindonesia.com',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        # IDXSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URLV1 = "https://www.indihometv.com/livetv/idx",
        #     RESOLUTIONV1 = "640x360",
        #     # PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/joss/134/idx/playlist.m3u8", #old
        #     # PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/atm/HLS-10s/idx/playlist.m3u8", #old
        #     # PLAYLIST_DIRECTORYV1 = "https://cdn10jtedge.indihometv.com/atm/hlsv3/idx/playlist.m3u8",
        #     PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/atm/hlsv3/idx/playlist.m3u8",
            
            
        #     HOST_DIRECTORYV1 = "https://cdnkbl2.indihometv.com/joss/134/idx",
        #     UPLOAD_LOCATION = "storage/idx",
        #     HEADERS = {
        #         'origin': 'https://www.indihometv.com',
        #         'referer': 'https://www.indihometvf.com/',
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        #         'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114    ',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'cross-site',
        #         'accept': '*/*',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en-US,en;q=0.9,id;q=0.8'
        #     }
        # ),
        IDXSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.youtube.com/live/O6dTFyyhHLI?si=h1DRWvlV5R8ELBoT",
            QUALITY = "360p",
            UPLOAD_LOCATION = "storage/idx",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        TVONESTREAMING = dict(
            ENVIRONMENT = "dev",
            # URL = get_channel_data('TVONESTREAMING')[0].get('url', ''),
            # QUALITY = get_channel_data('TVONESTREAMING')[0].get('resolusi', ''),
            UPLOAD_LOCATION = "storage/tvone",
            # COOKIES = get_channel_data('TVONESTREAMING')[0].get('cookies', ''),
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        # TVONESTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.vidio.com/live/783/tokens",
        #     RESOLUTION = "640x360",
        #     PLAYLIST = "index.m3u8",
        #     HOST_DIRECTORY = "https://etslive-app.vidio.com/live/783/master.m3u8",
        #     UPLOAD_LOCATION = "storage/tvone",
        #     HEADERS = {
        #         'origin': 'https://www.vidio.com',
        #         'referer': 'https://www.vidio.com/',
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        #         'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'cross-site',
        #         'accept': '*/*',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en-US,en;q=0.9'
        #     }
        # ),

        BERITASATUSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://beritasatu.secureswiftcontent.com/han/beritasatu/bsatu10008r/srtoutput",
            UPLOAD_LOCATION = "storage/beritasatu",
            HEADERS = {"User-Agent": "Mozilla/5.0"},
            # audio & video dipisah lewat PLAYLIST
            PLAYLIST_AUDIO = "haudio-eng.m3u8",
            PLAYLIST_VIDEO = "hvideo-640x360.m3u8",
            RESOLUTION = None,
        ),



        
        TVRISTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "http://klik.tvri.go.id/",
            RESOLUTION = "640x360",
            # RESOLUTION = "480x240", #OLD
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://ott-balancer.tvri.go.id/live/eds/Nasional/hls/Nasional.m3u8",
            HOST_DIRECTORY_TS = "https://ott-balancer.tvri.go.id/live/eds/Nasional",
            UPLOAD_LOCATION = "storage/tvri",
            HEADERS = {
                'origin': 'http://klik.tvri.go.id',
                'referer': 'http://klik.tvri.go.id/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114    ',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8'
            }
        ),
        # TVRISTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.vidio.com/live/6441/tokens",
        #     RESOLUTION = "640x360",
        #     PLAYLIST = "index.m3u8",
        #     HOST_DIRECTORY = "https://etslive-app.vidio.com/live/6441/master.m3u8",
        #     UPLOAD_LOCATION = "storage/tvri",
        #     HEADERS = {
        #         'origin': 'https://www.vidio.com',
        #         'referer': 'https://www.vidio.com/',
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        #         'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'cross-site',
        #         'accept': '*/*',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en-US,en;q=0.9'
        #     }
        # ),
        RCTISTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "https://www.rctiplus.com/tv/rcti",
            RESOLUTIONV1 = "640x360",
            # HOST_DIRECTORYV1 = "https://rcdn.rctiplus.id",
            # HOST_DIRECTORYV1 = "https://rcticdn.rctiplus.id", # OLD
            HOST_DIRECTORYV1 = "https://rcti-linier.rctiplus.id", #NEW
            RESOLUTION = "426x240",
            # HOST_DIRECTORY = "https://midcache.rctiplus.com/live",
            UPLOAD_LOCATION = "storage/rcti",
            HEADERS = {
                'origin': 'https://www.rctiplus.com',
                'referer': 'https://www.rctiplus.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
        ),
        # RCTISTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URLV1 = "https://tv.okezone.com/streaming/rcti",
        #     RESOLUTIONV1 = "426x240",
        #     # HOST_DIRECTORYV1 = "https://eng.rctiplus.id", # NEW
        #     HOST_DIRECTORYV1 = "https://rcti-linier.rctiplus.id", # OLD
        #     RESOLUTION = "426x240",
        #     HOST_DIRECTORY = "https://midcache.rctiplus.com/live",
        #     UPLOAD_LOCATION = "storage/rcti",
        #     HEADERS = {
        #         'origin': 'https://embed.rctiplus.com',
        #         'referer': 'https://embed.rctiplus.com/',
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        #         'sec-ch-ua': 'Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"macOS"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'cross-site',
        #         'accept': '*/*',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en-US,en;q=0.9'
        #     }
        # ),
        TRANS7STREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://video.detik.com/trans7/smil:trans7.smil",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = "storage/trans7",
            HEADERS = {
                'origin': 'https://20.detik.com',
                'referer': 'https://20.detik.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        # TRANS7STREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.transtv.co.id/live/trans7",
        #     RESOLUTION = "848x477",
        #     PLAYLIST = "x8qckyq.m3u8",
        #     HOST_DIRECTORY = "https://www.dailymotion.com/cdn/live/video/x8qckyq.m3u8",
        #     PATH_URL =  "https://etslive-v3-vidio-com-tokenized.akamaized.net",
        #     UPLOAD_LOCATION = "storage/trans7",
        #     HEADERS = {
        #         'origin': 'https://geo.dailymotion.com',
        #         'referer': 'https://geo.dailymotion.com/',
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        #         'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'cross-site',
        #         'accept': '*/*',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en-US,en;q=0.9'
        #     }
        # ),
        TRANSTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://video.detik.com/transtv/smil:transtv.smil",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = "storage/transtv",
            HEADERS = {
                'origin': 'https://20.detik.com',
                'referer': 'https://20.detik.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        RTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.vidio.com/live/1561/tokens",
            RESOLUTION = "640x360",
            PLAYLIST = "B1News_320x240.m3u8",
            HOST_DIRECTORY = "https://etslive-app.vidio.com/live/1561/master.m3u8",
            UPLOAD_LOCATION = "storage/rtv",
            HEADERS = {
                'origin': 'https://www.vidio.com',
                'referer': 'https://www.vidio.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
        ),
        MNCSTREAMING = dict(
            ENVIRONMENT = "dev",
            # URLV1 = "https://www.indihometv.com/livetv/mncnews",
            # RESOLUTIONV1 = "640x360",
            # PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/joss/134/mncnews/playlist.m3u8",
            # PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/atm/hlsv3/mncnews/playlist.m3u8",
            # HOST_DIRECTORYV1 = "https://cdnkbl2.indihometv.com/joss/134/mncnews",
            UPLOAD_LOCATION = "storage/mnc",
            HEADERS = {
                'origin': 'https://www.indihometv.com',
                'referer': 'https://www.indihometv.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114    ',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8'
            }
        ),
        # MNCSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.youtube.com/watch?v=mPfD52n-zdE",
        #     QUALITY = "360p",
        #     UPLOAD_LOCATION = "storage/mnc",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        #     }
        # ),
        SEATODAYSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.vidio.com/live/7687-sea-today",
            RESOLUTION = "640x360",
            PLAYLIST = "B1News_320x240.m3u8",
            #HOST_DIRECTORY = "https://etslive-app.vidio.com/live/7687/master.m3u8",
            #HOST_DIRECTORY = "https://etslive-2-vidio-com.akamaized.net/live/7687/master.m3u8",
            # HOST_DIRECTORY = "https://etslive-v3-vidio-com-tokenized.akamaized.net/live/7687/master.m3u8",
            HOST_DIRECTORY = "https://etslive-v3-vidio-com-tokenized.akamaized.net/stream/7687/file/live/7687/master.m3u8",
            PATH_URL =  "https://etslive-v3-vidio-com-tokenized.akamaized.net",
            UPLOAD_LOCATION = "storage/seatoday",
            HEADERS = {
                'origin': 'https://www.vidio.com',
                'referer': 'https://www.vidio.com/live/7687-sea-today',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
        ),
        # GARUDASTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     # URLV1 = "https://www.beritasatu.com/livestream", OLD
        #     URLV1 = "https://hgmtv.com:19360/garudatvlivestreaming/garudatvlivestreaming.m3u8",
        #     RESOLUTION = "640x360",
        #     PLAYLIST = "01.m3u8",
        #     HOST_DIRECTORY = "https://hgmtv.com:19360/garudatvlivestreaming",
        #     UPLOAD_LOCATION = "storage/garuda",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        #         'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'cross-site',
        #         'accept': '*/*',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en-US,en;q=0.9'
        #     }
        # ),
        GARUDASTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.vidio.com/live/18162-garuda-tv",
            RESOLUTION = "640x360",
            PLAYLIST = "B1News_320x240.m3u8",
            #HOST_DIRECTORY = "https://etslive-app.vidio.com/live/7687/master.m3u8",
            #HOST_DIRECTORY = "https://etslive-2-vidio-com.akamaized.net/live/7687/master.m3u8",
            # HOST_DIRECTORY = "https://etslive-v3-vidio-com-tokenized.akamaized.net/live/7687/master.m3u8",
            HOST_DIRECTORY = "https://etslive-v3-vidio-com-tokenized.akamaized.net/stream/18162/file/live/18162/master.m3u8",
            PATH_URL =  "https://etslive-v3-vidio-com-tokenized.akamaized.net",
            UPLOAD_LOCATION = "storage/garuda",
            HEADERS = {
                'origin': 'https://www.vidio.com',
                'referer': 'https://www.vidio.com/live/18162-garuda-tv',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
        ),
        TVRIBALISTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "http://klik.tvri.go.id/",
            RESOLUTION = "640x360",
            # RESOLUTION = "480x240", #OLD
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://ott-balancer.tvri.go.id/live/eds/Bali/hls/Bali.m3u8",
            HOST_DIRECTORY_TS = "https://ott-balancer.tvri.go.id/live/eds/Bali",
            UPLOAD_LOCATION = "storage/tvribali",
            HEADERS = {
                'origin': 'http://klik.tvri.go.id',
                'referer': 'http://klik.tvri.go.id/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114    ',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8'
            }
        ),
        TVRIJATIMSTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "http://klik.tvri.go.id/",
            RESOLUTION = "640x360",
            # RESOLUTION = "480x240", #OLD
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://ott-balancer.tvri.go.id/live/eds/Jatim/hls/Jatim.m3u8",
            HOST_DIRECTORY_TS = "https://ott-balancer.tvri.go.id/live/eds/Jatim",
            UPLOAD_LOCATION = "storage/tvrijatim",
            HEADERS = {
                'origin': 'http://klik.tvri.go.id',
                'referer': 'http://klik.tvri.go.id/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114    ',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8'
            }
        ),
        TVRIKALBARSTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "http://klik.tvri.go.id/",
            RESOLUTION = "640x360",
            # RESOLUTION = "480x240", #OLD
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://ott-balancer.tvri.go.id/live/eds/Kalbar/hls/Kalbar.m3u8",
            HOST_DIRECTORY_TS = "https://ott-balancer.tvri.go.id/live/eds/Kalbar",
            UPLOAD_LOCATION = "storage/tvrikalbar",
            HEADERS = {
                'origin': 'http://klik.tvri.go.id',
                'referer': 'http://klik.tvri.go.id/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114    ',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8'
            }
        ),
        TVRILAMPUNGSTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "http://klik.tvri.go.id/",
            RESOLUTION = "640x360",
            # RESOLUTION = "480x240", #OLD
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://ott-balancer.tvri.go.id/live/eds/Lampung/hls/Lampung.m3u8",
            HOST_DIRECTORY_TS = "https://ott-balancer.tvri.go.id/live/eds/Lampung",
            UPLOAD_LOCATION = "storage/tvrilampung",
            HEADERS = {
                'origin': 'http://klik.tvri.go.id',
                'referer': 'http://klik.tvri.go.id/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114    ',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8'
            }
        ),
        TVRISULSELSTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "http://klik.tvri.go.id/",
            RESOLUTION = "640x360",
            # RESOLUTION = "480x240", #OLD
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://ott-balancer.tvri.go.id/live/eds/Sulsel/hls/Sulsel.m3u8",
            HOST_DIRECTORY_TS = "https://ott-balancer.tvri.go.id/live/eds/Sulsel",
            UPLOAD_LOCATION = "storage/tvrisulsel",
            HEADERS = {
                'origin': 'http://klik.tvri.go.id',
                'referer': 'http://klik.tvri.go.id/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114    ',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8'
            }
        ),
        # JAKTVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     # URLV1 = "https://www.beritasatu.com/livestream", OLD
        #     URLV1 = "https://op-group1-swiftservesd-1.dens.tv/s/s123/S4",
        #     # https://op-group1-swiftservesd-1.dens.tv/s/s123/S4/mnf.m3u8
        #     RESOLUTION = "640x360",
        #     PLAYLIST = "mnf.m3u8",
        #     HOST_DIRECTORY = "https://op-group1-swiftservesd-1.dens.tv/s/s123/S4",
        #     UPLOAD_LOCATION = "storage/jaktv",
        #     HEADERS = {
        #         'origin': 'https://www.dens.tv',
        #         'referer': 'https://www.dens.tv/',
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        #         'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'cross-site',
        #         'accept': '*/*',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en-US,en;q=0.9'
        #     }
        # ),
        JAKTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.vidio.com/live/5415-jaktv",
            RESOLUTION = "640x360",
            PLAYLIST = "B1News_320x240.m3u8",
            #HOST_DIRECTORY = "https://etslive-app.vidio.com/live/7687/master.m3u8",
            #HOST_DIRECTORY = "https://etslive-2-vidio-com.akamaized.net/live/7687/master.m3u8",
            HOST_DIRECTORY = "https://etslive-v3-vidio-com-tokenized.akamaized.net/live/5415/master.m3u8",
            PATH_URL =  "https://etslive-v3-vidio-com-tokenized.akamaized.net",
            UPLOAD_LOCATION = "storage/jaktv",
            HEADERS = {
                'origin': 'https://www.vidio.com',
                'referer': 'https://www.vidio.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
        ),
        BANTENTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            # URLV1 = "https://www.beritasatu.com/livestream", OLD
            URLV1 = "https://5bf7b725107e5.streamlock.net/bantentv/bantentv",
            
            RESOLUTION = "1280x720",
            PLAYLIST = "playlist.m3u8",
            HOST_DIRECTORY = "https://5bf7b725107e5.streamlock.net/bantentv/bantentv",
            UPLOAD_LOCATION = "storage/bantentv",
            HEADERS = {
                'origin': 'https://wms.klikhost.com:2000',
                'referer': 'https://wms.klikhost.com:2000/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
        ),  
        DHOHOSTREAMING = dict(
            ENVIRONMENT = "dev",
            # URLV1 = "https://www.beritasatu.com/livestream", OLD
            URLV1 = "https://dhohotv.siar.us/dhohotv/live",
            
            RESOLUTION = "1280x720",
            PLAYLIST = "playlist.m3u8",
            HOST_DIRECTORY = "https://dhohotv.siar.us/dhohotv/live",
            UPLOAD_LOCATION = "storage/dhoho",
            HEADERS = {
                'origin': 'https://cdn.siar.us',
                'referer': 'https://cdn.siar.us/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Chromium";v="114", "Not.A/Brand";v="8", "Chromium";v="114',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
        ),
    )

    TELEGRAM = {
        "TOKEN":"8213920361:AAEMpyChKoMGb_FHw5QNVI9xdySfjP-yrtk",
        "CHAT_ID": "-1002147735635",
        "TOPIC_ID":"3042",
    }
    # TELEGRAM = {
    #     "TOKEN":"7490394454:AAHJKYIhpf3DBX3D6nsXJZgPovH3XBIECkk",
    #     "CHAT_ID": "-1002874522539",
    #     "TOPIC_ID":"7",
    # }
    ENGINE_KEYS = list(ENGINE.keys())

    OPS = dict(
        TELE_TOKEN = "8213920361:AAEMpyChKoMGb_FHw5QNVI9xdySfjP-yrtk",
        TELE_CHAT_ID = "-1001921508509",
        SEND_TIME = 60 * 30,
        STORAGE_PATH = {
            ENGINE_KEYS[0]: ENGINE[ENGINE_KEYS[0]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[1]: ENGINE[ENGINE_KEYS[1]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[2]: ENGINE[ENGINE_KEYS[2]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[3]: ENGINE[ENGINE_KEYS[3]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[4]: ENGINE[ENGINE_KEYS[4]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[5]: ENGINE[ENGINE_KEYS[5]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[6]: ENGINE[ENGINE_KEYS[6]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[7]: ENGINE[ENGINE_KEYS[7]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[8]: ENGINE[ENGINE_KEYS[8]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[9]: ENGINE[ENGINE_KEYS[9]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[10]: ENGINE[ENGINE_KEYS[10]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[11]: ENGINE[ENGINE_KEYS[11]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[12]: ENGINE[ENGINE_KEYS[12]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[13]: ENGINE[ENGINE_KEYS[13]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[14]: ENGINE[ENGINE_KEYS[14]]["UPLOAD_LOCATION"],
        }
    )

    ### Notif channel mati ###
    OPSV2 = dict(
        TELE_TOKEN = "8213920361:AAEMpyChKoMGb_FHw5QNVI9xdySfjP-yrtk",
        TELE_CHAT_ID = "-1002147735635",
        TELEGRAM_MESSAGE_THREAD_ID = 3042,
        SEND_TIME = 60 * 60,
        STORAGE_PATH = {
            # ENGINE_KEYS[0]: ENGINE[ENGINE_KEYS[0]]["UPLOAD_LOCATION"],    
            # ENGINE_KEYS[1]: ENGINE[ENGINE_KEYS[1]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[2]: ENGINE[ENGINE_KEYS[2]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[3]: ENGINE[ENGINE_KEYS[3]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[4]: ENGINE[ENGINE_KEYS[4]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[5]: ENGINE[ENGINE_KEYS[5]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[6]: ENGINE[ENGINE_KEYS[6]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[7]: ENGINE[ENGINE_KEYS[7]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[8]: ENGINE[ENGINE_KEYS[8]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[9]: ENGINE[ENGINE_KEYS[9]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[10]: ENGINE[ENGINE_KEYS[10]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[11]: ENGINE[ENGINE_KEYS[11]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[12]: ENGINE[ENGINE_KEYS[12]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[13]: ENGINE[ENGINE_KEYS[13]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[14]: ENGINE[ENGINE_KEYS[14]]["UPLOAD_LOCATION"],
        }
    )
    
    ### restart docker ###
    OPSV3 = dict(
        TELE_TOKEN = "8213920361:AAEMpyChKoMGb_FHw5QNVI9xdySfjP-yrtk",
        TELE_CHAT_ID = "-897317690",
        SEND_TIME = 60 * 40,
        STORAGE_PATH = {
            # ENGINE_KEYS[0]: ENGINE[ENGINE_KEYS[0]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[1]: ENGINE[ENGINE_KEYS[1]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[2]: ENGINE[ENGINE_KEYS[2]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[3]: ENGINE[ENGINE_KEYS[3]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[4]: ENGINE[ENGINE_KEYS[4]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[5]: ENGINE[ENGINE_KEYS[5]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[6]: ENGINE[ENGINE_KEYS[6]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[7]: ENGINE[ENGINE_KEYS[7]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[8]: ENGINE[ENGINE_KEYS[8]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[9]: ENGINE[ENGINE_KEYS[9]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[10]: ENGINE[ENGINE_KEYS[10]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[11]: ENGINE[ENGINE_KEYS[11]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[12]: ENGINE[ENGINE_KEYS[12]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[13]: ENGINE[ENGINE_KEYS[13]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[14]: ENGINE[ENGINE_KEYS[14]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[15]: ENGINE[ENGINE_KEYS[15]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[16]: ENGINE[ENGINE_KEYS[16]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[17]: ENGINE[ENGINE_KEYS[17]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[18]: ENGINE[ENGINE_KEYS[18]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[19]: ENGINE[ENGINE_KEYS[19]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[20]: ENGINE[ENGINE_KEYS[20]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[21]: ENGINE[ENGINE_KEYS[21]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[22]: ENGINE[ENGINE_KEYS[22]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[23]: ENGINE[ENGINE_KEYS[23]]["UPLOAD_LOCATION"],
        }
    )
    
    ### Server ###
    SOCKET_SERVER = dict(
        HOST = "12.12.12.8",
        PORT = 6969,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_BERITASATU = dict(
        HOST = "12.12.12.13",
        PORT = 6868,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    SOCKET_SERVER_BERITASATU_VIDEO = dict(
        HOST = "12.12.12.99",
        PORT = 5001,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    SOCKET_SERVER_BERITASATU_AUDIO = dict(
        HOST = "12.12.12.100",
        PORT = 5002,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_IDX = dict(
        HOST = "12.12.12.15",
        PORT = 6767,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
    SOCKET_SERVER_IDX_VIDEO = dict(
        HOST = "12.12.12.37",
        PORT = 7373,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
    SOCKET_SERVER_IDX_AUDIO = dict(
        HOST = "12.12.12.38",
        PORT = 7272,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_TRANS = dict(
        HOST = "12.12.12.18",
        PORT = 6565,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_CNBC = dict(
        HOST = "12.12.12.19",
        PORT = 6464,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_KOMPAS = dict(
        HOST = "12.12.12.31",
        PORT = 5353,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_TVONE = dict(
        HOST = "12.12.12.21",
        PORT = 6262,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_RCTI = dict(
        HOST = "12.12.12.22",
        PORT = 6161,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_METRO = dict(
        HOST = "12.12.12.24",
        PORT = 6060,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_TRANSTV = dict(
        HOST = "12.12.12.26",
        PORT = 7979,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_CNN = dict(
        HOST = "12.12.12.27",
        PORT = 7878,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_RTV = dict(
        HOST = "12.12.12.29",
        PORT = 7777,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_MNC = dict(
        HOST = "12.12.12.32",
        PORT = 7676,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_INEWS = dict(
        HOST = "12.12.12.34",
        PORT = 7575,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_SEATODAY = dict(
        HOST = "12.12.12.35",
        PORT = 7474,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
    SOCKET_SERVER_GARUDA = dict(
        HOST = "12.12.12.51",
        PORT = 5151,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
    SOCKET_SERVER_TVRIBALI = dict(
        HOST = "12.12.12.42",
        PORT = 5251,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
    SOCKET_SERVER_TVRIJATIM = dict(
        HOST = "12.12.12.43",
        PORT = 5351,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
    SOCKET_SERVER_TVRIKALBAR = dict(
        HOST = "12.12.12.45",
        PORT = 5451,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
    SOCKET_SERVER_TVRILAMPUNG = dict(
        HOST = "12.12.12.47",
        PORT = 5551,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
    SOCKET_SERVER_TVRISULSEL = dict(
        HOST = "12.12.12.49",
        PORT = 5651,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    SOCKET_SERVER_JAKTV = dict(
        HOST = "12.12.12.52",
        PORT = 5751,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    SOCKET_SERVER_BANTENTV = dict(
        HOST = "12.12.12.55",
        PORT = 5851,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
    SOCKET_SERVER_DHOHOTV = dict(
        HOST = "12.12.12.57",
        PORT = 5951,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    ### end Server ###

    ### Local ###

    # SOCKET_SERVER_GARUDA = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7014,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )
    
    # SOCKET_SERVER_TVRILAMPUNG = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7014,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )
    
    # SOCKET_SERVER_TVRIKALBAR = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7014,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )
    
    # SOCKET_SERVER_TVRIJATIM = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7014,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )
    
    # SOCKET_SERVER_SEATODAY = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7014,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_INEWS = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7014,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_MNC = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7013,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_RTV = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7012,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )
    
    # SOCKET_SERVER_CNN = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7012,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_TRANSTV = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7011,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_METRO = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7010,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_RCTI = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7009,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_TVONE = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7008,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_KOMPAS = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7007,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_CNBC = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7006,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_TRANS = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7005,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_IDX = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7002,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )
    # SOCKET_SERVER_IDX_VIDEO = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7003,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )
    # SOCKET_SERVER_IDX_AUDIO = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7004,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_BERITASATU = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7001,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )


    # SOCKET_SERVER_BERITASATU_AUDIO = {
    #     "HOST": "127.0.0.1",
    #     "PORT": 9101,
    #     "MAX_CONNECTION": 10,
    #     "BUFFER_SIZE": 8192
    # }

    # SOCKET_SERVER_BERITASATU_VIDEO = {
    #     "HOST": "127.0.0.1",
    #     "PORT": 9102,
    #     "MAX_CONNECTION": 10,
    #     "BUFFER_SIZE": 8192
    # }
    # SOCKET_SERVER = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7004,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    ### end local ###

    SOCKET_NOTIFICATIONS = dict(
        HOST_SERVER = "0.0.0.0",
        HOST_CLIENT = "36.88.246.50",
        PORT = 8888,
        BUFFER_SIZE = 1024,
        DELAY_CLIENT = 300
    )

    DB = dict(
        HOST = "172.22.0.2",
        PORT = 3306,
        NAME = "log_livestream",
        USER = "root",
        PASS = "1Teung@Kabayan123",
        TABLE_NAME = "logs"
    )
