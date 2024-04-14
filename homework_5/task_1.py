n=int(input("Enter the number: "))

if 0 < n < 50:
    for j in range (1,n+1):
        divisors=[1]
        for i in range (2, j + 1):
             if j % i ==0:
                  divisors.append(i)
                  if len(divisors)==3:
                       break
        print(f"{j} - {divisors}")

else: 
     print("Out of range")
