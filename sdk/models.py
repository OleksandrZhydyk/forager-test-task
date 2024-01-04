from typing import List, Any

from pydantic.dataclasses import dataclass
from sdk.filter import Filter, FilterChain


@dataclass
class DomainSearchSourcesInput:
    domain: str
    uri: str
    extracted_on: str
    last_seen_on: str
    still_on_page: bool


@dataclass
class DomainSearchVerificationInput:
    date: str | None
    status: str | None


@dataclass
class DomainSearchDataEmailsInput:
    value: str
    type: str
    confidence: int
    sources: List[DomainSearchSourcesInput] | None
    first_name: str | None
    last_name: str | None
    position: str | None
    seniority: str | None
    department: str | None
    linkedin: str | None
    twitter: str | None
    phone_number: str | int | None
    verification: DomainSearchVerificationInput | None


@dataclass
class DomainSearchDataInput:
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
    emails: List[DomainSearchDataEmailsInput]
    linked_domains: List[str]


@dataclass
class DomainSearchMetaParamsInput:
    domain: str | None
    company: str | None
    type: str | None
    seniority: str | None
    department: str | None


@dataclass
class DomainSearchMetaInput:
    results: int
    limit: int
    offset: int
    params: DomainSearchMetaParamsInput


@dataclass
class DomainSearchInput:
    data: DomainSearchDataInput
    meta: DomainSearchMetaInput

    def get_data(self) -> DomainSearchDataInput:
        return self.data

    def get_meta(self) -> DomainSearchMetaInput:
        return self.meta

    def get_items(self, *filters: Filter) -> List[DomainSearchDataEmailsInput]:
        filter_chain = FilterChain()
        data = self.data.emails
        for filter in filters:
            filter_chain.add_filter(filter)
        return filter_chain.apply_all(data)

    def get_item(self, email: str) -> DomainSearchDataEmailsInput:
        for user_data in self.data.emails:
            if user_data.value == email:
                return user_data

    def update_item(self, email: str, update_field: str, update_value: Any) -> DomainSearchDataEmailsInput:
        for key, user_data in enumerate(self.data.emails):
            if hasattr(user_data, update_field):
                if user_data.value == email:
                    setattr(self.data.emails[key], update_field, update_value)
                    return user_data
            else:
                raise ValueError(f"{update_field} doesn't exist in {user_data}")

    def delete_item(self, email: str) -> bool | None:
        for key, user_data in enumerate(self.data.emails):
            if user_data.value == email:
                del self.data.emails[key]
                return True
        raise ValueError(f"Item with {email} doesn't exist")

    def create_item(self, email: DomainSearchDataEmailsInput):
        self.data.emails.append(email)


@dataclass
class EmailVerifierSourcesInput:
    domain: str
    uri: str
    extracted_on: str
    last_seen_on: str
    still_on_page: bool


@dataclass
class EmailVerifierDataInput:
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
    email: str


@dataclass
class EmailVerifierMetaInput:
    params: EmailVerifierMetaParamsInput


@dataclass
class EmailVerifierInput:
    data: EmailVerifierDataInput
    meta: EmailVerifierMetaInput
