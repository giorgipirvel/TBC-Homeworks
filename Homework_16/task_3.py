import random

def remove_dublicates(list):
    unique_numbers = []
    for number in list:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers
    
random_numbers = [random.randint(1,30) for i in range(50)]

unique_elements = remove_dublicates(random_numbers)

print("List", unique_elements)
print("Lenght", len(unique_elements))
print(random_numbers)
