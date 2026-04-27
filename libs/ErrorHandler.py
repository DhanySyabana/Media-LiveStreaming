def get_error_message(status_code: int) -> str:
    """Get error message based on HTTP status code.
    
    Args:
        status_code: HTTP status code
        
    Returns:
        Error message description
    """
    error_messages = {
        400: "Bad Request - Permintaan tidak valid",
        403: "URL tidak aktif",
        404: "URL tidak ditemukan",
        410: "Konten sudah dihapus",
        429: "Terlalu banyak permintaan",
        500: "Server error - Masalah pada server",
        502: "Bad Gateway - Server tidak merespons",
        503: "Service Unavailable - Layanan tidak tersedia",
        504: "Gateway Timeout - Server tidak merespons"
    }
    return error_messages.get(status_code, f"HTTP Error {status_code}")


def get_exception_message(exception: Exception) -> str:
    """Get error message based on exception type.
    
    Args:
        exception: Exception object
        
    Returns:
        Error message description
    """
    exception_type = type(exception).__name__
    exception_str = str(exception).lower()
    
    # Map exception types to messages
    exception_messages = {
        "timeout": "Connection timeout - Koneksi timeout",
        "connectionerror": "Connection error - Gagal terhubung ke server",
        "readtimeout": "Read timeout - Server tidak merespons dengan cepat",
        "connecttimeout": "Connect timeout - Gagal menghubungi server",
        "httpconnectionpool": "Connection pool error - Masalah koneksi",
        "retryerror": "Retry error - Gagal setelah beberapa kali percobaan",
        "sslerror": "SSL error - Masalah SSL/TLS",
        "urlrequired": "URL required - URL tidak valid",
    }
    
    # Check exception type
    for exc_type, message in exception_messages.items():
        if exc_type.lower() in exception_type.lower():
            return message
    
    # Check exception string for keywords
    if "timeout" in exception_str:
        return "Connection timeout - Koneksi timeout"
    elif "connection" in exception_str:
        return "Connection error - Gagal terhubung ke server"
    elif "refused" in exception_str:
        return "Connection refused - Server menolak koneksi"
    elif "reset" in exception_str:
        return "Connection reset - Koneksi direset oleh server"
    
    # Default message
    return f"Exception - {exception_type}: {str(exception)[:100]}"
