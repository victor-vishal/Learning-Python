# local and global variables

# local variables are defined inside a function and can only be accessed within that function. They are created when the function is called and destroyed when the function is exited.

# Global variables are defined outside of any function and can be accessed from anywhere in the code. They are created when the program starts and destroyed when the program ends.

# for example
def myFunction():
    local_var = "I am a local variable"
    print(local_var, global_var)

global_var = "I am a global variable"
myFunction()  # Output: I am a local variable I am a global variable
# print(local_var)  # This will raise an error because local_var is not defined outside