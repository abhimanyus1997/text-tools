import os
import sys
import logging
from logging.handlers import RotatingFileHandler


def configure_logger():
    """Configure logger settings."""
    logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
    log_dir = "logs"
    log_filepath = os.path.join(log_dir, "running_logs.log")
    os.makedirs(log_dir, exist_ok=True)

    # Set up formatter
    formatter = logging.Formatter(logging_str)

    # Set up file handler with rotating capability
    file_handler = RotatingFileHandler(
        log_filepath, maxBytes=10*1024*1024, backupCount=5)
    file_handler.setFormatter(formatter)

    # Set up stream handler for console output
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    # Configure root logger
    logging.basicConfig(level=logging.INFO, handlers=[
                        file_handler, stream_handler])


def get_logger(name):
    """Get logger with specified name."""
    return logging.getLogger(name)
