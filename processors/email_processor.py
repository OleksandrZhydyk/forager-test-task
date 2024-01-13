"""The module for email validation."""

import re
import uuid

from data_manager.interface import BaseManager
from sdk.client import HunterIOClient


class EmailProcessor(object):
    """The class for email validation."""

    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    def __init__(self, client: HunterIOClient, data_manager: BaseManager) -> None:
        """Initialize instance of EmailProcessor."""
        self.client = client
        self.data_manager = data_manager

    def save_email(self, email: str) -> str:
        """
        Validate and save validated email to the storage.

        :param email: The email address to be validated.
        :return: Validated email.
        """
        email = self._validate_email(email)
        storage_key = str(uuid.uuid4())
        self.data_manager.add_data(storage_key, email)
        return storage_key

    def _validate_email(self, email: str) -> str:
        """
        Validate the given email address.

        :param email: The email address to be validated.
        :return: Email address or ValueError.
        """
        if not bool(self.email_pattern.match(email)):
            raise ValueError('Email {email} is not valid.'.format(email=email))
        res = self.client.email_verification_handler.verify_email(request_params={'email': email})
        if res and getattr(res, 'full_email_data', None) and res.full_email_data.status == 'valid':
            return email
        raise ValueError('Email {email} is not accessible.'.format(email=email))
