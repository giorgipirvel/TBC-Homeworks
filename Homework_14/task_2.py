from task_1 import gcd_rec

def lcm(a,b):
    return (a * b) // gcd_rec(a,b)

def main():
    a = int(input("Enter a: "))
    if a <= 0:
        print("Out of range")
        return
    
    b = int(input("Enter b: "))
    if b >= 10000:
        print("Out of range")
        return

    print(f"LCM of {a} and {b} is {lcm(a,b)}")

if __name__ == "__main__":
    main()
