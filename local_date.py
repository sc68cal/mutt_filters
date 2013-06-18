#!/usr/bin/env python
"""
Converts Date: headers in a mail message
to local timezone
"""
from dateutil import parser, tz
import re
import sys


def to_local_datetime(date_matches):
    date = parser.parse(date_matches.group(1).strip())
    return date.astimezone(tz.tzlocal())

if __name__ == "__main__":
    reg = re.compile("Date:(.*)")
    for line in sys.stdin:
        matches = reg.match(line)
        if matches:
            date = to_local_datetime(matches)
            sys.stdout.write("Date: %s\n" %
                             date.strftime("%a, %d %b %Y %I:%M:%S %p"))
        else:
            sys.stdout.write(line)
