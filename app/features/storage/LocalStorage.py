from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.features.storage.Storage import Storage


class LocalStorage(Storage):
    def __init__(self, storage_domain: str) -> None:
        self.storage_dir = self.storage_dir_root / storage_domain
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        
    def store(self, file: UploadFile) -> str:
        extension = Path(file.filename or "").suffix.lower()
        file_id = uuid4()

        filename = f"{file_id}{extension}"
        file_path = Path(self.storage_dir) / filename

        with file_path.open("wb") as buffer:
            while chunk := file.file.read(1024 * 1024):
                buffer.write(chunk)

        return str(file_path)
