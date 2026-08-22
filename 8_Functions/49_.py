# def decorator(func):
#     def wrapper():
#         print("Starting Wrapper")
#         func()
#         print("Ending Wrapper")
#     return wrapper
# @decorator
# def mf():
#     print("this is the main function")

# mf()





# STEP 1: The decorator function definition remains exactly the same.
# It still expects a function object as an input parameter ('func').
def decorator(func):
    def wrapper():
        print("Starting Wrapper")
        func()
        print("Ending Wrapper")
    return wrapper


# STEP 2: Use the '@' shortcut (Syntactic Sugar).
# This tells Python: "Take the 'mf' function below, automatically pass it 
# into 'decorator', and overwrite the name 'mf' with the returned wrapper."
# Effectively doing: mf = decorator(mf) behind the scenes.
@decorator
def mf():
    print("this is the main function")


# STEP 3: Call the function normally.
# Because the name 'mf' was automatically replaced with the wrapper, 
# calling 'mf()' now triggers the entire decorated execution sequence.
mf()

# in short this means that when mf() is called, it does the same thing as calling decorator(mf)


# to call mf without decorator we can use the .__wrapped__() 

# mf.__wrapped__()