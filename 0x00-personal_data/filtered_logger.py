#!/usr/bin/env python3
"""
This module contains the filter_datum function
which obfuscates sensitive information in log messages.
"""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): A list of field names whose
        values should be obfuscated.
        redaction (str): The string used to replace sensitive field values.
        message (str): The original log message that
        contains sensitive information.
        separator (str): The character separating the fields
        in the log message.

    Returns:
        str: The obfuscated log message with sensitive field
        values replaced by redaction.
    """
    pattern = '|'.join([f'{field}=.*?{separator}' for field in fields])
    return re.sub(
        pattern,
        lambda m: f'{m.group(0).split("=")[0]}={redaction}{separator}',
        message
    )
