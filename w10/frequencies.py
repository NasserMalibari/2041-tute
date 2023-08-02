#!/usr/bin/env python3

import sys, collections

freq = collections.Counter()

for line in sys.stdin:
    # chars = list(line)
    for char in line:
        if (char.isalnum()):
            freq[char] += 1

print(freq)


