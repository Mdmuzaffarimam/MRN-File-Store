import logging
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "bot.log"
PORT = '8080'
OWNER_ID = 6139759254
MSG_EFFECT = 5046509860389126442

# VPLink URL Shortener Configuration
VPLINK_API_TOKEN = "1b8e94e97189da28b35fcab06c0850bd92569751"
VPLINK_API_URL = "https://arolinks.com/api"

# URL Shortener Providers Configuration
URL_SHORTENERS = {
    'vplink': {
        'name': 'arolinks',
        'api_url': 'https://arolinks.com/api',
        'api_token': AROLINKS_API_TOKEN,
        'format': 'text',
        'active': True
    }
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
