#!/usr/bin/env python3
"""
Converts Date: headers in a mail message
to local timezone
"""
import datetime
import io
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
    # Replace characters when we hit a UnicodeDecodeError
    # https://docs.python.org/3.3/library/codecs.html?highlight=replace#codec-base-classes
    input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8',
                                    errors='replace')
    for line in input_stream:
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
