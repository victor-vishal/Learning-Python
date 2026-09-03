# Define a class Circle to create a circle with radius r using the constructor
# define area and perimeter methods to calculate the area and perimeter of the circle respectively.

class Circle:
    def __init__(self,r):
        self.radius = r
        print("Created a circle with radius ", r)

    def area(self):
        area = 3.14 * self.radius ** 2
        return area

    def peri(self):
        perimeter = 2*3.14*self.radius
        return perimeter

c1 = Circle(5)
print(f"Area:  {c1.area():.2f}")
# print("Perimeter: ", c1.peri())#31.400000000000002
print(f"Area: {c1.peri():.2f}") #31.40