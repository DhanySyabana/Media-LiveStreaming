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
        INEWSSTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "https://www.rctiplus.com/tv/inews",
            RESOLUTIONV1 = "640x360",
            # HOST_DIRECTORYV1 = "https://inewscdn.rctiplus.id", #OLD
            # HOST_DIRECTORYV1 = "https://icdn.rctiplus.id", #NEW
            HOST_DIRECTORYV1 = "https://inews-linier.rctiplus.id", #NEW
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
        CNNSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://live.cnnindonesia.com/livecnn/smil:cnntv.smil",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = "storage/cnn",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
            }
        ),
        # KOMPASSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.youtube.com/watch?v=DOOrIxw5xOw",
        #     QUALITY = "360p",
        #     UPLOAD_LOCATION = "storage/kompas",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        #     }
        # ),
        KOMPASSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://op-group1-swiftservehd-1.dens.tv/s/s104", 
            # RESOLUTION = "640x360",
            RESOLUTION = "640x480",
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://op-group1-swiftservehd-1.dens.tv/s/s104",
            UPLOAD_LOCATION = "storage/kompas",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
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
        # METROTVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     # HOST_DIRECTORY = "https://edge.medcom.id/live-edge/smil:metro.smil",
        #     HOST_DIRECTORY = "https://edge.medcom.id/live-edge/smil:mgnch.smil",
        #     PLAYLIST = "playlist.m3u8",
        #     RESOLUTION = "426x240",
        #     UPLOAD_LOCATION = "storage/metro",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
        #     }
        # ),
        # METROTVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     # URL = "https://www.youtube.com/watch?v=qA7_9fcCbZ8",
        #     URL = "https://www.youtube.com/watch?v=-CwtcKDaaLA",
        #     QUALITY = "360p",
        #     UPLOAD_LOCATION = "storage/metro",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        #     }
        # ),
        METROTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://op-group1-swiftservehd-1.dens.tv/h/h12", 
            # RESOLUTION = "640x360",
            RESOLUTION = "480x360",
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://op-group1-swiftservehd-1.dens.tv/h/h12",
            UPLOAD_LOCATION = "storage/metro",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
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
        # METROTVSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URLV1 = "https://www.indihometv.com/livetv/metrotv",
        #     RESOLUTIONV1 = "640x360",
        #     PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/joss/133/metrotv1080/playlist.m3u8",
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
        CNBCSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://live.cnbcindonesia.com/livecnbc/smil:cnbctv.smil",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = "storage/cnbc",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
            }
        ),
        # IDXSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URLV1 = "https://www.indihometv.com/livetv/idx",
        #     RESOLUTIONV1 = "640x360",
        #     # PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/joss/134/idx/playlist.m3u8",
        #     # PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/atm/HLS-10s/idx/playlist.m3u8", #old
        #     # PLAYLIST_DIRECTORYV1 = "https://cdn10jtedge.indihometv.com/atm/hlsv3/idx/playlist.m3u8",
        #     PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/atm/hlsv3/idx/playlist.m3u8",
        #     HOST_DIRECTORYV1 = "https://cdnkbl2.indihometv.com/joss/134/idx",
        #     UPLOAD_LOCATION = "storage/idx",
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
        IDXSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.youtube.com/watch?v=QB3oe7Q31F0",
            QUALITY = "360p",
            UPLOAD_LOCATION = "storage/idx",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        # TVONESTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     URL = "https://www.youtube.com/watch?v=yNKvkPJl-tg",
        #     QUALITY = "360p",
        #     UPLOAD_LOCATION = "storage/tvone",
        #     HEADERS = {
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        #     }
        # ),
        TVONESTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://op-group1-swiftservehd-1.dens.tv/h/h40", 
            # RESOLUTION = "640x360",
            RESOLUTION = "480x360",
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://op-group1-swiftservehd-1.dens.tv/h/h40",
            UPLOAD_LOCATION = "storage/tvone",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
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
        # BERITASATUSTREAMING = dict(
        #     ENVIRONMENT = "dev",
        #     # URLV1 = "https://www.beritasatu.com/livestream", OLD
        #     # https://b1world.beritasatumedia.com/Beritasatu/B1World_manifest.m3u8
        #     # URLV1 = "https://op-group1-swiftservehd-1.dens.tv/h/h210",
        #     URLV1 = "https://beritasatu-poc.secureswiftcontent.com/han/lineardemo/rtmp10008hls/srtoutput",
        #     RESOLUTION = "640x360",
        #     PLAYLIST = "manifest.m3u8",
        #     # HOST_DIRECTORY = "https://op-group1-swiftservehd-1.dens.tv/h/h210",
        #     HOST_DIRECTORY = "https://beritasatu-poc.secureswiftcontent.com/han/lineardemo/rtmp10008hls/srtoutput",
        #     UPLOAD_LOCATION = "storage/beritasatu",
        #     HEADERS = {
        #         'origin': 'https://beritasatu.tv',
        #         'referer': 'https://beritasatu.tv/',
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
        BERITASATUSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.vidio.com/live/18280-berita-satu",
            RESOLUTION = "640x360",
            # 18280
            PATH_URL =  "https://etslive-v3-vidio-com-tokenized.akamaized.net",
            PLAYLIST = "B1News_320x240.m3u8",
            HOST_DIRECTORY = " https://etslive-v3-vidio-com-tokenized.akamaized.net/live/18280/master.m3u8",
            UPLOAD_LOCATION = "storage/beritasatu",
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
        TVRISTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "https://www.dens.tv/tv-local/watch/17/tvri",
            RESOLUTION = "480x360",
            # RESOLUTION = "480x240", #OLD
            PLAYLIST = "02.m3u8",
            HOST_DIRECTORY = "https://op-group1-swiftservesd-1.dens.tv/s/s11/index.m3u8",
            HOST_DIRECTORY_TS = "https://op-group1-swiftservesd-1.dens.tv/s/s11/",
            UPLOAD_LOCATION = "storage/tvri",
            HEADERS = {
                'origin': 'https://www.dens.tv',
                'referer': 'https://www.dens.tv/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
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
        TRANSTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://video.detik.com/transtv/smil:transtv.smil",
            # HOST_DIRECTORY ="https://pullstream.transtv.co.id/livettv",
            # https://pullstream.transtv.co.id/livettv/
            # PLAYLIST = "livestreamttv.m3u8",
            # PLAYLIST = "playlist.m3u8",
            PLAYLIST = "chunklist_w835097260_b744100_sleng.m3u8",
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
            URLV1 = "https://www.indihometv.com/livetv/mncnews",
            RESOLUTIONV1 = "640x360",
            # PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/joss/134/mncnews/playlist.m3u8",
            PLAYLIST_DIRECTORYV1 = "https://streaming.indihometv.com/atm/hlsv3/mncnews/playlist.m3u8",
            HOST_DIRECTORYV1 = "https://cdnkbl2.indihometv.com/joss/134/mncnews",
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
        #     # URLV1 = "https://www.beritasatu.com/livestream", OLD
        #     # https://d43tg978oium5.cloudfront.net/out/v1/65c9a0ca766c4f6a9deef31e8b67ec07/index_4.m3u
        #     URLV1 = "https://d43tg978oium5.cloudfront.net/out/v1/65c9a0ca766c4f6a9deef31e8b67ec07",
        #     RESOLUTION = "320x240",
        #     PLAYLIST = "index_4.m3u8",
        #     HOST_DIRECTORY = "https://d43tg978oium5.cloudfront.net/out/v1/65c9a0ca766c4f6a9deef31e8b67ec07",
        #     UPLOAD_LOCATION = "storage/mnc",
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
        SEATODAYSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.vidio.com/live/7687-sea-today",
            RESOLUTION = "640x360",
            PLAYLIST = "B1News_320x240.m3u8",
            # HOST_DIRECTORY = "https://etslive-app.vidio.com/live/7687/master.m3u8",
            # HOST_DIRECTORY = "https://etslive-2-vidio-com.akamaized.net/live/7687/master.m3u8",
            HOST_DIRECTORY = "https://etslive-v3-vidio-com-tokenized.akamaized.net/live/7687/master.m3u8",
            PATH_URL =  "https://etslive-v3-vidio-com-tokenized.akamaized.net",
            UPLOAD_LOCATION = "storage/seatoday",
            HEADERS = {
                'origin': 'https://www.vidio.com',
                'referer': 'https://www.vidio.com/live/7687-sea-today',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'sec-ch-ua': 'Chromium";v="120", "Not.A/Brand";v="8", "Chromium";v="120',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'accept': '*/*',
                # 'Sentry-Trace:': 'd48f7af7266e439cae66bd4b829ccac4-bf0f4948846e015d-0',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
        ),
        SCTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://op-group1-swiftservehd-1.dens.tv/h/h217", 
            RESOLUTION = "640x360",
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://op-group1-swiftservehd-1.dens.tv/h/h217",
            PATH_URL =  "https://etslive-v3-vidio-com-tokenized.akamaized.net",
            UPLOAD_LOCATION = "storage/sctv",
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
        GARUDASTREAMING = dict(
            ENVIRONMENT = "dev",
            # URLV1 = "https://www.beritasatu.com/livestream", OLD
            URLV1 = "https://hgmtv.com:19360/garudatvlivestreaming/garudatvlivestreaming.m3u8",
            RESOLUTION = "640x360",
            PLAYLIST = "01.m3u8",
            HOST_DIRECTORY = "https://hgmtv.com:19360/garudatvlivestreaming",
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
    )

    ENGINE_KEYS = list(ENGINE.keys())

    OPS = dict(
        TELE_TOKEN = "5932299476:AAG4YmekrMEVMHaljj01xOqZX1LuBpjEyBw",
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
        TELE_TOKEN = "5988797823:AAEPdu06BRbmL4TWCqGY9-m8gLmr-XRJtH8",
        TELE_CHAT_ID = "-897317690",
        SEND_TIME = 60 * 60,
        STORAGE_PATH = {
            ENGINE_KEYS[0]: ENGINE[ENGINE_KEYS[0]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[1]: ENGINE[ENGINE_KEYS[1]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[2]: ENGINE[ENGINE_KEYS[2]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[3]: ENGINE[ENGINE_KEYS[3]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[4]: ENGINE[ENGINE_KEYS[4]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[5]: ENGINE[ENGINE_KEYS[5]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[6]: ENGINE[ENGINE_KEYS[6]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[7]: ENGINE[ENGINE_KEYS[7]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[8]: ENGINE[ENGINE_KEYS[8]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[9]: ENGINE[ENGINE_KEYS[9]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[10]: ENGINE[ENGINE_KEYS[10]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[11]: ENGINE[ENGINE_KEYS[11]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[12]: ENGINE[ENGINE_KEYS[12]]["UPLOAD_LOCATION"],
            ENGINE_KEYS[13]: ENGINE[ENGINE_KEYS[13]]["UPLOAD_LOCATION"],
            # ENGINE_KEYS[14]: ENGINE[ENGINE_KEYS[14]]["UPLOAD_LOCATION"],
        }
    )
    
    ### restart docker ###
    OPSV3 = dict(
        TELE_TOKEN = "5988797823:AAEPdu06BRbmL4TWCqGY9-m8gLmr-XRJtH8",
        TELE_CHAT_ID = "-897317690",
        SEND_TIME = 60 * 40,
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

    # SOCKET_SERVER_MNC = dict(
    #     HOST = "12.12.12.32",
    #     PORT = 7676,
    #     MAX_CONNECTION = 4,
    #     BUFFER_SIZE = 1024
    # )

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
        HOST = "12.12.12.39",
        PORT = 7171,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    
    SOCKET_SERVER_TVRIBALI = dict(
        HOST = "12.12.12.42",
        PORT = 7172,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    SOCKET_SERVER_GARUDA = dict(
        HOST = "12.12.12.51",
        PORT = 5151,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )
    SOCKET_SERVER_NUSANTARA = dict(
        HOST = "12.12.12.44",
        PORT = 5251,
        MAX_CONNECTION = 4,
        BUFFER_SIZE = 1024
    )

    ### end Server ###

    ### Local ###

    # SOCKET_SERVER_NUSANTARA = dict(
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
    #     PORT = 7010,
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

