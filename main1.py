from logginfr import setup_logger
from loguru import logger as loguru_logger

# Setup structured log file loggers
app_logger = setup_logger('app', 'app.log')
error_logger = setup_logger('error', 'error.log', level='ERROR')

# Use loguru to print to terminal (user-friendly)
loguru_logger.info("🚀 Starting the application...")
loguru_logger.success("✅ Service started successfully.")
loguru_logger.warning("⚠️  This is a warning shown to user.")
loguru_logger.error("❌ An error occurred but it's handled.")
