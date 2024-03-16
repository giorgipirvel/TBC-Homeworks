number = int(input("Enter the number: "))

if 0 <= number < 10000:
    reversed = 0
    n = number
    while n != 0:
        digit = n % 10
        reversed = reversed * 10 + digit
        n = n // 10

    digit_sum = 0
    n = number
    while n != 0:
        digit = n % 10
        digit_sum = digit_sum + digit
        n = n // 10

    print("Reversed number:",reversed)
    print("Sum:",digit_sum)

else:
    print("Out of range")
