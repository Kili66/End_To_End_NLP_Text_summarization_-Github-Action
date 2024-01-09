import os
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs" # create logs directory
log_filepath = os.path.join(log_dir,"running_logs.log")  # create log file running.log
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),  # show logs in file
        logging.StreamHandler(sys.stdout)   # show logs in terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger")