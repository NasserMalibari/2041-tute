#!/usr/bin/env python3

import sys

    
def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    words1 = set()
    with open(file1) as f1:
        for word in f1:
            word = word.strip()
            words1.add(word)
    
    words2 = set()
    with open(file2) as f2:
        for word in f2:
            word = word.strip()
            words2.add(word)
    
    # print(sorted(words1 - words2))

    for word in sorted(words1 - words2):
        print(word)

if __name__ == "__main__":
    main()