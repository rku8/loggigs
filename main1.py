from logginfr import setup_logger
from loguru import logger as loguru_logger

# Setup structured log file loggers
app_logger = setup_logger('app', 'app.log')
error_logger = setup_logger('error', 'error.log', level='ERROR')

import sys

# Remove the default loguru handler
loguru_logger.remove()

# Add terminal (stdout) with formatting
loguru_logger.add(
    sink=sys.stdout,
    format="<green>{time:HH:mm:ss}</green>| <magenta>({file.name}:{line} - {function})</magenta> | <level>{level}</level> | "
           "<cyan>{message}</cyan>",
    level="INFO"
)

# Use loguru to print to terminal (user-friendly)
def fx():
    loguru_logger.info("This is a user-friendly log message.")
    loguru_logger.debug("This is a debug message, not shown in terminal by default.")
    loguru_logger.error("This is an error message, also shown in terminal.")
fx()
# Log messages using the structured loggers
loguru_logger.info("🚀 Starting the application...")
loguru_logger.success("✅ Service started successfully.")
loguru_logger.warning("⚠️  This is a warning shown to user.")
loguru_logger.error("❌ An error occurred but it's handled.")
