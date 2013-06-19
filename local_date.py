#!/usr/bin/env python3.3
"""
Converts Date: headers in a mail message
to local timezone
"""
import datetime
import re
import sys

INPUT_FORMAT = '%a, %d %b %Y %H:%M:%S %z'
OUTPUT_FORMAT = "%a, %d %b %Y %I:%M:%S %p"
EXPR = "Date:.(\w{3},.\w{1,2}.\w{3}.{4}\d.\d{2}:\d{2}:\d{2}.[+-]\d{4})"


def to_local_datetime(date_matches):
    date = datetime.datetime.strptime(date_matches.group(1).strip(),
                                      INPUT_FORMAT)
    return date.astimezone()

if __name__ == "__main__":
    found = False
    reg = re.compile(EXPR)
    for line in sys.stdin:
        if not found:
            matches = reg.match(line)
            if matches:
                date = to_local_datetime(matches)
                sys.stdout.write("Date: %s\n" %
                                 date.strftime(OUTPUT_FORMAT))
                found = True
            else:
                sys.stdout.write(line)
        else:
            sys.stdout.write(line)
