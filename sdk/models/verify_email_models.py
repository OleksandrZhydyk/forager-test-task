"""The module represents data structures of response object on verify_email request."""

from typing import List

from pydantic.dataclasses import dataclass


@dataclass
class EmailVerifierSourcesInput:
    """Represents data structure of source that is related to the email."""

    domain: str
    uri: str
    extracted_on: str
    last_seen_on: str
    still_on_page: bool


@dataclass
class EmailVerifierDataInput:
    """Represents metaparams of email_verification response."""

    status: str
    result: str
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
    sources: List[EmailVerifierSourcesInput]


@dataclass
class EmailVerifierMetaParamsInput:
    """Represents metaparams of email_verification response."""

    email: str


@dataclass
class EmailVerifierMetaInput:
    """Represents metaparams of email_verification response."""

    params: EmailVerifierMetaParamsInput


@dataclass
class EmailVerifierInput:
    """Main dataclass for representation of email_validation response."""

    data: EmailVerifierDataInput
    meta: EmailVerifierMetaInput