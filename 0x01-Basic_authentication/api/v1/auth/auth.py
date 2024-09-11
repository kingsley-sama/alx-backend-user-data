#!/usr/bin/env python3
"""this module handles the authentication of users"""

from typing import List, TypeVar
from flask import request


class Auth:
    """this class handles the authentication of users"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method that returns False - path and excluded_paths will
         be used later, now, you don’t need to take care of them
         """
        if path:
            path = path if path.endswith('/') else path+'/'
        if not path or not excluded_paths or path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """public method that returns None -
        request will be the Flask request object
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return (request.headers["Authorization"])

    def current_user(self, request=None) -> TypeVar('User'):
        """public method that returns None -
        request will be the Flask request object
        """
        return None
