# Functions in python are defined using the def keyword.

# SYNTAX:
# def function_name(parameters):
#    """docstring"""  # optional
#    # function body
#    return value  # optional

def greet(name):
    """This function greets the person passed in as a parameter.""" #these are called docstrings, they are used to describe the function and its purpose.
    print(f"Hello, {name}!")

# unlike regular comments, docstrings are accessible through the __doc__ attribute of the function. For example, you can access the docstring of the greet function like this:
print(greet.__doc__)  # Output: This function greets the person passed in as a parameter.

greet(input("Please Enter your name: "))

# Return statement in functions
# it is used for exiting the function and returning a value to the caller.
# if there is no return statement, the function will return None by default.

# difference between print and return:
# print is used to display the output on the console, while return is used to send a value back to the caller of the function.
# when a function is called, the code inside the function is executed, and the return value is sent back to the caller. The caller can then use this return value for further processing or display it.


