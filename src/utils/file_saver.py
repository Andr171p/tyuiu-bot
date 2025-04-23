import uuid
from pathlib import Path
from fastapi import UploadFile

from src.settings import BASE_DIR
from src.misc.file_writers import write_file


FILES_DIR: Path = BASE_DIR / "files"


class FileSaver:
    def __init__(self, file: UploadFile) -> None:
        self._file = file

    def _get_file_path(self) -> Path:
        file_name = self._file.filename
        file_extension = file_name.split(".")[-1]
        file_id = str(uuid.uuid4())
        file_path = FILES_DIR / "texts" / f"{file_name}_{file_id}.txt"
        if file_extension == "png":
            file_path = FILES_DIR / "photo" / f"{file_name}_{file_id}.png"
        if file_extension == "jpeg":
            file_path = FILES_DIR / "photo" / f"{file_name}_{file_id}.jpeg"
        return file_path

    async def save(self) -> Path:
        file_path = self._get_file_path()
        data = await self._file.read()
        await write_file(file_path, data)
        return file_path
