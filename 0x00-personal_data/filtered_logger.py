#!/usr/bin/env python3
"""
this module conatains the filter_datum function
"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log messages in encrypted format encrypted"""
    for word in fields:
        message = re.sub('{}=[^{}]*'.format(word, separator),
                         '{}={}'.format(word, redaction), message)
    return message
