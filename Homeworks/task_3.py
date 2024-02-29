a=float(input("Enter the length of side a: "))
b=float(input("Enter the length of side b: "))
c=float(input("Enter the length of side c: "))

if a+b>c and b+c>a and a+c>b:
    print(a+b+c)
    print((a+b+c)/2)

else:
    print("violation")