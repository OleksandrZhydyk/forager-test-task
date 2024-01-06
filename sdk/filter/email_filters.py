"""The module contains available emails filters."""

from typing import Iterable, List

from sdk.filter.base_filter import Filter
from sdk.models.domain_search_models import DomainSearchDataEmailsInput


class FirstNameFilter(Filter[DomainSearchDataEmailsInput]):
    """Represents a filter functionality for first_name field."""

    def __init__(self, first_name: str) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.first_name = first_name

    def apply(self, emails: Iterable[DomainSearchDataEmailsInput]) -> List[DomainSearchDataEmailsInput]:
        """
        Filter data by first_name parameter.

        :param emails: The data that should be filtered.
        :return: The filtered data.
        """
        return [email for email in emails if email.first_name == self.first_name]


class LastNameFilter(Filter[DomainSearchDataEmailsInput]):
    """Represents a filter functionality for last_name field."""

    def __init__(self, last_name: str) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.last_name = last_name

    def apply(self, emails: Iterable[DomainSearchDataEmailsInput]) -> List[DomainSearchDataEmailsInput]:
        """
        Filter data by last_name parameter.

        :param emails: The data that should be filtered.
        :return: The filtered data.
        """
        return [email for email in emails if email.last_name == self.last_name]


class ConfidenceMoreThanFilter(Filter[DomainSearchDataEmailsInput]):
    """Represents a filter functionality for confidence field."""

    def __init__(self, confidence: int) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.confidence = confidence

    def apply(self, emails: Iterable[DomainSearchDataEmailsInput]) -> List[DomainSearchDataEmailsInput]:
        """
        Filter data by confidence parameter.

        :param emails: The data that should be filtered.
        :return: The filtered data.
        """
        return [email for email in emails if email.confidence > self.confidence]


class ConfidenceLessThanFilter(Filter[DomainSearchDataEmailsInput]):
    """Represents a filter functionality for confidence field."""

    def __init__(self, confidence: int) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.confidence = confidence

    def apply(self, emails: Iterable[DomainSearchDataEmailsInput]) -> List[DomainSearchDataEmailsInput]:
        """
        Filter data by confidence parameter.

        :param emails: The data that should be filtered.
        :return: The filtered data.
        """
        return [email for email in emails if email.confidence < self.confidence]


class SeniorityFilter(Filter[DomainSearchDataEmailsInput]):
    """Represents a filter functionality for seniority field."""

    def __init__(self, seniority: str) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.seniority = seniority

    def apply(self, emails: Iterable[DomainSearchDataEmailsInput]) -> List[DomainSearchDataEmailsInput]:
        """
        Filter data by seniority parameter.

        :param emails: The data that should be filtered.
        :return: The filtered data.
        """
        return [email for email in emails if email.seniority == self.seniority]


class DepartmentFilter(Filter[DomainSearchDataEmailsInput]):
    """Represents a filter functionality for department field."""

    def __init__(self, department: str) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.department = department

    def apply(self, emails: Iterable[DomainSearchDataEmailsInput]) -> List[DomainSearchDataEmailsInput]:
        """
        Filter data by department parameter.

        :param emails: The data that should be filtered.
        :return: The filtered data.
        """
        return [email for email in emails if email.department == self.department]
