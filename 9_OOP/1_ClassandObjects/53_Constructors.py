# __init__ method is called a constructor
# it is always excuted when an object of a class is created

# even if we do not define a constructor in our class, python provides a default constructor for us

# objectname = ClassName()  # the parenthesis here are actually used for calling the constructor of the class

#eg
class Student:
    name = "Vishal"
    def __init__(self):#constructor always takes self as first argument
        print("Constructor is called")
        print(self)#<__main__.Student object at 0x000001FB5DF586E0>

s1 = Student()  # here the constructor is called automatically
#thus the print statement is executed

# the self keyword act as a place holder for the object that will be created.
# it points or refrences the object that is created from the class

print(s1)#<__main__.Student object at 0x000001FB5DF586E0>
#as we can see printing s1 and self gives the same output, 

#although its not necessary to call the first argument self, it is just a convention, we can call it anything
print("\n\n\n")
class Teacher:

    def __init__(self, TeacherName, TeacherAge, subject):
        print("Constructor is called... A new teacher object is created")
        self.name = TeacherName
        self.age = TeacherAge
        self.subject = subject
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Subject: {self.subject}")

Teacher1 = Teacher("Vishal", 20, "Python")
print(Teacher1.name)
# to access the attributes or properties of the class we use the dot operator
Teacher1.display()