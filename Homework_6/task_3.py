import random

a=random.randrange(0,100)

tries=1

while tries<=10:
    b=int(input("Enter the number: "))

    if b==a:
        print("You are winner")
        break

    elif a<b<100:
        print("high")

    elif b<a:
        print("low")

    else: # if entered number is more than 100
        break
    
    tries+=1

if tries>10:
    print("Computer is winner")

print("random number is:",a)
