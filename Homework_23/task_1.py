import json

def calculate_average_salary(data):
    department_salaries = {}

    for department, details in data.items():
        employees = details.get("employees", [])

        total_salary = 0 
        count = 0

        for employee in employees:
            salary = employee.get("salary")

            if salary is not None:
                try:
                    salary = float(salary)
                    total_salary += salary
                    count += 1
                except ValueError:
                    pass


        if count > 0:
            average_salary = total_salary / count
            department_salaries[department] = round(average_salary, 2)

    return department_salaries

try:
    with open("homework.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("Make sure the file exists")
    exit()

department_salaries = calculate_average_salary(data)

try:
    with open("avg_salary.json", "w") as result_file:
        json.dump(department_salaries, result_file, indent=4)
except Exception as e:
    print("error to file", e)
