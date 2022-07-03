
def home():
    name = input("Please enter your name:   ")
    print("Welcome " + name)

    if name.count() > 5:
        print("Enter more than 5 characters!")
    print("Sucessfull")

    home()