from typing import Any

from app.core import BaseResponse


def success_response(
    data: Any = None,
    msg: str = "Success",
) -> BaseResponse:
    return BaseResponse(
        error=None,
        msg=msg,
        data=data,
    )
