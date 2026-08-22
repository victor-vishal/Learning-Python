#methods are functions that belong to a specific data type. In this case, we will be looking at string methods. String methods are built-in functions that can be used to manipulate and work with strings in Python.
#String methods are called using the dot notation, where the method name is preceded by the string variable or string literal.

#Instead of calling a function and passing the string as an argument, we can call the method directly on the string variable or string literal.
#for example

string1 = "Apple and Banana"
String2 = "Fruits"

print(len(string1))  # Output: 16
# print(string1.len())# gives error
#len is a standalone function and not a method of string

print(dir(str))  # Output: list of all string methods available in Python
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(len in dir(str))  # Output: 68 (number of string methods available in Python)
print(string1.__len__())

#when we call len() on string... BTS it calls the __len__() method of the string class and returns
#it happens because of polymorphism...
#so the same function is used for multiple data types

#Different ways to call string methods
print(string1.upper())  # Output: "APPLE AND BANANA"
string3 = "Hello, World!".lower()  # Output: "hello, world!"
print(string3)
