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

    def calculate(self):
        sum = 0
        for val in self.marks:
            sum += val