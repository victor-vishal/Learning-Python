a=float(input("Enter first number : "))
b=float(input("Enter second number : "))
operator = input("Enter operation to perform : +, -, *, /  : ")

if operator == "+":
    print(f"{a} {operator} {b} = {a+b}")
elif operator == "-":
    print(f"{a} {operator} {b} = {a-b}")
elif operator == "*":
    print(f"{a} {operator} {b} = {a*b}")
elif operator == "/":
    print(f"{a} {operator} {b} = {a/b}")

else:
    print("Invavlid operator")