# Property decocrator
# It lets you turn a method into a getter so you can access it like a regular attribute.

# for eg

class Area:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    @property
    def area(self):
        return self.length * self.breadth

a1 = Area(10, 20)
print(a1.area) # we called it like an attribute, thanks to the property decorator. 

# it also allows dynamic calculation of the area, if we change the length or breadth, the area will be calculated again when we access it.

#without decorator, 

class Area2:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = self.length * self.breadth

a2 = Area2(10, 20)
print(a2.area) # we have to call it like a method, not an attribute.
a2.length = 30
print(a2.area) # the area is still 200, 
# it can be fixed by making an area method

class Area3:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

#the only difference in Area3 and Area is that we have to call the area method like a method, not an attribute.
a3 = Area3(10, 20)
print(a3.area()) # we have to call it like a method, not an attribute.
a3.breadth = 30
print(a3.area()) # the area is now 300, but we have to call it like a method, not an attribute.