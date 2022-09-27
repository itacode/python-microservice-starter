import os

from pydantic import BaseModel

import app.config as app_config


class FilesService:
    class FindResult(BaseModel):
        files: list[str]

    def find(self) -> FindResult:
        upload_folder = app_config.AppConfig.UPLOAD_FOLDER
        files: list[str]

        for (_, _, filenames) in os.walk(upload_folder):
            files = [*filenames]
            # break at the first level
            break

        find_result = self.FindResult(files=files)

        return find_result

    class DeleteByNameParams(BaseModel):
        name: str

    def delete_by_name(self, params: DeleteByNameParams) -> None:
        upload_folder = app_config.AppConfig.UPLOAD_FOLDER
        file_path = os.path.join(upload_folder, params.name)

        if os.path.exists(file_path):
            os.remove(file_path)
