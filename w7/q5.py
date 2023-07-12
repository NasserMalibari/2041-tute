#!/usr/bin/env python3

import sys

# sys.argv --> ['./q5.py', 'arg1', 'arg2']

# len(sys.argv) not in [2,3]

# beware: many assumptions are made:
# ex: if 2 args are given, checks first argument is 
# of the form '-n' but doesnt check if n is an integer!


def head(filename, n_lines):
    try:
        with open(filename) as file:
            for curr_lines, line in enumerate(file, start = 0):
                if (curr_lines >= n_lines):
                    break
                print(line, end = "")
    except FileNotFoundError:
        print(f"couldn't open {filename}!")

if (len(sys.argv) != 2 and len(sys.argv) != 3):
    raise Exception("wrong num of args!")

# n_lines = 10
if (len(sys.argv) == 2):
    head(sys.argv[1], 10)

if (len(sys.argv) == 3):
    if (sys.argv[1][0] == '-'):
        n_lines = int(sys.argv[1][1:])
        head(sys.argv[2], n_lines)
    else:
        raise Exception("first argument should start with -")

# f = open('filename')

# try:
#     with open('b.txt') as file:
#         for line in file:
#             print(line)
# except FileNotFoundError as e:
#     print(f"we didnt find the file!")

