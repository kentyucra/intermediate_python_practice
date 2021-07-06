import logging

# Will create a logger with the name of the module
logger = logging.getLogger(__name__)

# If we do not want to propagate the BasicConfig from parent set propagate to False
logger.propagate = False

logger.info("Hello from helper")

# Handlers help us to redirect our log to the correct output (file, STDOUT, etc)
logger_handle = logging.getLogger(__name__)
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Set level and format for every handler
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger_handle.addHandler(stream_h)
logger_handle.addHandler(file_h)

logger_handle.warning('this is a warning')
logger_handle.error('this is an error')

# Best practice is to create a 'logging.conf' file that will have all configuration for logging
