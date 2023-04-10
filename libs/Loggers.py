import sys
import logging

class Loggers:

    def __init__(self, log_level = logging.DEBUG, log_handler_level = logging.INFO) -> None:
        self.log_level = log_level
        self.log_handler_level = log_handler_level
        self.Run()
        super().__init__()

    def Run(self) -> None:
        root = logging.getLogger()
        root.setLevel(self.log_level)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(self.log_handler_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)
        return None