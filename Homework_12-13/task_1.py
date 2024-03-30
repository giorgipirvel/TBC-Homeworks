def result(user_input):
    shifted_words = []
    word = user_input.split()
    first_word = word[0]
    second_word = word[1]

    for i in range(1, len(second_word) + 1):
        shifted_string = second_word[-i:] + first_word + " " + second_word[:-i]
        shifted_words.append(shifted_string[::])
    
    shifted_words.append(second_word + " " + first_word)

    return shifted_words

def main():
    user_input = input("Enter the word: ")
    shifted_words = result(user_input)
    for shifted_string in shifted_words:
        print(shifted_string)

if __name__ == "__main__":
    main()
