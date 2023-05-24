username = '1'
password = '1'

print("\n\t----- Welcome to Pythonram, Sign in blow! -----\n")
user_input = ''
pass_input = ''

while True:
    user_input = input("Enter username: ")
    pass_input = input("Enter password: ")
    if user_input == username :
        if pass_input == password:
            print("\tWelcome")
            break
        elif pass_input != password:
            print("\t Try again")
    else:
        print("\tIncorrect, please try again")
        continue