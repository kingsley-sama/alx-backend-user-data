#!/usr/bin/env python3
"""this module handles the authentication of users"""

from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """this class handles the authentication of users"""
    def __init__(self):
        pass
