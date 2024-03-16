n = int(input("Enter the number: "))

if 0 <= n <20:
    count= 0 
    a, b = 0, 1
    print("Fibonacci:",end=" ")
    while count <= n:
        print (a, end=" ")
        a, b = b, a + b
        count += 1

else:
    print("Out of range")
