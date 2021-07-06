import logging
import logging.config

# Get config from file 
logging.config.fileConfig('logging.conf')

# Using logger from config filwå
logger = logging.getLogger('simpleExample')
logger.debug('this is a bebug message')



logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    datefmt='%m/%d/%Y %H:%M:%S'
)

import helper

# levels of logging
logging.debug("This is a debug message")
logging.info("this is an info message")
# Just logs of warning, error and critical level are printed
# You need to config logging if you wanna print another levels of logging
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical error")

