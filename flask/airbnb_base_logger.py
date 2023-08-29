import logging
import datetime


logger = logging
log_file = "airbnb" + str(datetime.datetime.today().date()) + ".log"
logger.basicConfig(
    # Standard format
    format="%(asctime)s - %(message)s",
    level=logging.INFO,
    handlers=[logger.FileHandler(log_file), logger.StreamHandler()],
)
