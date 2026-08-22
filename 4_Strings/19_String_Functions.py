#Functions of strings
#1. len() - returns the length of the string
string = "Hello, World!"
print(len(string))  # Output: 13 includes every character

#2. lower() - converts the string to lowercase
print(string.lower())  # Output: "hello, world!"

#3. upper() - converts the string to uppercase
print(string.upper())  # Output: "HELLO, WORLD!"

#4. strip() - removes any leading and trailing whitespace
string_with_whitespace = "   Hello, World!   "
print(string_with_whitespace.strip())  # Output: "Hello, World!"

#5. replace() - replaces a specified phrase with another specified phrase
print(string.replace("World", "Python"))  # Output: "Hello, Python!"
#6. split() - splits the string into a list where each word is a list item
print(string.split())  # Output: ['Hello,', 'World!']

#7. find() - searches the string for a specified value and returns the position of where it was found
print(string.find("World"))  # Output: 7 (index of the first character of "World")