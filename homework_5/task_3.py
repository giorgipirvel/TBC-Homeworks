n = int(input("Enter the height of the Christmas tree: "))

if 0 < n < 50:
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(f"{spaces}{stars}")

    bottom = " " * (n - 1)
    print(f"{bottom}|")

else:
    print("Enter number between 0 and 50")

# ვიცი ისეთი არაა როგორიც უნდა იყოს, ვცდი ისეთის შექმნასაც
        