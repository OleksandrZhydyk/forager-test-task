"""Module for reusable methods for :class: RequestClient."""

from typing import Type

import requests

from sdk.exceptions import APIIncorrectRequestError
from sdk.models.response_dto.base_response_dto import BaseResponseDTO


def check_response_on_errors(res: requests.Response, response_dto: Type[BaseResponseDTO]) -> BaseResponseDTO | None:
    """
    Check response on errors.

    :param res: Response object of requests library.
    :param response_dto: Class container for response
    :return: Serialized response json or raise APIIncorrectRequestError if the errors exist.
    """
    if res.ok:
        return response_dto(**res.json())
    raise APIIncorrectRequestError(res.status_code, res.json())
