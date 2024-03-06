import datetime

year_of_birth=int(input("Enter the year of birth: "))
month_of_birth=int(input("Enter the month of birth: "))
day_of_birth=int(input("Enter the day of birth: "))

birth_date=datetime.date(year_of_birth,month_of_birth,day_of_birth)

day_of_week=birth_date.weekday()

weekdays=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(weekdays[day_of_week])
