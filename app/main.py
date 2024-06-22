import logging
import logging.config
import os

import connexion
from flask_compress import Compress
from flask_cors import CORS

from app.config import logging_config, settings
from app.exceptions.error_handlers import register_error_handlers

logging.config.dictConfig(logging_config)


app = connexion.App(__name__, specification_dir="./openapi/")
app.add_api("api.oas.yml", validate_responses=False)

flask_app = app.app
CORS(flask_app)
Compress(flask_app)

register_error_handlers(app)

# https://flask.palletsprojects.com/en/3.0.x/patterns/fileuploads/
# Maximum file size after which an upload is aborted: 1MB
flask_app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024
upload_folder = settings.UPLOAD_FOLDER
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
