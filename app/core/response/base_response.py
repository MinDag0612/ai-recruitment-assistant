from typing import Any

from pydantic import BaseModel

class BaseResponse(BaseModel):
    error: str | None = None
    msg: str
    data: Any = None
