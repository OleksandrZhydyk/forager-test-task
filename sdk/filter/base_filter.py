"""The module contains implementation of filtering."""

from typing import List

from sdk.models.domain_search_models import DomainSearchDataEmailsInput


class Filter:
    """Represent the required interface for all filters."""

    def apply(self, emails: List[DomainSearchDataEmailsInput]) -> List[DomainSearchDataEmailsInput]:
        """
        Represent the required interface method for applying filters.

        :param emails: The data that should be filtered.
        :return: The filtered data.
        """


class FilterChain:
    """Collect filters and implement apply filters functionality to the data."""

    def __init__(self):
        """Initialize FilterChain instance and storage for filters to apply."""
        self.filters = []

    def add_filter(self, filtr: Filter):
        """
        Add specified filter to self.filters storage.

        :param filtr: Needed filter, should be class Filter instance.
        :return: Current FilterChain class instance.
        """
        self.filters.append(filtr)
        return self

    def apply_all(self, emails: List[DomainSearchDataEmailsInput]) -> List[DomainSearchDataEmailsInput]:
        """
        Apply all filters from self.filter to the passed data.

        :param emails: Data to filter.
        :return: Filtered data.
        """
        for filtr in self.filters:
            emails = filtr.apply(emails)
        return emails
