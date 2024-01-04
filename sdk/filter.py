from typing import TypeVar


T = TypeVar('T')


class Filter:
    def apply(self, data: T) -> T:
        pass


class FirstNameFilter(Filter):
    def __init__(self, first_name: str) -> None:
        self.first_name = first_name

    def apply(self, data: T) -> T:
        return [item for item in data if item.first_name == self.first_name]


class LastNameFilter(Filter):
    def __init__(self, last_name: str) -> None:
        self.last_name = last_name

    def apply(self, data: T) -> T:
        return [item for item in data if item.last_name == self.last_name]


class ConfidenceMoreThanFilter(Filter):
    def __init__(self, confidence: int) -> None:
        self.confidence = confidence

    def apply(self, data: T) -> T:
        return [item for item in data if item.confidence > self.confidence]


class ConfidenceLessThanFilter(Filter):
    def __init__(self, confidence: int) -> None:
        self.confidence = confidence

    def apply(self, data: T) -> T:
        return [item for item in data if item.confidence < self.confidence]


class SeniorityFilter(Filter):
    def __init__(self, seniority: str) -> None:
        self.seniority = seniority

    def apply(self, data: T) -> T:
        return [item for item in data if item.seniority == self.seniority]


class DepartmentFilter(Filter):
    def __init__(self, department: str) -> None:
        self.department = department

    def apply(self, data: T) -> T:
        return [item for item in data if item.department == self.department]


class FilterChain:
    def __init__(self):
        self.filters = []

    def add_filter(self, filtr: Filter):
        self.filters.append(filtr)
        return self

    def apply_all(self, data: T) -> T:
        for filtr in self.filters:
            data = filtr.apply(data)
        return data
