#!/usr/bin/env python3
"""This will handle our basic auth"""
import base64
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """- defines the attr && methods for basic
    authorization
    - This will inherit from Auth
    Args:
        Auth (class):The  Parent authentication_class
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """This will return the Base64 part of Authorization header
        to a Basic_Authentication
        Args:
            authorization_header (str): auth_header
        Returns:
            str: Thos will be base64 part of header
        """
        if not (authorization_header and isinstance(authorization_header, str)
                and authorization_header.startswith('Basic ')):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """returns the decoded val of a Base64 str
        Args:
            base64_authorization_header (str): base64 auth header
        Returns:
            str: decoded val of the base64 str
        """
        if not (base64_authorization_header and
                isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> Tuple[str, str]:
        """This will extract usr email && passwrd
        from our Base64 decoded val.
        Args:
            self (obj): This our Basic Auth instance
            decoded_base64_authorization_header (str): auth_header
        """
        if not (decoded_base64_authorization_header and
                isinstance(decoded_base64_authorization_header, str) and
                ':' in decoded_base64_authorization_header):
            return None, None

        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """This returns the Usr instance based on his email && passwrd.
        Args:
            self (_type_): Our Basic auth instance
            user_email(str): usr email
            user_pwd(str): usr pwd
        """
        if not (user_email and isinstance(user_email, str) and
                user_pwd and isinstance(user_pwd, str)):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """This will get the current usr"""
        try:
            auth_header = self.authorization_header(request)
            encoded = self.extract_base64_authorization_header(auth_header)
            decoded = self.decode_base64_authorization_header(encoded)
            email, password = self.extract_user_credentials(decoded)
            return self.user_object_from_credentials(email, password)
        except Exception:
            return None
