i = 0
x = input("Insert a coin")
while i >= 0 :

    if x == "25" or x == "10" or x == "5":
        i = i + int(x)
        z = 50 - i
        if z > 0 :
            x = input(f"Amount Due: {z}\n")


        elif z <= 0:
            y = -z
            print(f"Change Owed: {y}")
            break
    else:
        x = input("Amount Due: 50\n")
        continue
