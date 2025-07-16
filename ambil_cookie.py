import browser_cookie3


cookie_keys = [
    "SID", "HSID", "SSID", "SAPISID", "APISID", "LOGIN_INFO", "PREF",
    "__Secure-1PSID", "__Secure-1PAPISID", "__Secure-1PSIDCC",
    "__Secure-3PSID", "__Secure-3PAPISID", "__Secure-3PSIDCC",
    "SIDCC", "VISITOR_INFO1_LIVE", "YSC", "__Secure-1PSIDTS", "__Secure-3PSIDTS"
]

def get_youtube_cookies_str():
    cj = browser_cookie3.chrome(domain_name='.youtube.com')
    cookie_dict = {c.name: c.value for c in cj if c.name in cookie_keys}
    cookie_str = ";".join([f"{k}={v}" for k, v in cookie_dict.items()])
    return cookie_str

if __name__ == "__main__":
    cookie_str = get_youtube_cookies_str()
    print("===== COOKIE HEADER UNTUK SCRAPER =====")
    print(cookie_str)
    with open("youtube_cookie_header.txt", "w") as f:
        f.write(cookie_str)
    print("Cookie berhasil diexport ke youtube_cookie_header.txt")
