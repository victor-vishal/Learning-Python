# Loops in dictionary
# We can use loops to iterate through the keys, values, or key-value pairs of a dictionary

data = {"Name": "Vishal", "Age": 25, "City": "New York", "Occupation": "Software Engineer", "Skills": ["Python", "Java", "C++"]}

for i in data:
    print(i) # prints the keys of the dictionary
print("\n")

for i in data.keys():
    print(i) # prints the keys of the dictionary
print("\n")

for i in data.values():
    print(i) # prints the values of the dictionary
print("\n")

for i in data.items():
    print(i) # prints the key-value pairs of the dictionary as tuples
print("\n")

for key, value in data.items():
    print(f"{key}: {value}") # prints the key-value pairs of the dictionary in a formatted way