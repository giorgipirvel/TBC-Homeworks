user_input = input("Enter a word: ")

length = len(user_input)

if length % 2 == 0:
    middle = length // 2 - 1
else:
    middle = length // 2

count = 0
while count < 5:
    print(user_input[0], user_input[-1], user_input[middle], end= " ")
    if length % 2 == 0:
        print(user_input[middle + 1], end="")
    print()
    count = count + 1
