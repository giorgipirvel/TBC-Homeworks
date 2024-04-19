temperatures= [
    (33, 34, 28),
    (24, 31, 27),
    (24, 23, 27),
    (28, 32, 34),
    (33, 21, 28),
    (20, 25, 31),
    (21, 31, 28)
]

weekly_total = 0
num_days = len(temperatures)

for i, temps in enumerate(temperatures, start = 1):
    average_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)

    weekly_total = weekly_total + average_temp

    print(f"Day {i}")
    print(f" Average temperature: {average_temp}")
    print(f" Maximum temperature: {max_temp}")
    print(f" Minimum temperature: {min_temp}")
    print()

weekly_average  = weekly_total / num_days
print(f"Average temperature of week: {weekly_average}")
