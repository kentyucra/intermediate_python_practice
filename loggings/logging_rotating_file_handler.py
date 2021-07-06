import logging
import time
from logging.handlers import RotatingFileHandler
# You can use TimeRotatingFileHandler that rotate the files based on time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log1, app.log2, ...
# Once the app.log_i is full (2KM) it copy the values to app.log_i+1 
handler_size = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)

# every 5 seconds a new file is created
# values used in when: s = second, m = minutes, h = hours, d = days, midning
handler_time = TimedRotatingFileHandler('time_test.log', when='s', interval=5, backupCount=5)

logger.addHandler(handler_time)
for i in range(1000):
    logger.info(f"hello world {i}")
    time.sleep(5)
