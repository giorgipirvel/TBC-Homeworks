def filter_words(words):
    filtered = [word.upper() for word in words if len(word) <= 3]
    print("Filtered words:",filtered)

def main():
    words = ["apple", "car", "bridge", "tomato", "sky"]
    print("Original words:", words)
    filter_words(words)

if __name__ == "__main__":
    main()
