#!/usr/bin/env python3
"""
    This is the usr module.
"""
import hashlib
from models.base import Base


class User(Base):
    """
        Our Usr class.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
            This will Init a Usr instance.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self._password = kwargs.get('_password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    @property
    def password(self) -> str:
        """
            This will Get the passwrd.
        """
        return self._password

    @password.setter
    def password(self, pwd: str):
        """
            This will set a new password: encrypt in SHA256.

            WARNING: Use a better passwrd hashing algo like argon2
            or bcrypt in real-world projects.
        """
        if pwd is None or type(pwd) is not str:
            self._password = None
        else:
            self._password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd: str) -> bool:
        """
            This will Validate a passwrd.
        """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        pwd_e = pwd.encode()
        return hashlib.sha256(pwd_e).hexdigest().lower() == self.password

    def display_name(self) -> str:
        """
            This will display Usr_name based on email/first_name/last_name.
        """
        if self.email is None and self.first_name is None \
                and self.last_name is None:
            return ""
        if self.first_name is None and self.last_name is None:
            return "{}".format(self.email)
        if self.last_name is None:
            return "{}".format(self.first_name)
        if self.first_name is None:
            return "{}".format(self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)
