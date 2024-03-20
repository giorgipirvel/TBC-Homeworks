user_input = input("Enter the text: ")

vowels = "aeiouAEIOU"

for i in user_input:
    if i not in vowels:
        print(i, end = "")
