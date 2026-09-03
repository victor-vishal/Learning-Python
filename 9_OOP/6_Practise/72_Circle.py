# Define a class Circle to create a circle with radius r using the constructor
# define area and perimeter methods to calculate the area and perimeter of the circle respectively.

class Circle:
    def __init__(self,r):
        self.radius = r
        print("Created a circle with radius {r}")

    def area(self, r):
        area = 3.14*r*r
        print("Area of cirlce: ", r)

    def peri(self, r):
        perimeter = 2*3.14*r
        print("Perimeter of circle: ", perimeter)

c1 = Circle(5)
c1.area(5)
c1.peri(5)