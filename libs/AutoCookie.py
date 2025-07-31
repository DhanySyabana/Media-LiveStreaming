import asyncio
import json
import logging
import platform
import subprocess
import time
import os
import signal
from playwright.async_api import async_playwright

# === KONFIGURASI ===
CDP_PORT = 9222
COOKIE_FILE_PATH = "cookie.json"
USER_DATA_DIR = "/tmp/chrome-session"  # Bebas, pastikan writeable

cookie_keys = [
    "SID", "HSID", "SSID", "SAPISID", "APISID", "LOGIN_INFO", "PREF",
    "__Secure-1PSID", "__Secure-1PAPISID", "__Secure-1PSIDCC",
    "__Secure-3PSID", "__Secure-3PAPISID", "__Secure-3PSIDCC",
    "SIDCC", "VISITOR_INFO1_LIVE", "YSC", "__Secure-1PSIDTS", "__Secure-3PSIDTS"
]

# === LOGGING ===
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

# === LAUNCH CHROME ===
def launch_chrome():
    chrome_path = "/usr/bin/google-chrome"

    cmd = [
        chrome_path,
        f"--remote-debugging-port={CDP_PORT}",
        f"--user-data-dir={USER_DATA_DIR}",
        "--no-first-run",
        "--no-default-browser-check"
    ]

    logging.info("🚀 Menjalankan Chrome dengan remote debugging...")
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)
        logging.info("✅ Chrome berhasil dijalankan.")
        return proc
    except Exception as e:
        logging.error(f"❌ Gagal menjalankan Chrome: {e}")
        return None

# === AMBIL COOKIE ===
async def fetch_cookies():
    async with async_playwright() as p:
        try:
            logging.info("🔌 Menghubungkan ke Chrome (CDP)...")
            browser = await p.chromium.connect_over_cdp(f"http://127.0.0.1:{CDP_PORT}")
        except Exception as e:
            logging.error(f"❌ Gagal konek ke Chrome: {e}")
            return

        contexts = browser.contexts
        if not contexts:
            logging.error("❌ Tidak ada tab aktif ditemukan di Chrome.")
            await browser.close()
            return

        context = contexts[0]
        cookies = await context.cookies()

        youtube_cookies = [
            c for c in cookies
            if ".youtube.com" in c["domain"] and c["name"] in cookie_keys
        ]

        if not youtube_cookies:
            logging.error("❌ Tidak ada cookie dari domain .youtube.com ditemukan.")
            await browser.close()
            return

        cookie_dict = {c["name"]: c["value"] for c in youtube_cookies}
        cookie_header = "; ".join([f"{k}={v}" for k, v in cookie_dict.items()])

        result = {
            "cookies": cookie_dict,
            "cookie_header": cookie_header,
            "timestamp_created": time.strftime("%Y-%m-%d %H:%M:%S"),
            "valid": True,
            "source": "youtube_engine"
        }

        os.makedirs(os.path.dirname(COOKIE_FILE_PATH), exist_ok=True)
        with open(COOKIE_FILE_PATH, "w") as f:
            json.dump(result, f, indent=4)

        logging.info("✅ Cookie berhasil diambil dan disimpan ke cookies/cookie.json")
        await browser.close()

# === MAIN ENTRY POINT ===
def main():
    logging.info("🔥 Mulai proses pengambilan cookie YouTube...")
    chrome_proc = launch_chrome()

    if not chrome_proc:
        return

    try:
        asyncio.run(fetch_cookies())
    finally:
        logging.info("🛑 Menutup Chrome...")
        try:
            os.kill(chrome_proc.pid, signal.SIGKILL)
        except Exception as e:
            logging.warning(f"Gagal membunuh proses Chrome: {e}")

if __name__ == "__main__":
    main()
