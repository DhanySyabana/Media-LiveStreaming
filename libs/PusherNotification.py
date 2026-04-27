import pusher
import sys
import os
from datetime import datetime

# Add parent directory to path untuk imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ==============================
# KONFIGURASI PUSHER
# ==============================
PUSHER_APP_ID = "2096075"  # Ganti dengan App ID Anda
PUSHER_KEY = "94a9c1084a700c48f455"
PUSHER_SECRET = "7b8a6fe9f3f72421109d"  # Ganti dengan Secret Anda
PUSHER_CLUSTER = "ap1"

# Inisialisasi Pusher Client
try:
    pusher_client = pusher.Pusher(
        app_id=PUSHER_APP_ID,
        key=PUSHER_KEY,
        secret=PUSHER_SECRET,
        cluster=PUSHER_CLUSTER,
        ssl=True
    )
    PUSHER_ENABLED = True
except Exception as e:
    print(f"⚠️  Pusher initialization failed: {e}")
    PUSHER_ENABLED = False


def trigger_error_notification(channel_name, log_text):
    """
    Trigger notifikasi error real-time via Pusher
    
    Args:
        channel_name (str): Nama channel (e.g., 'BantenTV', 'CNBCIndonesia')
        log_text (str): Pesan error singkat (max 255 characters)
        detail (str, optional): Detail log lengkap
    
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    if not PUSHER_ENABLED:
        print(f"   ⚠️  Pusher is not enabled. Notification for {channel_name} could not be sent.")
        return False
    
    try:
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        pusher_client.trigger(
            'Notification',  # Channel name (sesuai Laravel)
            'Event-notification',  # Event name (sesuai Laravel)
            {
                'notif': {
                    'channel_name': channel_name,
                    'log_text': log_text[:255],  # Ensure max 255 chars
                    'source': 'SIPUTRI',
                    'created_at': created_at
                }
            }
        )
        
        print(f"   📡 Pusher error notification triggered for {channel_name}")
        return True
        
    except Exception as e:
        print(f"   ⚠️  Failed to trigger Pusher notification: {e}")
        return False
