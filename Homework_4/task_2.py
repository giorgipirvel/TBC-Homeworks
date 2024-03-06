import random

n = int(input("Enter the number: "))

if 0 < n < 30:
    random_numbers = [random.randrange(0, 1000) for int in range(n)]
    
    print("Generated numbers:", random_numbers)
    print("Maximum number:", max(random_numbers))

else: #out of range
    print("N/A")
