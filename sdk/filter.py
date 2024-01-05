from typing import TypeVar

T = TypeVar('T')


class Filter:
    """Represent the required interface for all filters."""

    def apply(self, data: T) -> T:
        """
        Represent the required interface method for applying filters.

        :param data: The data that should be filtered.
        :return: The filtered data.
        """
        ...


class FirstNameFilter(Filter):
    """Represents a filter functionality for first_name field."""

    def __init__(self, first_name: str) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.first_name = first_name

    def apply(self, data: T) -> T:
        """
        Filter data by first_name parameter.

        :param data: The data that should be filtered.
        :return: The filtered data.
        """
        return [item for item in data if item.first_name == self.first_name]


class LastNameFilter(Filter):
    """Represents a filter functionality for last_name field."""

    def __init__(self, last_name: str) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.last_name = last_name

    def apply(self, data: T) -> T:
        """
        Filter data by last_name parameter.

        :param data: The data that should be filtered.
        :return: The filtered data.
        """
        return [item for item in data if item.last_name == self.last_name]


class ConfidenceMoreThanFilter(Filter):
    """Represents a filter functionality for confidence field."""

    def __init__(self, confidence: int) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.confidence = confidence

    def apply(self, data: T) -> T:
        """
        Filter data by confidence parameter.

        :param data: The data that should be filtered.
        :return: The filtered data.
        """
        return [item for item in data if item.confidence > self.confidence]


class ConfidenceLessThanFilter(Filter):
    """Represents a filter functionality for confidence field."""

    def __init__(self, confidence: int) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.confidence = confidence

    def apply(self, data: T) -> T:
        """
        Filter data by confidence parameter.

        :param data: The data that should be filtered.
        :return: The filtered data.
        """
        return [item for item in data if item.confidence < self.confidence]


class SeniorityFilter(Filter):
    """Represents a filter functionality for seniority field."""

    def __init__(self, seniority: str) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.seniority = seniority

    def apply(self, data: T) -> T:
        """
        Filter data by seniority parameter.

        :param data: The data that should be filtered.
        :return: The filtered data.
        """
        return [item for item in data if item.seniority == self.seniority]


class DepartmentFilter(Filter):
    """Represents a filter functionality for department field."""

    def __init__(self, department: str) -> None:
        """Initialize class Filter instance and store filter parameter."""
        self.department = department

    def apply(self, data: T) -> T:
        """
        Filter data by department parameter.

        :param data: The data that should be filtered.
        :return: The filtered data.
        """
        return [item for item in data if item.department == self.department]


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

    def apply_all(self, data: T) -> T:
        """
        Apply all filters from self.filter to the passed data.

        :param data: Data to filter.
        :return: Filtered data.
        """
        for filtr in self.filters:
            data = filtr.apply(data)
        return data
