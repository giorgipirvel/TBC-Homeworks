import random

n = int(input("Enter the number: "))

if 0 < n < 30:
    random_numbers = [random.randrange(0, 1000) for int in range(n)]
    
    print("Generated numbers:", random_numbers)
   
    max_number = random_numbers[0]
    
    for number in random_numbers:
        if number > max_number:
            max_number = number

    print("Maximum number:", max_number)

else: #out of range
    print("N/A")
