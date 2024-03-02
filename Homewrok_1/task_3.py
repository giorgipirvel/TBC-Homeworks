a=int(input("Enter the length of side a: "))
b=int(input("Enter the length of side b: "))
c=int(input("Enter the length of side c: "))
s=(a+b+c)/2

if a+b>c and b+c>a and a+c>b:
    print(a+b+c)
    print((s*(s-a)*(s-b)*(s-c))**0.5)

else:
    print("violation")