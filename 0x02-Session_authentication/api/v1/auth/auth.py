#!/usr/bin/env python3
"""
    This will Authenticate a module for our API.
"""
import os
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """
        This is our Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            This will check if a path requires auth.
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
            This will get the authorization header field from our request.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Thia will get the current usr from the/our request.
        """
        return None

    def session_cookie(self, request=None) -> str:
        """
            This will get the val of the cookie named SESSION_NAME.
        """
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
