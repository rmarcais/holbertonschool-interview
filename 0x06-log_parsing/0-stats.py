#!/usr/bin/python3
"""Task 0. Log parsing"""

from sys import stdin
import re
import signal

lap = 0

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

regex = r"^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} - "
regex += r"\[[\d\-:\.\s]+\] \"[\w\s\/.]+\" \d{1,3} \d{1,3}$"

total_size = 0


def print_stats(status_codes, total_size):
    """Prints statistics from the beginning"""
    print("File size: {}".format(total_size))
    for k, v in status_codes.items():
        if v > 0:
            print("{}: {}".format(k, v))


def handler(signal, frame):
    """Prints statistics after a keybord interruption"""
    print_stats(status_codes, total_size)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    for line in stdin:
        if re.match(regex, line):
            lap += 1
            infos = line.split()
            code = int(infos[-2])
            total_size += int(infos[-1])
            if code in status_codes.keys():
                status_codes[code] += 1
            if lap == 10:
                lap = 0
                print_stats(status_codes, total_size)
