import random

Number_of_players=int(input("Enter the players number: "))

if Number_of_players>0:
    for player in range (1, Number_of_players+1):
        dice_1=random.randint(1,6)
        dice_2=random.randint(1,6)
        print(f"{dice_1} {dice_2}")

else:
    print("No way")
