import os
from pathlib import Path

from pydantic import BaseModel

import app.config as app_config


class FilesService:
    class FindResult(BaseModel):
        files: list[str]

    def find(self) -> FindResult:
        upload_folder = app_config.AppConfig.UPLOAD_FOLDER
        (_, _, filenames) = next(os.walk(upload_folder))
        find_result = self.FindResult(files=filenames)
        return find_result

    class DeleteByNameParams(BaseModel):
        name: str

    def delete_by_name(self, params: DeleteByNameParams) -> None:
        upload_folder = app_config.AppConfig.UPLOAD_FOLDER
        file_path = Path(upload_folder, params.name)
        if file_path.exists():
            file_path.unlink()
