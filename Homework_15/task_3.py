def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
    
def main():
    test = ["Test", "Abc", "Pitagora"]

    for string in test:
        reversed = reverse(string)
        print(f"{string} - {reversed}")

if __name__ == "__main__":
    main()
