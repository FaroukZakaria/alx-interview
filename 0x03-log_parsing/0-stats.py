#!/usr/bin/python3
"""
Interview question - Log parsing
"""

import sys
import re

i = 0  # counts the number of lines read
total_size = 0
pattern = r'''
\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} -
 \[([^]]+)\] \"GET /projects/260 HTTP/1.1\" \d+ \d+
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
        codes[code] = 0


for line in sys.stdin:
    match = re.findall(pattern, line)
    if match == []:
        continue
    i += 1
    line = line.split()
    total_size += line[-1]
    status = line[-2]
    if KeyboardInterrupt or i == 10:
        print_statistics(codes)
        i = 0
