# def decorator(func):
#     def wrapper():
#         print("Starting Wrapper")
#         func()
#         print("Ending Wrapper")
    
#     return wrapper

# def mf():
#     print("this is the main function")

# variable = decorator(mf)
# variable()


# STEP 1: Define the decorator function.
# It acts as a "factory" that takes an existing function object as an argument.
def decorator(func):
    
    # STEP 2: Define an inner function called 'wrapper'.
    # This is the "gift box" that will wrap around the original function.
    def wrapper():
        print("Starting Wrapper")  # Injected code BEFORE the main function runs
        
        func()                     # Triggers the original function that was passed in
        
        print("Ending Wrapper")    # Injected code AFTER the main function runs
    
    # STEP 3: Return the wrapper function object ITSELF.
    # CRUCIAL: No parentheses '()' here! We are returning the "machine" itself,
    # not running it yet. This allows us to store it for later use.
    return wrapper


# STEP 4: Define the plain, standalone function.
# This function is completely unaware of any wrapper logic on its own.
def mf():
    print("this is the main function")


# STEP 5: Pass 'mf' into the decorator and catch what it returns.
# Because the decorator returns the unexecuted 'wrapper' function, 
# 'variable' now literally becomes the 'wrapper' function.
variable = decorator(mf)


# STEP 6: Execute the wrapped code.
# Putting '()' after 'variable' finally triggers the code inside 'wrapper',
# which prints the start line, jumps to 'mf()', and prints the end line.
variable()