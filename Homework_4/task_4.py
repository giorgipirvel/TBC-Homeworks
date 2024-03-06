n = int(input("Enter number: "))

if 0 <= n < 20:
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        a, b = 0, 1
        for int in range(2, n + 1):
            a, b = b, a + b
        result = b

    print(f"{result}")
    
else:
    print("N/A")
