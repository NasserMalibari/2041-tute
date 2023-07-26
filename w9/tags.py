"""
Write a Python program, tags.py which given the URL of a web page fetches it by running wget and prints the HTML tags it uses.
The tag should be converted to lower case and printed in alphabetical order with a count of how often each is used.
Don't count closing tags.
Make sure you don't print tags within HTML comments
"""

from argparse import ArgumentParser
import subprocess
import re
import collections

def main():
    parser = ArgumentParser(prog="tags")
    parser.add_argument("-f","--frequency",action="store_true", help="prints tags by frequency")
    parser.add_argument("url", help="url to find tags of")

    args = parser.parse_args()

    # args.url 
    # args.frequency: Bool

    process = subprocess.run(["wget", "-O-", "-q", args.url], capture_output=True, text=True)

    text = process.stdout.lower()

    # remove comments
    text = re.sub(r"<!--(.*?)-->","",text, flags=re.DOTALL)
    # get list of tags
    tags = re.findall(r"<\s*(\w+)>", text)

    # print(tags[:10])

    # count them
    counts = collections.Counter(tags)
    # print(counts)
    # alternatively loop through tags, and increment counts[tag]

    if args.frequency:
        # print("print by freq")
        for tag in counts.most_common():
            print(tag)
    else:
        for tag in sorted(counts):
            print(tag)
        # print("by alphabetical")
if __name__ == "__main__":
    main()