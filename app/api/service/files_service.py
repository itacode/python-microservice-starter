import os
from dataclasses import dataclass

import app.config as app_config


class FilesService:

    @dataclass
    class FindResult:
        files: list[str]

    def find(self):
        upload_folder = app_config.AppConfig.UPLOAD_FOLDER
        files: list[str]

        for (_, _, filenames) in os.walk(upload_folder):
            files = [*filenames]
            # break at the first level
            break

        find_result = self.FindResult(files=files)

        return find_result

    @dataclass
    class DeleteByNameParams:
        name: str

    def delete_by_name(self, params: DeleteByNameParams):
        upload_folder = app_config.AppConfig.UPLOAD_FOLDER
        file_path = os.path.join(upload_folder, params.name)

        if os.path.exists(file_path):
            os.remove(file_path)
