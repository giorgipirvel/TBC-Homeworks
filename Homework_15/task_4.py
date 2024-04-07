def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for i in string:
        if i in vowels:
            count = count + 1
    return count

def main():
    test = ["Test", "Python", "Kvaratskhelia", "dEmonstrAtion"]

    for string in test:
        num_of_vowels = count_vowels(string)
        print(f"{string} - {num_of_vowels}")

if __name__ == "__main__":
    main()
