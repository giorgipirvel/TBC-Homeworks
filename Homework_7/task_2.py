n = int(input("Enter the number: "))

if 0 < n <= 1000:
   print("Sequence:", end=" ")
   while n != 1:
      print(n, end=" ")
      if n%2 == 0:
         n = n // 2

      else:
         n = n * 3 + 1
   print(n)

else:
   print("Number should be between 0 and 1000")
