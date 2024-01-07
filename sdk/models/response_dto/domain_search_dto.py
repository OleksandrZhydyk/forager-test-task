"""The module represents data structures of response object on domain_search request."""

from typing import Any, Iterable, List

from pydantic import Field
from pydantic.dataclasses import dataclass

from sdk.filter.base_filter import Filter, FilterChain
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

    def get_items(self, *filters: Filter) -> Iterable[DomainSearchDataEmailsResponse]:
        """
        Allow to filter received emails by specified filters.

        :param filters: The instances by Filter class.
        :return: The list of filtered emails.
        """
        filter_chain = FilterChain()
        emails = self.domain_email_data.emails
        for filtr in filters:
            filter_chain.add_filter(filtr)
        return filter_chain.apply_all(emails)

    def get_item(self, email: str) -> DomainSearchDataEmailsResponse | None:
        """
        Get all data by specified email.

        :param email: By which email the data will be searched.
        :return: Email data object.
        """
        for user_data in self.domain_email_data.emails:
            if user_data.email == email:
                return user_data
        return None

    def update_item(self, email: str, update_field: str, update_value: Any) -> DomainSearchDataEmailsResponse:
        """
        Update specified field in email data object.

        :param email: By which email the data will be updated.
        :param update_field: Which field in email data will be updated.
        :param update_value: Which new value will be assigned to update_field.
        :return: Updated email data object.
        """
        for key, user_data in enumerate(self.domain_email_data.emails):
            if self._is_obj_has_attr(user_data, update_field):
                if user_data.email == email:
                    setattr(self.domain_email_data.emails[key], update_field, update_value)
                    return user_data
            else:
                raise ValueError(
                    "{update_field} doesn't exist in {user_data}".format(
                        update_field=update_field, user_data=user_data,
                    ),
                )
        raise ValueError(
            "{email} doesn't exist in received emails.".format(email=email),
        )

    def delete_item(self, email: str) -> bool | None:
        """
        Delete the specified email data object.

        :param email: By which email the data will be deleted.
        :return:
        """
        for key, user_data in enumerate(self.domain_email_data.emails):
            if user_data.email == email:
                self.domain_email_data.emails.pop(key)
                return True
        raise ValueError("Item with {email} doesn't exist".format(email=email))

    def create_item(self, email_obj_data: DomainSearchDataEmailsResponse) -> None:
        """
        Create email data object.

        :param email_obj_data: The data that is needed to represent email data object.
        :return: None.
        """
        self.domain_email_data.emails.append(email_obj_data)

    def _is_obj_has_attr(self, email_obj: DomainSearchDataEmailsResponse, attr: str) -> bool:
        try:
            getattr(email_obj, attr)
        except AttributeError:
            return False
        return True