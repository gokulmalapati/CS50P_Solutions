#importing the required library
import  pyfiglet
import sys



#implementing the figlet
if len(sys.argv) == 1 :
    user = input("What ?")
    print(pyfiglet.figlet_format(user))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in  pyfiglet.FigletFont.getFonts():
            user = input("What ?")
            print(pyfiglet.figlet_format( user ,font = f"{sys.argv[2]}"))
        else:
            sys.exit("Invalid Usage")
    else :
        sys.exit("Invalid Usage")
#factoring any error or edge cases
else:
    sys.exit("Invalid Usage")

