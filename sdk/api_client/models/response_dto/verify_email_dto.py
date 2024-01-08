"""The module represents data structures of response object on verify_email request."""

from typing import List

from pydantic import Field
from pydantic.dataclasses import dataclass

from sdk.api_client.models.response_dto.base_response_dto import BaseResponseDTO


@dataclass
class EmailVerifierSourcesResponse(object):
    """Represents data structure of source that is related to the email."""

    domain: str
    uri: str
    extracted_on: str
    last_seen_on: str
    still_on_page: bool


@dataclass(kw_only=True)
class EmailVerifierDataResponse(object):
    """Represents metaparams of email_verification response."""

    status: str
    request_result: str = Field(..., alias='result')
    _deprecation_notice: str
    score: int
    email: str
    regexp: bool
    gibberish: bool
    disposable: bool
    webmail: bool
    mx_records: bool
    smtp_server: bool
    smtp_check: bool
    accept_all: bool
    block: bool
    sources: List[EmailVerifierSourcesResponse]


@dataclass
class EmailVerifierMetaParamsResponse(object):
    """Represents metaparams of email_verification response."""

    email: str


@dataclass
class EmailVerifierMetaResponse(object):
    """Represents metaparams of email_verification response."""

    request_meta_params: EmailVerifierMetaParamsResponse = Field(..., alias='params')


@dataclass(kw_only=True)
class EmailVerifierResponse(BaseResponseDTO):
    """Main dataclass for representation of email_validation response."""

    full_email_data: EmailVerifierDataResponse = Field(..., alias='data')
    meta: EmailVerifierMetaResponse
