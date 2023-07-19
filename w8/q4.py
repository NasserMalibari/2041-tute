#!/usr/bin/env python3

import sys


def main():
    # Todo: check args ...

    row = int(sys.argv[1])
    col = int(sys.argv[2])
    width = int(sys.argv[3])

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print(f"{i*j: >{width}}", end = "")
        print("")

# "1" --> "1  "
    
if __name__ == "__main__":
    main()