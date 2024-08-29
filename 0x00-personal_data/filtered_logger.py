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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ';'

    def __init__(self, fields: List[str]):
        """inititalizes instance attributes"""
        self.fields: List[str] = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """this function formats a log record"""
        single_string: str = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            single_string, self.SEPARATOR)
