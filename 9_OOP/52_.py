#class classname: or class classname(): does the same thing!


class Car:
    def set_details(self, color, brand):
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f"This Car is {self.color} {self.brand}")


car1=Car()
car1.set_details('Blue', 'BMW')
car1.show_details()

car2=Car()
car2.set_details("Red", "Mustang")
car2.show_details()