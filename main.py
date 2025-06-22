# main.py

from logginfr import setup_logger
import logging

# Initialize multiple loggers
app_logger = setup_logger('app', 'app.log')
error_logger = setup_logger('error', 'error.log', level=logging.ERROR)
service_logger = setup_logger('service', 'service.log')
backend_logger = setup_logger('backend', 'backend.log')

# Logging examples
app_logger.info("Application started successfully.")
error_logger.error("An error occurred in the application.")
service_logger.info("Service X initialized.")
backend_logger.warning("Backend connection is slow.")
