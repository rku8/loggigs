# logger_manager.py

import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """
    Creates a logger with the specified name, log file, and log level.
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers
    if not logger.handlers:
        os.makedirs('logs', exist_ok=True)  # Create logs folder if not exists

        file_handler = logging.FileHandler(f'logs/{log_file}')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)

        logger.addHandler(file_handler)

    return logger
