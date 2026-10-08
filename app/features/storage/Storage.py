from abc import ABC, abstractmethod
from app.core.config import settings
from pathlib import Path

from fastapi import UploadFile


class Storage(ABC):
    storage_dir_root = Path(settings.storage_dir_root)
    @abstractmethod
    def store(self, file: UploadFile) -> str:
        pass