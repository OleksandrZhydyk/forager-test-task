"""The module represents data structures of response object on domain_search request."""

from typing import Any, List

from pydantic.dataclasses import dataclass

from sdk.filter.base_filter import Filter, FilterChain


@dataclass
class DomainSearchSourcesInput:
    """Represents data structure of source that is related to the email."""

    domain: str
    uri: str
    extracted_on: str
    last_seen_on: str
    still_on_page: bool


@dataclass
class DomainSearchVerificationInput:
    """Represents data structure of verification key of domain_search data."""

    date: str | None
    status: str | None


@dataclass
class DomainSearchDataEmailsInput:
    """Represents data structure of emails from domain_search."""

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
    emails: List[DomainSearchDataEmailsInput]
    linked_domains: List[str]


@dataclass
class DomainSearchMetaParamsInput:
    """Represents search meta params of domain_search."""

    domain: str | None
    company: str | None
    type: str | None
    seniority: str | None
    department: str | None


@dataclass
class DomainSearchMetaInput:
    """Represents metadata of domain_search."""

    results: int
    limit: int
    offset: int
    params: DomainSearchMetaParamsInput


@dataclass
class DomainSearchInput:
    """Main dataclass for representation of domain_search response."""

    data: DomainSearchDataInput
    meta: DomainSearchMetaInput

    def get_items(self, *filters: Filter) -> List[DomainSearchDataEmailsInput]:
        """
        Allow to filter received emails by specified filters.

        :param filters: The instances by Filter class.
        :return: The list of filtered emails.
        """
        filter_chain = FilterChain()
        data = self.data.emails
        for filtr in filters:
            filter_chain.add_filter(filtr)
        return filter_chain.apply_all(data)

    def get_item(self, email: str) -> DomainSearchDataEmailsInput:
        """
        Get all data by specified email.

        :param email: By which email the data will be searched.
        :return: Email data object.
        """
        for user_data in self.data.emails:
            if user_data.value == email:
                return user_data

    def update_item(self, email: str, update_field: str, update_value: Any) -> DomainSearchDataEmailsInput:
        """
        Update specified field in email data object.

        :param email: By which email the data will be updated.
        :param update_field: Which field in email data will be updated.
        :param update_value: Which new value will be assigned to update_field.
        :return: Updated email data object.
        """
        for key, user_data in enumerate(self.data.emails):
            if self._is_obj_has_attr(user_data, update_field):
                if user_data.value == email:
                    setattr(self.data.emails[key], update_field, update_value)
                    return user_data
            else:
                raise ValueError(
                    "{update_field} doesn't exist in {user_data}".format(
                        update_field=update_field, user_data=user_data,
                    ),
                )

    def delete_item(self, email: str) -> bool | None:
        """
        Delete the specified email data object.

        :param email: By which email the data will be deleted.
        :return:
        """
        for key, user_data in enumerate(self.data.emails):
            if user_data.value == email:
                del self.data.emails[key]
                return True
        raise ValueError("Item with {email} doesn't exist".format(email=email))

    def create_item(self, email_obj_data: DomainSearchDataEmailsInput) -> None:
        """
        Create email data object.

        :param email_obj_data: The data that is needed to represent email data object.
        :return: None.
        """
        self.data.emails.append(email_obj_data)

    def _is_obj_has_attr(self, email_obj: DomainSearchDataEmailsInput, attr: str) -> bool:
        try:
            getattr(email_obj, attr)
        except AttributeError:
            return False
        return True
