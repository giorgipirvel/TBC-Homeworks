password = "hey"
max_tries = 3

for tries in range(1, max_tries + 1):
    input_password = input("Please enter password: ")
    if password == input_password:
        print("Hello from Georgia")
        break
    else:
        if tries == max_tries:
            print("You are blocked!!!")
        else:
            print("Password was not correct. Try again - ")
