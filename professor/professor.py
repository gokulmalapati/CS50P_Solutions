import random


#collecting info about the level of the program
def get_level():
    while True:
        try:
            level1 = input("Level: ")
            if int(level1) in [1 , 2 , 3]:
                return level1
                break
            else:
                continue
        except ValueError:
            continue




def generate_integer(level):
    if int(level) == 1:
        for _ in range(10):
            return random.randint(0,9)

    elif int(level) == 2:
        for _ in range(10):
            return random.randint(10,99)

    elif int(level) == 3:
        for _ in range(10):
            return random.randint(100,999)



def main():
    level = get_level()
    pairs = []
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        pair = (x,y)
        pairs.append(pair)
    score = 0
    strike = 0

    for pair in pairs:
        correct_ans = int(pair[0]) + int(pair[1])
        for attempt in range(3):
            ans = input(f"{pair[0]} + {pair[1]} = ")
            try:
                if int(ans) == int(correct_ans):
                    score += 1
                    break
                else :
                    print("EEE")
                    strike += 1
                    if int(strike) == 3:
                        print(f"{pair[0]} + {pair[1]} = {correct_ans}")
                    else:
                        continue
            except ValueError:
                print("EEE")


    print(f"Score: {score}")





if __name__ == "__main__":
    main()
