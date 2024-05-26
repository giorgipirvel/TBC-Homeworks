def shifted_string(a, b):
    if len(a) != len(b):
        return "NO"

    for i in range(len(a)):
        if a[i+1:] + a[:i+1] == b:
            return "YES"
        
    return "NO"

def main():
    a = input("Input a: ")
    b = input("Input b: ")
    result = shifted_string(a, b)
    print("Output:", result)

if __name__ == "__main__":
    main()
 