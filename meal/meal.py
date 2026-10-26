def main():
    time = input("what is the time? ")
    hours = convert(time)
    if 7<= hours <=8:
        print("breakfast time")
    elif 12<= hours <= 13:
        print("lunch time")
    elif 18<= hours <= 19:
        print("dinner time")



def convert(time):
    if time.endswith("a.m.") or time.endswith("p.m."):
        time = time[:-4]
        parts = time.split(":")
        hour = int(parts[0])+12
        minutes = int(parts[1])
        return hour + int(minutes)/60
    else :
        parts = time.split(":")
        hour = int(parts[0])
        minutes = int(parts[1])
        return hour + int(minutes)/60

if __name__ == "__main__":
    main()

