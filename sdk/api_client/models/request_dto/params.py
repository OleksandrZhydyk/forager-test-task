"""The module represents request parameters structures for HunterIO API."""

from pydantic.dataclasses import dataclass

from sdk.api_client.models.request_dto.base_params import RequestParams


@dataclass
class EmailsByDomain(RequestParams):
    """Available search parameters for GET_EMAILS_BY_DOMAIN api route."""

    domain: str | None = None
    company: str | None = None
    limit: int | None = None
    offset: int | None = None

    def __post_init__(self) -> None:
        """Call after all data was assign to the field and runs a validation."""
        self.validate_fields()

    def validate_fields(self) -> None:
        """Validate if at least one, company or domain field has value."""
        if not self.domain and not self.company:
            raise ValueError('At least one of domain or company should have a value.')


@dataclass
class VerifyEmail(RequestParams):
    """Available search parameters for VERIFY_EMAIL api route."""

    email: str
