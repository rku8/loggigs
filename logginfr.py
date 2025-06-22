import logging
import json
import os

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "file": record.pathname,
            "line": record.lineno,
            "function": record.funcName,
        }

        # Include custom fields if provided
        if hasattr(record, 'user_id'):
            log_record['user_id'] = record.user_id
        if hasattr(record, 'request_id'):
            log_record['request_id'] = record.request_id

        return json.dumps(log_record)

def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        os.makedirs('logs', exist_ok=True)

        # File handler
        file_handler = logging.FileHandler(f'logs/{log_file}')
        file_handler.setLevel(level)

        # Console handler
        # console_handler = logging.StreamHandler()
        # console_handler.setLevel(level)

        # JSON formatter
        formatter = JsonFormatter(datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)
        # console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        # logger.addHandler(console_handler)

    return logger
