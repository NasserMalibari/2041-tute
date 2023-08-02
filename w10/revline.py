#!/usr/bin/env python3


import sys


def main():
    for line in sys.stdin:
        line = line.split()
        words = reversed(line)
        # alternatively
        # line = line[::-1]
        print(line)
        print(" ".join(words))
        # for word in words:
        #     print(f"{word} ", end = "")

if __name__ == "__main__":
    main()