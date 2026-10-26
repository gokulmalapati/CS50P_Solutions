
def main():
    while True:
        y = input("How much fuel is left? [In the form of X/Y]")
        percent = convert(y)
        print(gauge(percent))


def convert(fraction):
    fraction = fraction.split("/")

    if len(fraction) == 2 and fraction[0].isdigit() and fraction[1].isdigit():
        x = fraction[0]
        a = fraction[1]
        if int(a) == 0:
            raise ZeroDivisionError
        elif int(a) <0 or int(x)<0 or int(x)>int(a):
            raise ValueError
        elif int(x)>= 0 and int(a)>0  and int(x)<= int(a) :
            fract = round( int(x)/int(a) *100)
            return fract





def gauge(percentage):
    if percentage < 2:
        return ("E")

    elif percentage > 98:
        return ("F")

    else :
        return (f"{percentage}%")

if __name__ == "__main__":
    main()
