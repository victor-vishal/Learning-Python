#String in python is immutable
#When we use a string method, it does not change the original string but returns a new string with the desired changes.
#It creates a new string with the modifications and leaves the original string unchanged.

#METHODS
#Boolean Methods
#Return either true or false based on the condition being checked
#Example: isalpha(), isdigit(), isspace(), islower(), isupper(), istitle(), isalnum() etc.
string1 = "123@Varun"
print(string1.isalnum())  # Output: False (because of the presence of '@' character)
string2 = "Varun123"
print(string2.isalnum())  # Output: True (because it contains only alphanumeric characters)



#String Manipulation Methods
#These methods are used to manipulate and modify strings in various ways.
#Example: upper(), lower(), title(), capitalize(), swapcase(), strip(), lstrip(), rstrip(), replace(), etc.
string3 = "   Hello, World!   "
print(string3.strip())  # Output: "Hello, World!" (removes leading and trailing whitespace)
print(string3.lstrip())  # Output: "Hello, World!   " (removes leading whitespace)
print(string3.rstrip())  # Output: "   Hello, World!" (removes trailing whitespace)
print(string3.replace("Hello", "Hi"))  # Output: "   Hi, World!   "

#other string methods include
#center(), count(), encode(), endswith(), expandtabs(), find(), format(), format_map(), index(), isidentifier(), join(), ljust(), maketrans(), partition(), removeprefix(), removesuffix(), rfind(), rindex(), rjust(), rpartition(), rsplit(), splitlines(), startswith(), swapcase(), title(), translate(), zfill() etc.

#startwith() and endswith() methods are used to check if a string starts or ends with a specific substring, respectively. They return True if the condition is met and False otherwise.
string4 = "Hello, World!"
print(string4.startswith("Hello"))  # Output: True
print(string4.endswith("!"))  # Output: True

print(string4.startswith("H"))  # Output: True
print(string4.endswith("d!"))  # Output: True
