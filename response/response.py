import validators

email = input("What is your Email Address: ")
if validators.email(email):
    print("Valid")
else :
    print("Invalid")
