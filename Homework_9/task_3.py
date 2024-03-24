input_date = input("Enter the date: ")

date_component = input_date.split("T")
date = date_component[0]
time_component = date_component[1].split("+")
time = time_component[0]
timezone = time_component[1]

year, month, day = date.split("-")

hours, minutes, seconds = time.split(":")
hours = int(hours)

timezone_hours = int(timezone.split(":")[0])
if timezone_hours >= 0:
    timezone_format = "+" + str(timezone_hours).lstrip("0")

else:
     str(timezone_hours).lstrip("0")

print(f"{day}-{month}-{year} {hours}:{minutes}:{seconds.split('.')[0]} {timezone_format}")
