
#login user
def login():
    username = input("Enter user name: ")
    password = input("Enter password")
    if username.count() < 5 or password.count() <= 5:
        print("Username is too short!")
    print("Successful!")

    if username.isnumeric():
        print("Enter characters")
    print("Sucessful")

def signup():
    email = input("Enter your email address")
    password = input("Enter your password")
    