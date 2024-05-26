import random
import math

n = int(input("Enter the number: "))

if n > 1:
    counter = 0
    for i in range(n):
        a = random.random()
        b = random.random()
        if math.sqrt(a ** 2 + b ** 2) <= 1:
            counter = counter + 1
    
    result = 4 * counter / n
    print(f"The result is: {result}")

else:
    print("Out of range")
