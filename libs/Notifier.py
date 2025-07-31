import requests
import logging
import datetime
def send_telegram_alert(
    token: str,
    chat_id: str,
    topic_id: int,
    scraper_name: str,
    fallback_message: str
) -> None:
    """
    Kirim alert Telegram ketika error tertentu terjadi (stream off, cookie expired, dll)
    Format pesan selalu dalam bentuk list notifikasi standar.
    """
    if "UNPLAYABLE" in fallback_message.upper():
        icon = "🚧"
    elif "LOGIN_REQUIRED" in fallback_message.upper() or "COOKIE" in fallback_message.upper() or "PROTECTED" in fallback_message.upper():
        icon = "🍪"
    else:
        icon = "🚧"
    text = (
    "🛑 *SERVER - SIPUTRI* 🛑\n"
    "━━━━━━━━━━━━━━━━━━━━━━━\n"
    f"📺 STREAMING : {scraper_name.upper()} \n"
    f"❗ WARN : {icon} {fallback_message}\n"
    "🕒 WAKTU  : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    "━━━━━━━━━━━━━━━━━━━━━━━\n"
    "🔔 *Tolong Segera Dicek!*\n"
)

    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "message_thread_id": topic_id
        }
        response = requests.post(url, data=payload)

        if response.status_code != 200:
            logging.warning(f"[NOTIFIER] Gagal kirim ke Telegram: {response.text}")
        else:
            logging.info("[NOTIFIER] Pesan berhasil dikirim ke Telegram.")
    except Exception as e:
        logging.error(f"[NOTIFIER] Gagal kirim alert Telegram: {e}")
