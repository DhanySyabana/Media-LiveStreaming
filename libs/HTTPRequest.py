import logging
import requests
from requests.adapters import HTTPAdapter

class HTTPRequest:

    def __init__(self, method, url, headers, body = None, retry_count=3, retry_backoff=0.5) -> None:
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body
        self.retry_count = retry_count
        self.retry_backoff = retry_backoff
        super().__init__()

    def Hit(self) -> None:
        try:
            session = requests.Session()
            retry = Retry(connect=self.retry_count, backoff_factor=self.retry_backoff)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)

            response = session.request(self.method, self.url, headers=self.headers, data=self.body)
            return response
        except requests.exceptions.RequestException as e:
            logging.error(F"Error HTTPRequest: {e}")
            return None