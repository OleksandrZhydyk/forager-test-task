"""The module represents base class RequestParams that is parent for all request parameters typed objects."""

from pydantic.dataclasses import dataclass


@dataclass
class RequestParams(object):
    """Base :class: for all typed request parameters objects."""
