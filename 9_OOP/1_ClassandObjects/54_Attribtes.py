#Class and Instance Attributes

# Class Attributes are the attributes that are shared by all instances of a class
# they are the attributes that are common to all objects of a class
# for example for Student class, School name is common to all students, 

# Instance Attributes are specific to each object or instance of a class
# for example, name and age of a student

class Student:
    school_name = "APS School" # class attribute
    name = "anonymous" # class attribute

    # instance attributes have more precedence than class attributes, 
    # if both have same name, then instance attribute will be used

    def __init__(self, name, age, roll_no):
        print("Constructor is called... ")
        self.name = name  #instance attribute
        self.age = age
        self.roll_no = roll_no
        print(f"Student {self.name} is created\n")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll No: {self.roll_no}")
        print(f"School Name: {Student.school_name}")  # accessing class attribute
        # Class Attributes can be accessed using the class name as well as the object name, but it is recommended to access them using the class name

s1 = Student("Vishal", 20, 65)
# s2 = Student("Rohit", 21, 66)
# s3 = Student("Amit", 22, 67)
s1.display()