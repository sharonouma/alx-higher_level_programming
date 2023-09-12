#!/usr/bin/python3
"""
Prints the metrics including total file size and number of lines
by status code
"""
import sys


def print_metrics(total_size, status_codes):
    """
    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary containing the count of each
        status code.

    Returns:
        None.

    Raises:
        None.

    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {}


try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            ip, _, _, _, status, size = line.split()[0], line.split()[8],\
                    line.split()[10]
            total_size += int(size)

            if status in status_codes:
                status_codes[status] += 1
            else:
                status_codes[status] = 1

            if i % 10 == 0:
                print_metrics(total_size, status_codes)
        except (IndexError, ValueError):
            pass

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
