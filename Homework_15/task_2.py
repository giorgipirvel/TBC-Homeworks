def prime(n):
        for i in range(2, n):
           if n % i == 0:
               return False   
        return True

def main():
    numbers = [2,6,7,21,61,87,103,201]

    for num in numbers:
        if prime(num):
            print(f"{num} - prime number")
        else:
            print(f"{num} - isn't prime number")

if __name__ == "__main__":
    main()
