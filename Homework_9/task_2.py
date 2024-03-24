a = input("Enter the word: ")
b = input("Enter the word: ")

def first_from_second(a,b):
    a = a.lower()
    b = b.lower()
    
    count = {}
    for i in b:
        count[i] = count.get(i,0) + 1
    
    for i in a:
        if i not in count or count[i] == 0:
            return "NO"
        else:
            count[i] = count[i] - 1
    
    return "YES"

result = first_from_second(a,b)
print("Output:",result)
