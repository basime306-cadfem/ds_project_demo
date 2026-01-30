import os
import sys

import logging

log_frmt = "[%(asctime)s | %(levelname)s | %(message)s]"

log_folder = "log"
log_path = os.path.join(log_folder, "logging.log")

os.makedirs(log_folder, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=log_frmt,
    handlers=[logging.FileHandler(log_path),
              logging.StreamHandler(sys.stdout)]
    
)

logger = logging.getLogger("DS Logger")