"""The module represents DataManager for data saving and manipulating."""

from typing import Any, Dict

from sdk.exceptions.data_manager_errors import KeyAlreadyExistsError, KeyNotFoundError


class DataManager(object):
    """The class represents methods for data saving and manipulating."""

    def __init__(self) -> None:
        """Initialize class DataManager instance."""
        self._storage: Dict[str, Any] = {}

    def add_data(self, key: str, data_to_store: Any) -> None:
        """
        Add data in the storage.

        :param key: Unique value that corresponds to a specific data.
        :param data_to_store: Data to store.
        :return: None or KeyAlreadyExistsError.
        """
        if key not in self._storage:
            self._storage[key] = data_to_store
        else:
            raise KeyAlreadyExistsError()

    def read(self, key: str) -> Any | None:
        """
        Get data by specified key.

        :param key: Unique value that corresponds to a specific data.
        :return: Saved value or KeyNotFoundError.
        """
        if key in self._storage:
            return self._storage.get(key)
        raise KeyNotFoundError()

    def update(self, key: str, new_data_to_store: Any) -> None:
        """
        Update stored value in storage.

        :param key: Unique value that corresponds to a specific data.
        :param new_data_to_store: Provided updated data to store.
        :return: None or KeyNotFoundError.
        """
        if self._storage.get(key):
            self._storage[key] = new_data_to_store
        else:
            raise KeyNotFoundError()

    def delete(self, key: str) -> str:
        """
        Delete data from the storage.

        :param key: Unique value that corresponds to a specific data.
        :return: Key of deleted item or KeyNotFoundError.
        """
        if key in self._storage:
            self._storage.pop(key, None)
            return key
        raise KeyNotFoundError()

    def get_all_stored_data(self) -> Dict[str, Any]:
        """Get all data from that will be stored."""
        return self._storage
