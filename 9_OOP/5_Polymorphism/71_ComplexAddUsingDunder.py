class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def showNumber(self):
        print(f"{self.real} + {self.image}i")

    def __add__(self, num2): #just change this add to __add__ and now we can use + operator to 
        newReal = self.real + num2.real
        newImage = self.image + num2.image
        return Complex(newReal, newImage) # returning a new object of Complex class

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImage = self.image - num2.image
  
        return Complex(newReal, newImage) # returning a new object of Complex class
c1 = Complex(2, 3)
c1.showNumber() # 2 + 3i
c2 = Complex(5, 6)
c2.showNumber() # 5 + 6i

c3 = c1 + c2 # now we can use + operator to add two complex numbers
c3.showNumber() # 7 + 9i

c4 = c1 - c2 # now we can use - operator to subtract two complex numbers
c4.showNumber() # -3 + -3i


#in short working of + or - operator is defined in the class using dunder methods __add__ and __sub__ respectively. 
# so when we do c1+c2, it is internally calling c1.__add__(c2) and returning a new object of Complex class.