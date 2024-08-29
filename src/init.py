import copy
import logging
from datetime import datetime, timedelta
from telegram.ext import Application
from telegram.warnings import PTBUserWarning
from warnings import filterwarnings

from config import settings
import handlers
import utils


def setup_logging() -> None:
    # Logging
    logging_level = logging.DEBUG if settings.DEBUG else logging.INFO
    logging.basicConfig(filename=settings.LOG_PATH, level=logging_level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.getLogger('apscheduler').setLevel(logging.WARNING)
    logging.getLogger('httpx').setLevel(logging.WARNING)
    # Debugging
    filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)


async def post_init(app: Application) -> None:
    """Initializes bot with data and its tasks."""
    pass


def add_handlers(app: Application) -> None:
    # Error handler
    app.add_error_handler(handlers.error)
    # Debug & business logic handlers
    app.add_handlers(handlers.all)
