# Implement a class called Employee with attributes name, age, and salary.
# Create methods increase_salary and display_details.
# The increase_salary method should take a percentage increase and update the salary accordingly.
# The display_details method should print all attributes of the employee.
# Instantiate an object of this class, apply a salary increase of 10%, and display the details.

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)
        print(f"Salary increased by {percentage}%, new salary: {self.salary}")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")

# Instantiate an object of the Employee class
employee = Employee("John Doe", 35, 50000)

# Increase salary by 10%
employee.increase_salary(10)

# Display employee details
employee.display_details()