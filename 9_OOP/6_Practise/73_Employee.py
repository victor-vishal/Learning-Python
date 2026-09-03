# Define a Employee class with attributes role, department & salary. This class also has a showDetails( ) method. 
# Create an Engineer class that inherits properties from Employee & has additional attributes : name & age."

class Employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showDetails(self):
        print(f"Role:{self.role} \nDepartment: {self.dept} \nSalary: {self.sal}\n\n\n")


class Engineer(Employee):
    def __init__(self, name, age, role, dept, sal):
        self.name = name
        self.age = age
        super().__init__(role, dept, sal)

    def showDetails(self):
        print(f"Name: {self.name} \nAge: {self.age} \nRole:{self.role} \nDepartment: {self.dept} \nSalary: {self.sal}")

e1 = Engineer('Vishal', 25, 'Software Engineer', 'IT', 50000)
e1.showDetails()