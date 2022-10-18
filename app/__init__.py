import os

import connexion
from flask import Flask
from flask_compress import Compress
from flask_cors import CORS
from flask_request_id import RequestID

import app.config as app_config
from app.exceptions.error_handlers import register_error_handlers


def create_app():
    connexion_app = connexion.App(__name__, specification_dir="./openapi")
    flask_app: Flask = connexion_app.app

    connexion_app.add_api("api.oas.yml", validate_responses=False)

    CORS(flask_app)
    Compress(flask_app)

    # https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/
    # Maximum file size after which an upload is aborted: 1MB
    flask_app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024
    upload_folder = app_config.AppConfig.UPLOAD_FOLDER
    print(upload_folder)
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Add a header named "X-Request-ID"
    RequestID(flask_app)

    register_error_handlers(flask_app)

    return flask_app
