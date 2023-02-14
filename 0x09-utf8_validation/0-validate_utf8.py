#!/usr/bin/python3
"""0-validate_utf8 module"""


def count_ones(n: int) -> int:
    """Counts the ones at the beginning of a number"""
    count = 0
    for i in range(7, -1, -1):
        if n & (1 << i):
            count += 1
        else:
            break
    return count


def validUTF8(data) -> bool:
    """
    Determines if a given data set represents
    a valid UTF-8 encoding
    """
    if not data:
        return False
    count = 0
    for d in data:
        if not count:
            count = count_ones(d)
            if count == 0:
                continue
            elif count == 1 or count > 4:
                return False
        else:
            if count_ones(d) != 1:
                return False
        count -= 1
    return True
