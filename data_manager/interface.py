"""The module represents DataManager for data saving and manipulating."""

from abc import ABC, abstractmethod
from typing import Any


class BaseManager(ABC):
    """The class represents methods for data saving and manipulating."""

    @abstractmethod
    def add_data(self, key: str, data_to_store: Any) -> Any:
        """
        Add data in the storage.

        :param key: Unique value that corresponds to a specific data.
        :param data_to_store: Data to store.
        :return: None or KeyAlreadyExistsError.
        """

    @abstractmethod
    def read(self, key: str) -> Any:
        """
        Get data by specified key.

        :param key: Unique value that corresponds to a specific data.
        :return: Saved value or KeyNotFoundError.
        """

    @abstractmethod
    def update(self, key: str, new_value: Any) -> Any:
        """
        Update stored value in storage.

        :param key: Unique value that corresponds to a specific data.
        :param new_value: Provided updated data to store.
        :return: None or KeyNotFoundError.
        """

    @abstractmethod
    def delete(self, key: str) -> str:
        """
        Delete data from the storage.

        :param key: Unique value that corresponds to a specific data.
        :return: Key of deleted item or KeyNotFoundError.
        """

    @abstractmethod
    def get_all_stored_data(self) -> Any:
        """Get all data from that will be stored."""
