class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def showNumber(self):
        print(f"{self.real} + {self.image}i")

    def add(self, num2):
        newReal = self.real + num2.real
        newImage = self.image + num2.image
        # print(f"Sum of two complex numbers is: {newReal} + {newImage}i")
        return Complex(newReal, newImage) # returning a new object of Complex class
c1 = Complex(2, 3)
c1.showNumber() # 2 + 3i
c2 = Complex(5, 6)
c2.showNumber() # 5 + 6i

# c1.add(c2) # Sum of two complex numbers is: 7 + 9i

c3 = c1.add(c2) # returning a new object of Complex class
c3.showNumber() # 7 + 9i
