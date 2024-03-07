A=int(input("Enter the number: "))
if 0<=A<=10:
    if A==0:
        print("none")
    elif A==1: #არ აქვს მარტივი გამყოფი, თავად არც მარტივ და არც შედგენილ რიცხვებს არ მიეკუთვნება.
        print("No prime divisor")
    elif A==2:
        print("2")
    elif A==3:
        print("3")
    elif A==4:
        print("2")
    elif A==5:
        print("5")
    elif A==6:
        print("2;3")
    elif A==7:
        print("7")
    elif A==8:
        print("2")
    elif A==9:
        print("3")
    elif A==10:
        print("2")

else:
    print("out of range")
 
 