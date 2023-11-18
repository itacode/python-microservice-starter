import logging
import os

import connexion
from flask import Flask
from flask_compress import Compress
from flask_cors import CORS
from flask_request_id import RequestID

from app.config import settings
from app.exceptions.error_handlers import register_error_handlers

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def create_app() -> Flask:
    connexion_app = connexion.FlaskApp(__name__, specification_dir="./openapi/")
    flask_app: Flask = connexion_app.app

    connexion_app.add_api("api.oas.yml", validate_responses=False)

    CORS(flask_app)
    Compress(flask_app)

    # https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/
    # Maximum file size after which an upload is aborted: 1MB
    flask_app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024
    upload_folder = settings.UPLOAD_FOLDER
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Add a header named "X-Request-ID"
    RequestID(flask_app)

    register_error_handlers(flask_app)

    return flask_app
