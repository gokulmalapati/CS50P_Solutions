while True:
    y = input("How much fuel is left? [In the form of X/Y]").split("/")
    if len(y) == 2 and y[0].isdigit() and y[1].isdigit():
        x = y[0]
        a = y[1]
        if int(x)>= 0 and int(a)>0  and int(x)<= int(a) :
            z = round( int(x)/int(a) *100)
            if z < 2:
                print("E")
                break
            elif z > 98:
                print("F")
                break
            else :
                print(f"{z}%")
                break
