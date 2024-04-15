def gcd_rec(a,b):
    if b == 0:
        return a
    else: 
        return gcd_rec(b, a%b)
    
def gcd_iter(a,b):
    while b:
        a, b = b, a % b
    return a

def main():
    a = int(input("Enter a: "))
    if a <= 0:
        print("Out of range")
        return
    
    b = int(input("Enter b: "))
    if b >= 10000:
        print("Out of range")
        return
    
    recursive = gcd_rec(a,b)
    iterative = gcd_iter(a,b)

    print(f"GCD OF {a} and {b} is {recursive}")
    print(f"GCD OF {a} and {b} is {iterative}")

if __name__ == "__main__":
    main()
