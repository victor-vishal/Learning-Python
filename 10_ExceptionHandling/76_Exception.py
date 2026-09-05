# Exception are errors detected during execution. 
# Exception Handling is a mechanism to handle these errors and prevent the program from crashing.

# zeroDivisionError: # n/0

# TypeError: # 56 + "HI" 
# operation or function is applied to an object of an inappropriate data type

# ValueError: # int("HI")

# It has 3 blocks: try, except, finally
# try contains the code that may raise an exception
# except contains the code that will be executed if an exception occurs in the try block
# finally contains the code that will be executed regardless of whether an exception occurs or not. 
# used for clean up actions

# n = int(input("Enter a number: "))
# print(1/n) # if n = 0 
# Zero Division error, programs stops

try:
    n = int(input("Enter a number :"))
    print(1/n)
except ZeroDivisionError:
    print("Enter a non zero number!")#entering 0
except TypeError:
    print("Enter a number only") #String like HI
except ValueError:
    print("Enter a valid number") #69h
finally:
    print("Cleaning up resources") #executed in all cases, even if there is no exception

# Custom Exception: We can create our own exception by creating a new class that inherits from the built-in Exception class.

try: 
    n = int(input("Enter a number :"))
    if n < 0:
        raise Exception("Negative numbers are not allowed") #raise is used to raise an exception
    print(1/n)

except Exception as e: # e is the exception object
    print(e) #prints the message of the exception