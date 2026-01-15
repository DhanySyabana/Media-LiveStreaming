class Config(object):

    ENGINE = dict(
        # INEWSSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URLV1 = "https://tv.inews.id/live",
        #     RESOLUTIONV1 = "640x360",
        #     # HOST_DIRECTORYV1 = "https://eng.rctiplus.id", # NEW
        #     HOST_DIRECTORYV1 = "https://inews-linier.rctiplus.id", # OLD
        #     RESOLUTION = "426x240",
        #     HOST_DIRECTORY = "https://midcache.rctiplus.com/live",
        #     UPLOAD_LOCATION = "storage/inews",
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

        #ENGINE_KEYS[0]
        INEWSSTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "https://www.rctiplus.com/tv/inews",
            RESOLUTIONV1 = "640x360",
            # HOST_DIRECTORYV1 = "https://inews-linier.rctiplus.id", #old
            HOST_DIRECTORYV1 = "https://icdn.rctiplus.id", #NEW
            RESOLUTION = "640x360",
            # HOST_DIRECTORY = "https://midcache.rctiplus.com/live",
            UPLOAD_LOCATION = "storage/inews",
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

        #ENGINE_KEYS[1]
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

        #ENGINE_KEYS[2]
        KOMPASSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.youtube.com/watch?v=DOOrIxw5xOw",
            QUALITY = "360p",
            UPLOAD_LOCATION = "storage/kompas",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        # METROTVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     HOST_DIRECTORY = "https://edge.medcom.id/live-edge/smil:metro.smil",
        #     # HOST_DIRECTORY = "https://edge.medcom.id/live-edge/smil:mgnch.smil",
        #     PLAYLIST = "playlist.m3u8",
        #     RESOLUTION = "426x240",
        #     UPLOAD_LOCATION = "storage/metro",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        #     }
        # ),

        #ENGINE_KEYS[3]
        METROTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            # URL = "https://www.youtube.com/watch?v=qA7_9fcCbZ8",
            # URL = "https://www.youtube.com/watch?v=nfgnpM28xDA",
            URL = "https://www.youtube.com/watch?v=-CwtcKDaaLA",
            ID_CHANNEL = "UCzl0OrB3-ehunyotIQvK77A",
            QUALITY = "360p",
            UPLOAD_LOCATION = "storage/metro",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        # METROTVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URLV1 = "https://www.indihometv.com/livetv/metrotv",
        #     RESOLUTIONV1 = "640x360",
        #     PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/atm/hlsv3/METRO_TV/playlist.m3u8",
        #     HOST_DIRECTORYV1 = "https://cdnkbl2.indihometv.com/joss/133/metrotv1080",
        #     UPLOAD_LOCATION = "storage/metro",
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

        #ENGINE_KEYS[4]
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
        #ENGINE_KEYS[5]
        IDXSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.youtube.com/watch?v=QB3oe7Q31F0",
            QUALITY = "360p",
            ID_CHANNEL = "UCQA6NejSxQguRkD3L8eXHzA",
            UPLOAD_LOCATION = "storage/idx",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        # TVONESTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     # URLV1 = "https://www.beritasatu.com/livestream", OLD
        #     URLV1 = "https://op-group1-swiftservehd-1.dens.tv/h/h224",
        #     RESOLUTION = "640x360",
        #     PLAYLIST = "index.m3u8",
        #     HOST_DIRECTORY = "https://op-group1-swiftservehd-1.dens.tv/h/h224",
        #     UPLOAD_LOCATION = "storage/tvone",
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
        #ENGINE_KEYS[6]
        TVONESTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.youtube.com/watch?v=yNKvkPJl-tg&feature=youtu.be",
            QUALITY = "360p",
            UPLOAD_LOCATION = "storage/tvone",
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
        #ENGINE_KEYS[7]
        BERITASATUSTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "https://www.dens.tv/tv-local/watch/131/berita-satu",
            RESOLUTION = "640x360",
            # RESOLUTION = "1024x576",
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://op-group1-swiftservehd-1.dens.tv/h/h209",
            UPLOAD_LOCATION = "storage/beritasatu",
            HEADERS = {
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
        # BERITASATUSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.youtube.com/watch?v=QB3oe7Q31F0",
        #     QUALITY = "360p",
        #     ID_CHANNEL = "UCQA6NejSxQguRkD3L8eXHzA",
        #     UPLOAD_LOCATION = "storage/beritasatu",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        #     }
        # ),
        # BERITASATUSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.vidio.com/live/6165/tokens",
        #     RESOLUTION = "640x360",
        #     PLAYLIST = "B1News_320x240.m3u8",
        #     HOST_DIRECTORY = "https://etslive-app.vidio.com/live/6165/master.m3u8",
        #     UPLOAD_LOCATION = "storage/beritasatu",
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
        #ENGINE_KEYS[8]
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
        #     URL = "https://www.vidio.com/live/6441-tvri", 
        #     RESOLUTION = "640x360",
        #     PLAYLIST = "B1News_320x240.m3u8",
        #     HOST_DIRECTORY = "https://etslive-v3-vidio-com-tokenized.akamaized.net/live/6441/master.m3u8",
        #     PATH_URL =  "https://etslive-v3-vidio-com-tokenized.akamaized.net",
        #     UPLOAD_LOCATION = "storage/tvri",
        #     HEADERS = {
        #         'origin': 'https://www.vidio.com',
        #         'referer': 'https://www.vidio.com/live/6441-tvri',
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
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
        #ENGINE_KEYS[9]
        RCTISTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "https://www.rctiplus.com/tv/rcti",
            RESOLUTIONV1 = "640x360",
            # HOST_DIRECTORYV1 = "https://rcti-linier.rctiplus.id", #old
            HOST_DIRECTORYV1 = "https://rcdn.rctiplus.id", #NEW
            RESOLUTION = "426x240",
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
        #  TRANS7STREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://sevenhub.id/live",
        #     RESOLUTION = "848x477",
        #     PLAYLIST = "x8qckyq.m3u8",
        #     #HOST_DIRECTORY = "https://etslive-app.vidio.com/live/7687/master.m3u8",
        #     #HOST_DIRECTORY = "https://etslive-2-vidio-com.akamaized.net/live/7687/master.m3u8",
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
        # TRANS7STREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     HOST_DIRECTORY = "https://video.detik.com/trans7/smil:trans7.smil",
        #     PLAYLIST = "playlist.m3u8",
        #     RESOLUTION = "640x360",
        #     UPLOAD_LOCATION = "storage/trans7",
        #     HEADERS = {
        #         'origin': 'https://20.detik.com',
        #         'referer': 'https://20.detik.com/',
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        #     }
        # ),
        #ENGINE_KEYS[10]
        TRANS7STREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://video.detik.com/trans7/smil:trans7.smil",
            #HOST_DIRECTORY ="https://pullstream.transtv.co.id/livettv",
            # https://pullstream.transtv.co.id/livettv/
            #PLAYLIST = "livestreamttv.m3u8",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = "storage/trans7",
            HEADERS = {
                'origin': 'https://20.detik.com',
                'referer': 'https://20.detik.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        #ENGINE_KEYS[11]
        TRANSTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://video.detik.com/transtv/smil:transtv.smil",
            #HOST_DIRECTORY ="https://pullstream.transtv.co.id/livettv",
            # https://pullstream.transtv.co.id/livettv/
            #PLAYLIST = "livestreamttv.m3u8",
            PLAYLIST = "chunklist_w835097260_b744100_sleng.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = "storage/transtv",
            HEADERS = {
                'origin': 'https://20.detik.com',
                'referer': 'https://20.detik.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        # RTVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.vidio.com/live/1561/tokens",
        #     RESOLUTION = "640x360",
        #     PLAYLIST = "B1News_320x240.m3u8",
        #     HOST_DIRECTORY = "https://etslive-app.vidio.com/live/1561/master.m3u8",
        #     UPLOAD_LOCATION = "storage/rtv",
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
        # NUSANTARATVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     # URLV1 = "https://v5.siar.us/nusantaratv/live/",
        #     URLV1 = "https://nusantaratv.siar.us/nusantaratv/live/",
        #     RESOLUTION = "320x240",
        #     PLAYLIST = "playlist.m3u8",
        #     # PLAYLIST = "playlist.m3u8",
        #     # HOST_DIRECTORY = "https://v5.siar.us/nusantaratv/live",
        #     HOST_DIRECTORY = "https://nusantaratv.siar.us/nusantaratv/live",
        #     UPLOAD_LOCATION = "storage/nusantaratv",
        #     HEADERS = {
        #         'origin': 'https://nusantaratv.com',
        #         'referer': 'https://nusantaratv.com/',
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
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
        # NUSANTARATVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.youtube.com/watch?v=1TeWDeIVRJc",
        #     ID_CHANNEL = "UCAMpZJJNQPZ6q7ZYKJV1igQ",
        #     QUALITY = "360p",
        #     UPLOAD_LOCATION = "storage/nusantaratv",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        #     }
        # ),
        #ENGINE_KEYS[12]
        NUSANTARATVSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://op-group1-swiftservehd-1.dens.tv/h/h37", 
            RESOLUTION = "480x360",
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://op-group1-swiftservehd-1.dens.tv/h/h37",
            PATH_URL =  "https://etslive-v3-vidio-com-tokenized.akamaized.net",
            UPLOAD_LOCATION = "storage/nusantaratv",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
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
        # MNCSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URLV1 = "https://www.indihometv.com/livetv/mncnews",
        #     RESOLUTIONV1 = "640x360",
        #     #PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/joss/134/mncnews/playlist.m3u8",
        #     #PLAYLIST_DIRECTORYV1 = "ttps://streaming.indihometv.com/atm/HLS-10s/mncnews/playlist.m3u8", 
        #     PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/atm/hlsv3/mncnews/playlist.m3u8", 
        #     HOST_DIRECTORYV1 = "https://cdnkbl2.indihometv.com/joss/134/mncnews",
        #     UPLOAD_LOCATION = "storage/mnc",
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
        #ENGINE_KEYS[13]
        MNCSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.youtube.com/watch?v=B9dEq-lU4yU",
            QUALITY = "360p",
            ID_CHANNEL = "UCGfXjFgIUUTUUlzdG6BenXA",
            UPLOAD_LOCATION = "storage/mnc",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        #ENGINE_KEYS[14]
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
        #ENGINE_KEYS[15]
        SCTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            # URL = get_channel_data('TVONESTREAMING')[0].get('url', ''),
            # QUALITY = get_channel_data('TVONESTREAMING')[0].get('resolusi', ''),
            UPLOAD_LOCATION = "storage/sctv",
            # COOKIES = get_channel_data('TVONESTREAMING')[0].get('cookies', ''),
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        #ENGINE_KEYS[16]
        GARUDASTREAMING = dict(
            ENVIRONMENT = "dev",
            # URLV1 = "https://www.beritasatu.com/livestream", OLD
            URL = "https://hgmtv.com:19360/garudatvlivestreaming/garudatvlivestreaming.m3u8",
            RESOLUTION = "1024x576",
            PLAYLIST = "01.m3u8",
            HOST_DIRECTORY = "https://hgmtv.com:19360/garudatvlivestreaming/",
            UPLOAD_LOCATION = "storage/garuda",
            HEADERS = {
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
        #ENGINE_KEYS[17]
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
        #ENGINE_KEYS[18]
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
        #ENGINE_KEYS[19]
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
        #ENGINE_KEYS[20]
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
        #ENGINE_KEYS[21]
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
        #ENGINE_KEYS[22]
        TVRISUMUTSTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "http://klik.tvri.go.id/",
            RESOLUTION = "640x360",
            # RESOLUTION = "480x240", #OLD
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://ott-balancer.tvri.go.id/live/eds/Sumut/hls/Sumut.m3u8",
            HOST_DIRECTORY_TS = "https://ott-balancer.tvri.go.id/live/eds/Sumut",
            UPLOAD_LOCATION = "storage/tvrisumut",
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
        #ENGINE_KEYS[23]
        TVRIYOGYASTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "http://klik.tvri.go.id/",
            RESOLUTION = "640x360",
            # RESOLUTION = "480x240", #OLD
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://ott-balancer.tvri.go.id/live/eds/Jogjakarta/hls/Jogjakarta.m3u8",
            HOST_DIRECTORY_TS = "https://ott-balancer.tvri.go.id/live/eds/Jogjakarta",
            UPLOAD_LOCATION = "storage/tvriyogya",
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
        #ENGINE_KEYS[24]
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
        #ENGINE_KEYS[25]
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
        #ENGINE_KEYS[26]
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
        #ENGINE_KEYS[27]
        JAWAPOSSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://63b2dc7196c38.streamlock.net:1937/JAWAPOSTVJKT/_definst_/myStream/",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "1280x720",
            UPLOAD_LOCATION = "storage/jawapos",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        #ENGINE_KEYS[28]
        PONTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://63b2dc7196c38.streamlock.net:1937/PONTV/_definst_/myStream/",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = None,
            UPLOAD_LOCATION = "storage/pontv",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
    )
    
        
        

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
            # ENGINE_KEYS[14]: ENGINE[ENGINE_KEYS[14]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[15]: ENGINE[ENGINE_KEYS[15]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[16]: ENGINE[ENGINE_KEYS[16]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[17]: ENGINE[ENGINE_KEYS[17]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[18]: ENGINE[ENGINE_KEYS[18]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[19]: ENGINE[ENGINE_KEYS[19]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[20]: ENGINE[ENGINE_KEYS[20]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[21]: ENGINE[ENGINE_KEYS[21]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[22]: ENGINE[ENGINE_KEYS[22]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[23]: ENGINE[ENGINE_KEYS[23]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[24]: ENGINE[ENGINE_KEYS[24]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[25]: ENGINE[ENGINE_KEYS[25]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[26]: ENGINE[ENGINE_KEYS[26]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[27]: ENGINE[ENGINE_KEYS[27]]["UPLOAD_LOCATION"],
        }
    )

    ### Notif channel mati ###
    OPSV2 = dict(
        TELE_TOKEN = "8213920361:AAEMpyChKoMGb_FHw5QNVI9xdySfjP-yrtk",
        TELE_CHAT_ID = "-1002147735635",
        TELEGRAM_MESSAGE_THREAD_ID = 3042,
        SEND_TIME = 60 * 60,
        STORAGE_PATH = {
            ENGINE_KEYS[0]: ENGINE[ENGINE_KEYS[0]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[1]: ENGINE[ENGINE_KEYS[1]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[2]: ENGINE[ENGINE_KEYS[2]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[3]: ENGINE[ENGINE_KEYS[3]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[4]: ENGINE[ENGINE_KEYS[4]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[5]: ENGINE[ENGINE_KEYS[5]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[6]: ENGINE[ENGINE_KEYS[6]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[7]: ENGINE[ENGINE_KEYS[7]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[8]: ENGINE[ENGINE_KEYS[8]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[9]: ENGINE[ENGINE_KEYS[9]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[10]: ENGINE[ENGINE_KEYS[10]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[11]: ENGINE[ENGINE_KEYS[11]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[12]: ENGINE[ENGINE_KEYS[12]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[13]: ENGINE[ENGINE_KEYS[13]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[14]: ENGINE[ENGINE_KEYS[14]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[15]: ENGINE[ENGINE_KEYS[15]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[16]: ENGINE[ENGINE_KEYS[16]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[17]: ENGINE[ENGINE_KEYS[17]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[18]: ENGINE[ENGINE_KEYS[18]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[19]: ENGINE[ENGINE_KEYS[19]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[20]: ENGINE[ENGINE_KEYS[20]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[21]: ENGINE[ENGINE_KEYS[21]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[22]: ENGINE[ENGINE_KEYS[22]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[23]: ENGINE[ENGINE_KEYS[23]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[24]: ENGINE[ENGINE_KEYS[24]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[25]: ENGINE[ENGINE_KEYS[25]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[26]: ENGINE[ENGINE_KEYS[26]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[27]: ENGINE[ENGINE_KEYS[27]]["UPLOAD_LOCATION"],
        }
    )
    
    ### restart docker ###
    OPSV3 = dict(
        TELE_TOKEN = "8213920361:AAEMpyChKoMGb_FHw5QNVI9xdySfjP-yrtk",
        TELE_CHAT_ID = "-897317690",
        SEND_TIME = 60 * 40,
        STORAGE_PATH = {
            ENGINE_KEYS[0]: ENGINE[ENGINE_KEYS[0]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[1]: ENGINE[ENGINE_KEYS[1]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[2]: ENGINE[ENGINE_KEYS[2]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[3]: ENGINE[ENGINE_KEYS[3]]["UPLOAD_LOCATION"],
            #ENGINE_KEYS[4]: ENGINE[ENGINE_KEYS[4]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[5]: ENGINE[ENGINE_KEYS[5]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[6]: ENGINE[ENGINE_KEYS[6]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[7]: ENGINE[ENGINE_KEYS[7]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[8]: ENGINE[ENGINE_KEYS[8]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[9]: ENGINE[ENGINE_KEYS[9]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[10]: ENGINE[ENGINE_KEYS[10]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[11]: ENGINE[ENGINE_KEYS[11]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[12]: ENGINE[ENGINE_KEYS[12]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[13]: ENGINE[ENGINE_KEYS[13]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[14]: ENGINE[ENGINE_KEYS[14]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[15]: ENGINE[ENGINE_KEYS[15]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[16]: ENGINE[ENGINE_KEYS[16]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[17]: ENGINE[ENGINE_KEYS[17]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[18]: ENGINE[ENGINE_KEYS[18]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[19]: ENGINE[ENGINE_KEYS[19]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[20]: ENGINE[ENGINE_KEYS[20]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[21]: ENGINE[ENGINE_KEYS[21]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[22]: ENGINE[ENGINE_KEYS[22]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[23]: ENGINE[ENGINE_KEYS[23]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[24]: ENGINE[ENGINE_KEYS[24]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[25]: ENGINE[ENGINE_KEYS[25]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[26]: ENGINE[ENGINE_KEYS[26]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[27]: ENGINE[ENGINE_KEYS[27]]["UPLOAD_LOCATION"],
    }
    )
    
    ### Server ###
    
    SOCKET_SERVER_JAWAPOS = dict(
        HOST = "12.12.12.68",
        PORT = 7171,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
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

    SOCKET_SERVER_NUSANTARA = dict(
        HOST = "12.12.12.67",
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
    
    SOCKET_SERVER_SCTV = dict(
        HOST = "12.12.12.59",
        PORT = 7171,
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

    SOCKET_SERVER_TVRISUMUT = dict(
        HOST = "12.12.12.64",
        PORT = 5752,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_TVRIYOGYA = dict(
        HOST = "12.12.12.63",
        PORT = 5453,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    SOCKET_SERVER_PONTV = dict(
        HOST = "12.12.12.73",
        PORT = 9191,
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

    # SOCKET_SERVER_NUSANTARA = dict(
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

    # SOCKET_SERVER_BERITASATU = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 7001,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

    # SOCKET_SERVER_PONTV = dict(
    #     HOST = "127.0.0.1",
    #     PORT = 9191,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

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