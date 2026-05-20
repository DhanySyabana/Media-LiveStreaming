class Config(object):

    ENGINE = dict(

        #ENGINE_KEYS[0]
        INEWSSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.rctiplus.com/tv/inews",
            RESOLUTIONV1 = "640x360",
            # HOST_DIRECTORYV1 = "https://inews-linier.rctiplus.id", #old
            HOST_DIRECTORYV1 = "https://icdn.rctiplus.id/anevia1", #NEW
            RESOLUTION = "640x360",
            # HOST_DIRECTORY = "https://midcache.rctiplus.com/live",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\inews",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\cnn",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\kompas",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),

        #ENGINE_KEYS[3]
        METROTVSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.youtube.com/watch?v=-CwtcKDaaLA",
            ID_CHANNEL = "UCzl0OrB3-ehunyotIQvK77A",
            QUALITY = "360p",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\metro",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),

        #ENGINE_KEYS[4]
        CNBCSTREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://live.cnbcindonesia.com/livecnbc/smil:cnbctv.smil",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\cnbc",
            HEADERS = {
                'referer': 'https://www.cnbcindonesia.com/',
                'origin': 'https://www.cnbcindonesia.com',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
        
        #ENGINE_KEYS[5]
        IDXSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.youtube.com/watch?v=8dNAAe5dcqQ",
            QUALITY = "360p",
            ID_CHANNEL = "UCQA6NejSxQguRkD3L8eXHzA",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\idx",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
       
        #ENGINE_KEYS[6]
        TVONESTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.youtube.com/watch?v=yNKvkPJl-tg&feature=youtu.be",
            QUALITY = "360p",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\tvone",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        
        #ENGINE_KEYS[7]
        BERITASATUSTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "https://www.dens.tv/tv-local/watch/131/berita-satu",
            RESOLUTION = "640x360",
            # RESOLUTION = "1024x576",
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://op-group1-swiftservehd-1.dens.tv/h/h209",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\beritasatu",
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
        
        #ENGINE_KEYS[8]
        TVRISTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "http://klik.tvri.go.id/",
            RESOLUTION = "640x360",
            # RESOLUTION = "480x240", #OLD
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://ott-balancer.tvri.go.id/live/eds/Nasional/hls/Nasional.m3u8",
            HOST_DIRECTORY_TS = "https://ott-balancer.tvri.go.id/live/eds/Nasional",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\tvri",
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
        
        #ENGINE_KEYS[9]
        RCTISTREAMING = dict(
            ENVIRONMENT = "dev",
            URLV1 = "https://www.rctiplus.com/tv/rcti",
            RESOLUTIONV1 = "640x360",
            # HOST_DIRECTORYV1 = "https://1s1.rctiplus.id", #NEW 26 Januari 2026
            RESOLUTION = "426x240",
            HOST_DIRECTORYV1 = "https://rcti-linier.rctiplus.id", #old
            # HOST_DIRECTORYV1 = "https://rcdn.rctiplus.id", #NEW
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\rcti",
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
       
        #ENGINE_KEYS[10]
        TRANS7STREAMING = dict(
            ENVIRONMENT = "dev",
            HOST_DIRECTORY = "https://video.detik.com/trans7/smil:trans7.smil",
            #HOST_DIRECTORY ="https://pullstream.transtv.co.id/livettv",
            # https://pullstream.transtv.co.id/livettv/
            #PLAYLIST = "livestreamttv.m3u8",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\trans7",
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
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = "640x360",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\transtv",
            HEADERS = {
                'origin': 'https://20.detik.com',
                'referer': 'https://20.detik.com/',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        ),
       
        #ENGINE_KEYS[12]
        NUSANTARATVSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://op-group1-swiftservehd-1.dens.tv/h/h37", 
            RESOLUTION = "1280x720",
            PLAYLIST = "index.m3u8",
            HOST_DIRECTORY = "https://op-group1-swiftservehd-1.dens.tv/h/h37",
            PATH_URL =  "https://etslive-v3-vidio-com-tokenized.akamaized.net",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\nusantaratv",
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
        
        #ENGINE_KEYS[13]
        MNCSTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://www.youtube.com/watch?v=BpT2mGUdTN0",
            QUALITY = "360p",
            ID_CHANNEL = "UCGfXjFgIUUTUUlzdG6BenXA",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\mnc",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\seatoday",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\sctv",
            # COOKIES = get_channel_data('TVONESTREAMING')[0].get('cookies', ''),
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
        #ENGINE_KEYS[16]
        GARUDASTREAMING = dict(
            ENVIRONMENT = "dev",
            URL = "https://hgmtv.com:19360/garudatvlivestreaming/",
            RESOLUTION = "1280x720",
            PLAYLIST = "garudatvlivestreaming.m3u8",
            HOST_DIRECTORY = "https://hgmtv.com:19360/garudatvlivestreaming/",
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\garuda",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\tvribali",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\tvrijatim",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\tvrikalbar",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\tvrilampung",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\tvrisulsel",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\tvrisumut",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\tvriyogya",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\jaktv",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\bantentv",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\dhoho",
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
            HOST_DIRECTORY = "https://63b2dc7196c38.streamlock.net:1937/JAWAPOSTVSBY/_definst_/myStream/",
            PLAYLIST = "playlist.m3u8",
            RESOLUTION = '1280x720',
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\jawapos",
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
            UPLOAD_LOCATION = r"D:\Medmon\storage\New folder\pontv",
            HEADERS = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        ),
    )