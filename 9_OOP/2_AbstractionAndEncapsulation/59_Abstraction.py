#Abstraction is a process of hiding the implementation details and showing only functionality to the user.

# For Example a driver only needs to know how to drive a car, not how the engine works.

class Car:
    def __init__(self):
        self.accl = False
        self.brake = False
        self.clutch = False

    def start(self):
        self.accl = True
        self.brake = False
        self.clutch = False
        print("Car started")

    def stop(self):
        self.accl = False
        self.brake = True
        self.clutch = True
        print("Car stopped")

c1 = Car()
c1.start()