#1. (5 ქულა) Დაწერეთ პროგრამა რომელიც მომხმარებელს მოსთხოვს შეიყვანოს შემდეგი მონაცემები:
# სახელი, გვარი და ასაკი. Ეს ინფორმაცია Პროგრამამ ეკრენზე უნდა დაბეჭდოს შემდეგ ფორმატში:
# Hello სახელი გვარი. 
#Age: ასაკი.

user_input = input("Please, enter you first name and last name: ")

age = int(input("Please, indicate your age: "))

if age > 0:
    print("Hello",user_input)
    print("Age:",age)

else:
    print("It isn't possible")
