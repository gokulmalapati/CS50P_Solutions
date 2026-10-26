import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r'^<iframe.*src="https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"', s):
        if link[2] != "":
            return f"https://youtu.be/{link[2]}"
        else :
            return "None"



if __name__ == "__main__":
    main()
