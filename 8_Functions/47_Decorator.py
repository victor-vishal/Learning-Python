# A Python decorator is a function that takes another function as an argument, extends its behavior, and returns a new function without modifying the original function's source code.

# assigning a function to a variable
def sum(a,b):
    print((a+b))

c= sum
c(1,2)

print("--------------------------------------------------")
# passing a function as an argument to another function

def twice(func):
    func()
    func()

def greet1():
    print("Hi!")

twice(greet1)

print("\n\n--------------------------------------------------")

def runTwice(func):
    def wrapper():
        func()
        func()
    
    wrapper()

def greet2():
    print("Hi!")

runTwice(greet2)

print("\n\n--------------------------------------------------")

def runTvise(func):
    def wrapper():
        func()
        func()

    return wrapper

def greet3():
    print("Hi")

greeting = runTvise(greet3)
greeting()


print("\n\n--------------------------------------------------")
def run2wice(func):
    def wrapper():
        func()
        func()
    return wrapper

def greet4():
    print("Hi")

greeting = run2wice(greet4)
greeting()

