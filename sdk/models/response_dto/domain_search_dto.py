"""The module represents data structures of response object on domain_search request."""

from typing import List

from pydantic import Field
from pydantic.dataclasses import dataclass

from sdk.models.response_dto.base_response_dto import BaseResponseDTO


@dataclass
class DomainSearchSourcesResponse(object):
    """Represents data structure of source that is related to the email."""

    domain: str
    uri: str
    extracted_on: str
    last_seen_on: str
    still_on_page: bool


@dataclass
class DomainSearchVerificationResponse(object):
    """Represents data structure of verification key of domain_search data."""

    date: str | None
    status: str | None


@dataclass(kw_only=True)
class DomainSearchDataEmailsResponse(object):
    """Represents data structure of emails from domain_search."""

    email: str = Field(..., alias='value')
    type: str
    confidence: int
    sources: List[DomainSearchSourcesResponse] | None
    first_name: str | None
    last_name: str | None
    position: str | None
    seniority: str | None
    department: str | None
    linkedin: str | None
    twitter: str | None
    phone_number: str | int | None
    verification: DomainSearchVerificationResponse | None


@dataclass
class DomainSearchDataResponse(object):
    """Represents data structure of domain_search."""

    domain: str | None
    disposable: bool
    webmail: bool
    accept_all: bool
    pattern: str | None
    organization: str | None
    description: str | None
    industry: str | None
    twitter: str | None
    facebook: str | None
    linkedin: str | None
    instagram: str | None
    youtube: str | None
    technologies: List[str]
    country: str | None
    state: str | None
    city: str | None
    postal_code: str | None
    street: str | None
    emails: List[DomainSearchDataEmailsResponse]
    linked_domains: List[str]


@dataclass
class DomainSearchMetaParamsResponse(object):
    """Represents search meta params of domain_search."""

    domain: str | None
    company: str | None
    type: str | None
    seniority: str | None
    department: str | None


@dataclass(kw_only=True)
class DomainSearchMetaResponse(object):
    """Represents metadata of domain_search."""

    found_emails_qty: int = Field(..., alias='results')
    limit: int
    offset: int
    request_params: DomainSearchMetaParamsResponse = Field(..., alias='params')


@dataclass
class DomainSearchResponse(BaseResponseDTO):
    """Main dataclass for representation of domain_search response."""

    domain_email_data: DomainSearchDataResponse = Field(..., alias='data')
    meta: DomainSearchMetaResponse = Field(..., alias='meta')
