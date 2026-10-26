import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    ums = re.findall(r"\b(um|Um|UM)\b",s)
    no_ums = len(ums)
    return no_ums




if __name__ == "__main__":
    main()
