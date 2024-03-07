import random

colors=["clubs", "diamons", "hearts", "spades"]
values=["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

random_color = random.choice(colors)
random_value = random.choice(values)

random_card= f"{random_value} of {random_color}"

print(random_card)
