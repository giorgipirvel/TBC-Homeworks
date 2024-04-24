import random

random_numbers = [random.randint(1, 10000) for i in range (100)]
    
even_num = 0
odd_num = 0

for j in random_numbers:
    if j % 2 == 0:
        even_num = even_num + 1
    else:
        odd_num = odd_num + 1

numbers_dict = {'Even Numbers': even_num, 'Odd Numbers': odd_num}

print(numbers_dict)
print(random_numbers, end=" ")