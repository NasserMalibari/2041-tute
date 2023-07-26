
from argparse import ArgumentParser
import requests
from bs4 import BeautifulSoup
import sys
import collections

    
def main():
    parser = ArgumentParser(prog="tags")
    parser.add_argument("-f","--frequency",action="store_true", help="prints tags by frequency")
    parser.add_argument("url", help="url to find tags of")

    args = parser.parse_args()

    resp = requests.get(args.url)

    if (resp.status_code != 200):
        print("something went wrong")
        sys.exit(1)

    text = resp.text.lower()

    soup = BeautifulSoup(text, 'html.parser') # "html5lib"

    tags = soup.find_all('a')

    tag_names = [tag.name for tag in tags] 
    # print(tag_names[:10])

    counts = collections.Counter(tag_names)
    # alternatively loop through tags, and increment counts[tag]

    if args.frequency:
        # print("print by freq")
        for name, count in counts.most_common():
            # print(tag)
            print(f"{name} {count}")
            pass
    else:
        for tag in sorted(counts.items()):
            print(tag)
        # print("by alphabetical")

    # print(tags[:10])

    

if __name__ == "__main__":
    main()