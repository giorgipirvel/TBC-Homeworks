import json

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        try:
            self.salary = int(salary)
        except ValueError:
            self.salary = 0

class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = [Employee(**emp) for emp in employees]

    def average(self):
        if not self.employees:
            return 0
        return sum(emp.salary for emp in self.employees) / len(self.employees)
    
    def max_salary(self):
        if not self.employees:
            return 0 
        return max(emp.salary for emp in self.employees)
    
    def min_salary(self):
        if not self.employees:
            return 0
        return min(emp.salary for emp in self.employees )
    
    def positions(self):
        positions_count = {}
        for emp in self.employees:
            if emp.position in positions_count:
                positions_count[emp.position] += 1
            else:
                positions_count[emp.position] = 1
        return positions_count
    

def main():
    filename = "homework_1.json"

    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return
    
    departments = []
    for key, value in data.items():
        departments.append(Department(value["name"],value["description"], value["employees"]))
    
    for department in departments:
        print(f"Description: {department.description}")
        print(f"Average salary: {department.average()}")
        print(f"Max salary: {department.max_salary()}")
        print(f"Min salary: {department.min_salary()}")
        print("Positions - amount:", department.positions())
        print("\n")

if __name__ == "__main__":
    main()
