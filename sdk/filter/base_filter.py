"""The module contains implementation of filtering."""

from abc import ABC, abstractmethod
from typing import Generic, Iterable, List, TypeVar

FilterGeneric = TypeVar('FilterGeneric')


class Filter(ABC, Generic[FilterGeneric]):
    """Represent the required interface for all filters."""

    @abstractmethod
    def apply(self, input_data: Iterable[FilterGeneric]) -> List[FilterGeneric]:
        """
        Represent the required interface method for applying filters.

        :param input_data: The data that should be filtered.
        :return: The filtered data.
        """


class FilterChain(object):
    """Collect filters and implement apply filters functionality to the data."""

    def __init__(self) -> None:
        """Initialize FilterChain instance and storage for filters to apply."""
        self.filters: List[Filter] = []

    def add_filter(self, filtr: Filter) -> 'FilterChain':
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
