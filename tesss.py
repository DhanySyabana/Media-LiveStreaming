import streamlink

# URL video YouTube
youtube_url = "https://www.youtube.com/watch?v=nfgnpM28xDA"

# Path ke file cookies.txt
cookies_file = "cookies.txt"

# URL proxy (misalnya: http://username:password@proxyserver:port)
proxy_url = "socks5://trkcytfh:xtfqu68rlqwr@207.228.7.241:7423"

# Menggunakan cookies untuk login
session = streamlink.Streamlink()

# Menambahkan cookies ke session Streamlink
session.set_option("http-cookies", cookies_file)

# Menambahkan proxy ke session Streamlink
session.set_option("http-proxy", proxy_url)

# Mendapatkan stream yang tersedia
streams = session.streams(youtube_url)

# Menampilkan stream yang tersedia
if streams:
    for stream_quality, stream_url in streams.items():
        print(f"Stream tersedia dengan kualitas: {stream_quality}, URL: {stream_url}")
else:
    print("Tidak ada stream yang tersedia.")
