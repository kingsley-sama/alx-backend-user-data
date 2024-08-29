#!/usr/bin/env python3
"""this module conatains the filter_datum function"""
import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """returns the log messages encrypted"""
    for word in fields:
        message = re.sub('{}=[^{}]*'.format(word, separator),
                         '{}={}'.format(word, redaction), message)
    return message
