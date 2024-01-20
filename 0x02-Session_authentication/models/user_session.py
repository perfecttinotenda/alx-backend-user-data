#!/usr/bin/env python3
"""
    This is our Usr session module.
"""
from models.base import Base


class UserSession(Base):
    """
        Our Usr session class.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
            This will Init a Usr session instance.
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
