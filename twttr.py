
def main():
    t = input("Wtf")
    print(shorten(t))

def shorten(word):
    word = word.replace("a" , "").replace("e","").replace("i","").replace("o","").replace("u","").replace("A","").replace("E","").replace("I","").replace("I","").replace("O","").replace("U","")
    return(word)

if __name__ == "__main__":
    main()


