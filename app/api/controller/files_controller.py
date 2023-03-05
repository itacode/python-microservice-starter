from pathlib import Path

from flask import request
from werkzeug.utils import secure_filename

import app.config as app_config
from app.api.service.files_service import FilesService
from app.exceptions.application_errors import ParameterError

_files_service = FilesService()


def get_files_name():
    result = _files_service.find()

    return result.dict()


def upload_files():
    # https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/
    # check if the post request has the file part
    if "file" not in request.files:
        raise ParameterError("No file part")
    file = request.files["file"]
    # If the user does not select a file raises error
    if file.filename == "":
        raise ParameterError("No selected file")
    if file:
        filename = secure_filename(file.filename)
        file.save(Path(app_config.AppConfig.UPLOAD_FOLDER, filename))

        return "OK"


def delete_files_name(name: str):
    params = _files_service.DeleteByNameParams(name=name)
    _files_service.delete_by_name(params=params)

    return "OK"
