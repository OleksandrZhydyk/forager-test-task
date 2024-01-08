"""The module for email validation."""

import re


class EmailValidator(object):
    """The class for email validation."""

    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    @classmethod
    def validate_email(cls, email: str) -> bool:
        """
        Validate the given email address.

        :param email: The email address to be validated.
        :return: True if the email is valid, False otherwise.
        """
        return bool(cls.email_pattern.match(email))
