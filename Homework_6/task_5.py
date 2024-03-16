a = int(input("Enter the number: "))

if 0 <= a <= 10:
    i = 0
    while i <= a:
        print(" " * (a - i) * 2, end=" ")

        j = i
        while j >= 0:
            print(j, end=" ")
            j -= 1

        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1

        print()
        i += 1
else:
    print("Out of range")
