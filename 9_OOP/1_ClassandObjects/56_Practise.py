# Create a student class that take name and marks of 3 subjects as arguments in constructor and create a method to calculate the total marks and percentage of the student

# class Student:
#     def __init__(self, english, hindi, maths):
#         self.english = english
#         self.hindi = hindi
#         self.maths = maths

#     def calculate(self):
#         total = self.english + self.hindi + self.maths
#         percent = (total / 300) * 100
#         return total, percent

# # Create an object of the Student class and call the calculate method
# student1 = Student(85, 90, 95)
# total_marks, percentage = student1.calculate()
# print(f"Total Marks: {total_marks}")
# print(f"Percentage: {percentage:.2f}%")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Created Student "+ self.name+" \n")

    def calculate(self):
        sum = 0
        for val in self.marks:()
        avg = sum/len(self.marks)
        percentage = (sum/(len(self.marks)*100))*100

        print(f"Hi Student {self.name} !! \n Total Marks: {sum} \n Your Average:{avg}\n Your Percentage {percentage}\n\n")

s1 = Student("Vikor", (98, 92, 95, 100, 50))
s2 = Student("Shubham", (100, 55, 98, 40))

s1.calculate()
s2.calculate()

