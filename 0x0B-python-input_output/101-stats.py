#!/usr/bin/python3

import sys
import signal
from collections import defaultdict

file_size = 0
status_codes = defaultdict(int)
line_counter = 0

def print_statistics():
    global file_size, status_codes, line_counter
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
    print("")

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts = line.split()
    if len(parts) >= 9:
        try:
            status_code = parts[-2]
            size = int(parts[-1])
            file_size += size
            status_codes[status_code] += 1
            line_counter += 1
        except (ValueError, IndexError):
            pass

    if line_counter >= 10:
        print_statistics()
        line_counter = 0

print_statistics()
