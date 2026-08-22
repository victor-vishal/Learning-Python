# Dictionary comprehension
# Dictionary comprehension is a concise way to create a dictionary

#SYNTAX
# {key: value for item in iterable if condition}

# Example 1: Create a dictionary of squares
squares = {x: x**2 for x in range(1,11)}
print(squares)