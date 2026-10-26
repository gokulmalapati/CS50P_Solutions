import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hourf := re.search(r"^(\d+)(?::(\d{2}))? AM to (\d+)(?::(\d{2}))? PM$", s):
        for i in [1,3]:
            if int(hourf[i]) > 12:
                raise ValueError
            elif int(hourf[i+1] or 0) > 59:
                raise ValueError
        houri = str(int(hourf[1])%12).zfill(2)
        minutei = hourf[2] or "00"
        minuteS = hourf[4] or "00"
        hourS = str(int(hourf[3])%12 + 12).zfill(2)
        return f"{houri}:{minutei} to {hourS}:{minuteS}"
    elif hourf := re.search(r"^(\d+)(?::(\d{2}))? PM to (\d+)(?::(\d{2}))? AM$", s):
        for i in [1,3]:
            if int(hourf[i]) > 12:
                raise ValueError
            elif int(hourf[i+1] or 0) > 59:
                raise ValueError
        hourAM = str(int(hourf[1])%12 ).zfill(2)
        minuteAM = hourf[2] or "00"
        minutePM = hourf[4] or "00"
        hourPM = str(int(hourf[3])%12 + 12).zfill(2)
        return f"{hourPM}:{minutePM} to {hourAM}:{minuteAM}"
    else :
        raise ValueError


if __name__ == "__main__":
    main()
