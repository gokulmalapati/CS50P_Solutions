import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip_v = re.search(r"^(0*)(\d+)\.(0*)(\d+)\.(0*)(\d+)\.(0*)(\d+)$" , ip)
    if ip_v:
        count = 0
        for i in [2,4,6,8]:
            if 0<=int(ip_v[i])<=255:
                count +=1
        for i in [1,3,5,7]:
            if ip_v[i] == "":
                count += 1
        if count == 8:
            return True
        else:
            return False
    else :
        return False



if __name__ == "__main__":
    main()
