# quiz 1
def validate():
    while True:
        password = input("Please enter password: ")
        if len(password) < 8:
            print("must have a minimum of 8 characters")
        elif not any(p.isupper() for p in password):
            print("must contain at least one upper-case letter ")
        elif sum(p.isdigit() for p in password) < 2:
            print("must contain at least two digits")
        # elif :
        #     print("Can’t contain two or more consecutive digits")
        else:
            print("This is a valid password")
            break


validate()
