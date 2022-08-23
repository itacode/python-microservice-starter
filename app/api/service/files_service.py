import os
from typing import List

import app.config as app_config


class FilesService:

    def findFiles(self):
        upload_folder = app_config.AppConfig.UPLOAD_FOLDER
        files: List[str]

        for (_, _, filenames) in os.walk(upload_folder):
            files = [*filenames]
            # break at the first level
            break

        return {"files": files}

    def delete_files_name(self, *, name: str):
        upload_folder = app_config.AppConfig.UPLOAD_FOLDER
        file_path = os.path.join(upload_folder, name)

        if os.path.exists(file_path):
            os.remove(file_path)
