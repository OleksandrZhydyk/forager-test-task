"""The module contains implementation of filtering."""

from typing import Iterable, TypeVar

FilterGeneric = TypeVar('FilterGeneric')


class Filter(object):
    """Represent the required interface for all filters."""

    def apply(self, input_data: Iterable[FilterGeneric]) -> Iterable[FilterGeneric]:
        """
        Represent the required interface method for applying filters.

        :param input_data: The data that should be filtered.
        :return: The filtered data.
        """


class FilterChain(object):
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

    def apply_all(self, input_data: Iterable[FilterGeneric]) -> Iterable[FilterGeneric]:
        """
        Apply all filters from self.filter to the passed data.

        :param input_data: Data to filter.
        :return: Filtered data.
        """
        for filtr in self.filters:
            input_data = filtr.apply(input_data)
        return input_data
