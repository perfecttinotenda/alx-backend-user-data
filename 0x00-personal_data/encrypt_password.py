#!/usr/bin/env python3
"""
    Here will be Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ This reltrns a salted, hashed_password, which is a byte_str """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates the provided passwrd matches the hashed_passwrd """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
