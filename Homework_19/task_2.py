def count_characters(input_string):
    char_count = {}

    for i in input_string:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for i, count in char_count.items():
        print(f"{i} - {count}")

input_string = input("Enter the word: ")

count_characters(input_string)
