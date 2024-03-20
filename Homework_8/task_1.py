user_input = input("Enter the text: ")

for i in range (len(user_input)):
    if i % 2 == 0 and user_input[i] != "e":
        print(user_input[i], end = "")
