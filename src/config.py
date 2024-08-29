from datetime import datetime, timedelta
from dynaconf import Dynaconf
import logging


settings = Dynaconf(
    settings_files=['settings.toml'],
    secrets=['.secrets.toml'],
    load_dotenv=True,
    environments=True
)