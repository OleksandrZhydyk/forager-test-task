"""The module represents base class for all request payload objects."""

from pydantic.dataclasses import dataclass


@dataclass
class RequestPayload(object):
    """Base :class: for all typed request payload objects."""
