#!/usr/bin/env python3
"""this module handles the authentication of users"""

from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """this class handles the authentication of users"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the
        Authorization header for a Basic Authentication:
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ returns the decoded value of a
        Base64 string base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encode = base64.b64decode(base64_authorization_header)
            return (encode.decode('utf-8'))
        except base64.binascii.Error as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header:
            str) -> (str, str):
        """returns the user email
        and password from the Base64 decoded value.
        """
        _data = ()
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        data = decoded_base64_authorization_header.split(':')
        return(data)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """that returns the User instance based on his email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        from models.user import User
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overload current_user - which now overloads Auth.current_user
        but with
        a request input
        """
        auth_header = \
            self.authorization_header(request)
        if auth_header:
            b64_header = \
                self.extract_base64_authorization_header(auth_header)
            if b64_header:
                decode_header = \
                    self.decode_base64_authorization_header(b64_header)
                if decode_header:
                    email, pwd = \
                        self.extract_user_credentials(decode_header)
                    print(email, pwd)
                    if email:
                        user = self.user_object_from_credentials(
                            email, pwd)
                        return user
        return None
