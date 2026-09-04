# Exception Handling in Python is a mechanism to handle errors that occur during the execution of a program (run)
# Errors detected during execution are called exceptions

# Types of Errors
# 1. Compile Time Errors: [although Python is an interpreted language, here compile time errors refer to errors that are detected before the program is run]
# These are errors that occur during the compilation of the program. They are usually syntax errors, such as missing colons, parentheses, or incorrect indentation.

if 1==1
    print("Syntax error missing colon")  # This will raise a SyntaxError because of the missing colon after the if statement.



# 2. Runtime Errors: 
# These are errors that occur during the execution of the program. They can be caused by various factors, such as invalid input, division by zero, or accessing a non-existent file.

print(10/0)  # This will raise a ZeroDivisionError because we are dividing by zero.



# 3. Logical Errors: 
# These are errors that occur when the program runs without crashing, but produces incorrect results. They are usually caused by incorrect logic or algorithms in the code.
# Programs with logical errors will not raise any exceptions, but they will produce unexpected or incorrect output.

a=2, b=3
sum  = a*b
print("The sum of a and b is:", sum)  # Expected:5 output:6, Logic error because we used wrong operator


#errors in software are called bugs. 
# Debugging is the process of finding and fixing bugs in a program.