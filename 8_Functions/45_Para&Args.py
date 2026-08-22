# Parameters and Arguments
# Parameters are the variables that are defined in the function definition. They are used to receive the values that are passed to the function when it is called.

# Arguments are the values that are passed to the function when it is called. They are used to provide the values for the parameters defined in the function.

# for example,

def add(a, b):
    return a+b

add(5,3)  # Here, a and b are parameters, and 5 and 3 are arguments.

# in short values passed while calling a function - arguments
# values defined in the function definition - parameters


print("\nTYPES of Arguments:")
# TYPES of Arguments:
# 1. Positional Arguments: These are the most common type of arguments. They are passed to the function in the same order as the parameters are defined in the function.
print("\n1. Positional Arguments:")
def yourName(name, age):
    print(f"You are {name} and you are {age} years old!!")
#in this type, the order of arguments matters.
# if we call the function like this:
yourName("Alice", 30)  # Output: You are Alice and you are 30 years old!!
# if we call the function like this:
yourName(30, "Alice")  # Output: You are 30 and you are Alice years old!!

# we can fix this by explicity defining the parameter using = that is Keyword Arguments

# 2. Keyword Arguments: These are the arguments that are passed to the function using the parameter names. They can be passed in any order.
print("\n2. Keyword Arguments:")
yourName(name="Alice", age=30)  # Output: You are Alice and you are 30 years old!!

# 3. Default Arguments: These are the arguments that have default values. If the caller does not provide a value for a default argument, the default value will be used.
print("\n3. Default Arguments:")

# default are defined in the function definition using the = operator with parameter name. 
# it used as default value when no argument is passed for that parameter.

def greet(name="Guest"):
    print(f"Welcome back, {name}!")
# here Guest is the default value for the parameter name. 
# so if no argument is passed, then the default value will be used and error won't arise

greet()  # Output: Welcome back, Guest!
greet("Vishal")  # Output: Welcome back, Vishal!