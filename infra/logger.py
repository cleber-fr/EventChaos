import logging
from datetime import datetime

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    timestamp_str = datetime.now().strftime('app_%d-%m-%Y_%H-%M-%S.log')
    file = logging.FileHandler(timestamp_str)
    file.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file)