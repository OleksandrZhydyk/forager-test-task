"""Module for reusable methods for :class: RequestClient."""
from typing import Any, Dict

import requests

from sdk.exceptions import APIIncorrectRequestError


def check_response_on_errors(res: requests.Response) -> Dict[str, Any] | None:
    """
    Check response on errors.

    :param res: Response object og requests library.
    :return: Serialized response json or raise APIIncorrectRequestError if the errors exist.
    """
    if res.ok:
        return res.json()
    raise APIIncorrectRequestError(res.status_code, res.json())
