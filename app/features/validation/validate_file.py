from pathlib import Path
from typing import Annotated

from fastapi import File, HTTPException, UploadFile

from app.core.response.exception_type import InvalidFileExtension



class ValidateFile:
    ALLOWED_EXTENSIONS = {".pdf", ".docx"}

    @staticmethod
    def validate_upload_file(
        file: Annotated[UploadFile, File(...)]
    ) -> UploadFile:
        extension = Path(file.filename or "").suffix.lower()

        if extension not in ValidateFile.ALLOWED_EXTENSIONS:
            raise InvalidFileExtension

        return file