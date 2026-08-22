passing a function as an argument to another function

def twice(func):
    func()
    func()

def greet():
    print("Hi!")

twice(greet)