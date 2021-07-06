import logging
import traceback
try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    # exc_info get the traceback information
    logging.error(e, exc_info=True)
except:
    # Use this when you do not know the exception and want to print the traceback
    logging.error("The error is %s", traceback.format_exc())
