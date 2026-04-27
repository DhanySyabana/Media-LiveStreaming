import time
import logging

def countdown_sleep(total_seconds: int = 300, interval: int = 1) -> None:
    remaining = total_seconds
    while remaining > 0:
        mins, secs = divmod(remaining, 60)
        logging.info(f"Loop countdown remaining: {mins:02d}:{secs:02d}")
        to_sleep = interval if remaining >= interval else remaining
        time.sleep(to_sleep)
        remaining -= to_sleep

if __name__ == "__main__":
    # contoh pemanggilan: 10 detik
    countdown_sleep(total_seconds=10, interval=1)
