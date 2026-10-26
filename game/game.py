#importing random
import random


#taking an input
while True:
    num = input("Level: ")
    if int(num) > 0:
        break
    else :
        continue

ran_num = random.randint(0,int(num))

while True:
    try:
        guess = input("Guess: ")
        if int(guess) > 0:

            if int(guess) == int(ran_num) :
                print("Just right!")
                break
            elif int(guess) < int(ran_num):
                print("Too small!")
                pass
            elif int(guess) > int(ran_num):
                print("Too large!")
                pass
        else:
            continue
    except ValueError:
        continue

