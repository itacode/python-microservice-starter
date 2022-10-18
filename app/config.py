import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


def getenv_or_raise(key: str) -> str:
    """Get the environment variable or raise exception if it doesn't exists"""
    result: Optional[str] = os.getenv(key)
    if result is None:
        raise Exception(f"environment variable doesn't exist: {key}")
    return result


class AppConfig:
    UPLOAD_FOLDER: str = getenv_or_raise("UPLOAD_FOLDER")


class DBConfig:
    MY_SERVICE_DB_URL: str = (
        f"mysql+pymysql://{getenv_or_raise('MY_SERVICE_DB_USER')}"
        + f":{getenv_or_raise('MY_SERVICE_DB_PASSWORD')}"
        + f"@{getenv_or_raise('MY_SERVICE_DB_HOST')}"
        + f":{getenv_or_raise('MY_SERVICE_DB_PORT')}"
        + f"/{getenv_or_raise('MY_SERVICE_DB_NAME')}"
    )
