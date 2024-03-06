n=int(input("Enter the number: "))

if 0<n<1000:
    divisor=[i for i in range(1,n+1) if n % i==0]
    print(divisor)

else:
    print("Out of range")
