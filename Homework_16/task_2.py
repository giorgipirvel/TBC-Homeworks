import random

random_numbers = [random.randint(1,30) for i in range(50)]

new_list = []
for num in random_numbers:
    new_list.extend([num] * num)

print("List:",new_list)
print("Length:",len(new_list))
print(random_numbers)
