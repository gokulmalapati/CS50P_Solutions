#making a container
names = []

# taking input untill command-d
while True:
    try:
        name = input("what is your name? \n")
        names.append(name)
        continue
    #the adieu part
    except EOFError:
        if len(names) == 1:
            print(f"Adieu, adieu, to {names[0]}" )
            break
        elif len(names) == 2:
            last_name = names[-1]
            nameall = ", ".join(names[:-1])
            print(f"Adieu, adieu, to {nameall} and {last_name}")
            break

        elif len(names) > 2:
            last_name = names[-1]
            nameall = ", ".join(names[:-1])
            print(f"Adieu, adieu, to {nameall}, and {last_name}")
            break


