"""The module represents request parameters structures for HunterIO API."""

from pydantic.dataclasses import dataclass

from sdk.models.request_dto.base_params import RequestParams


@dataclass
class EmailsByDomain(RequestParams):
    """Available search parameters for GET_EMAILS_BY_DOMAIN api route."""

    domain: str | None = None
    company: str | None = None
    limit: int | None = None
    offset: int | None = None


@dataclass
class VerifyEmail(RequestParams):
    """Available search parameters for VERIFY_EMAIL api route."""

    email: str
