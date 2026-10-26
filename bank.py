
def main():
    test = input("[greet me]").lower().strip()
    print(value(test))

def value(greetings):
    greetings = greetings.lower().strip()
    if greetings.startswith("hello"):
        return 0
    elif greetings.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
