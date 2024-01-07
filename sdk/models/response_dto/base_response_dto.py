"""The module represents base class for all response objects."""
from pydantic.dataclasses import dataclass


@dataclass
class BaseResponseDTO(object):
    """Base class for response DTOs."""
