a = input("Enter the word: ")

def palindrome(a):
    checked = ""
    for i in a:
        if i.isalpha():
            checked = checked + i.lower()
    
    return checked == checked[::-1]

if palindrome(a):
    print("Output: is palindrome")

else:
    print("Output: isn't palindrome")
