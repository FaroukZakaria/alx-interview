#!/usr/bin/python3
"""
Interview question - Log parsing
"""

import sys
import re

i = 0  # counts the number of lines read
total_size = 0
pattern = r'''(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) -
 \[([^\]]+)\] \"GET \/projects\/260 HTTP\/1\.1\" (\d+) (\d+)
'''.replace('\n', '')
codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
    }


def print_statistics(codes):
    """
    Prints the statistics
    """
    print("File size: {}".format(total_size))
    for code in codes:
        if codes[code] == 0:
            continue
        print(f"{code}: {codes[code]}")

try:
    for line in sys.stdin:
        match = re.findall(pattern, line)
        if match == []:
            continue

        line = line.split()
        total_size += int(line[-1])
        status = int(line[-2])
        if status in codes:
            codes[status] += 1
        else:
            continue
        i += 1
        if i == 10:
            print_statistics(codes)
            i = 0

    print_statistics(codes)

except KeyboardInterrupt:
    print_statistics(codes)
    i = 0
