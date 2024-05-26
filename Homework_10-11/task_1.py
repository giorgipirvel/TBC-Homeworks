n = int(input("Enter the number: "))

if n > 1:
    x = 0
    sign = 1

    for i in range(1, n + 1):
        term = 1/(2 * i - 1)
        x = x + sign * term
        sign = sign * (-1)

    x = x * 4

    print(f"Value of x is: {x}")

else:
    print("Out of range")

# ორივე შემთხვევაში რაც უფრო მაღალ მნიშვნელობას ვაძლევთ n-ს, 
# მით უფრო უახლოვდება დაბეჭდილი მნიშვნელობა პის (3.14159)
