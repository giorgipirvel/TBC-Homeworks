n = int(input("Enter the height of the Christmas tree: "))

if 0 < n < 50:
    star = " " * n
    print(f"{star}*")
    for i in range(1, n):
        spaces = " " * (n - i)
        branches = ("/" * i) + "|" + ("\\" * i)
        print(f"{spaces}{branches}")

    bottom = " " * n 
    print(f"{bottom}|")

else:
    print("Enter number between 0 and 50")
