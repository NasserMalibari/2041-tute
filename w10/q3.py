#!/usr/bin/python3

import sys

vowels = "aeiou"

# "aeiouAEIOU" "AEIOUaeiou"
our_table = str.maketrans(vowels.lower() + vowels.upper() , 
                vowels.upper() + vowels.lower())

for line in sys.stdin:
    line = line.strip()
    print(line.translate(our_table))

# {'a':"A"}