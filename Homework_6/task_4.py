a = int(input("Enter the number: "))

if 0 <= a <= 10:
    i = 1
    while i <= a * 2 - 1:
        if i <= a:
            j = 1
            while j <= i:
                print(j, end=" ")
                j += 1
        else:
            j = 1
            while j <= a * 2 - i:
                print(j, end=" ")
                j += 1
        print()
        i += 1
else:
    print("Out of range")
