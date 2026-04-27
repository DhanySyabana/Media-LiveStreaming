import sys
import logging
import os
from datetime import datetime

# Add parent directory to path untuk imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from libs.DBConnection import DatabaseConnection

class DatabaseHandler(logging.Handler):
    """
    Custom logging handler untuk menyimpan error logs ke database
    """
    def __init__(self):
        super().__init__()
        self.setLevel(logging.ERROR)
    
    def emit(self, record):
        """
        Emit log record ke database
        """
        try:
            log_entry = self.format(record)
            timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
            
            query = """
            INSERT INTO streaming_logs (channel_name, log_text, detail_log, created_at, updated_at, source)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            channel_name = os.path.splitext(record.filename)[0]
            
            # Get log_text and detail from extra fields if provided
            log_text = getattr(record, 'log_text', None)
            detail = getattr(record, 'detail', None)
            
            if not log_text:
                log_text = f"{record.levelname}: {record.getMessage()}"[:255]
            
            if detail:
                detail_log = f"{log_entry} {detail}"
            else:
                detail_log = log_entry
            
            params = (
                channel_name,  # channel_name (file name without extension)
                log_text[:255],  # log_text (varchar 255)
                detail_log,  # detail_log
                timestamp,  # created_at
                timestamp,  # updated_at
                "REMOTE 1"  # source fixed text
            )
            
            DatabaseConnection.execute_insert(query, params)
        except Exception as e:
            # Jika ada error saat menyimpan ke database, print ke stderr
            print(f"Error saving log to database: {e}", file=sys.stderr)


class Loggers:

    def __init__(self, log_level = logging.DEBUG, log_handler_level = logging.INFO, save_error_to_db = True) -> None:
        self.log_level = log_level
        self.log_handler_level = log_handler_level
        self.save_error_to_db = save_error_to_db
        self.Run()
        super().__init__()

    def Run(self) -> None:
        root = logging.getLogger()
        root.setLevel(self.log_level)

        # Handler untuk console output
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(self.log_handler_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)
        
        # Handler untuk menyimpan error ke database
        if self.save_error_to_db:
            try:
                DatabaseConnection.init_connection_pool()
                db_handler = DatabaseHandler()
                db_handler.setFormatter(formatter)
                root.addHandler(db_handler)
            except Exception as e:
                print(f"Warning: Could not initialize database logging: {e}", file=sys.stderr)
        
        return None