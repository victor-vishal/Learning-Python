# Dictionary is a data structure that stores information in key-value pairs.
# Keys must be unique and of immuatable data types(strings, tuples etc)
# while, values can be of any data type whether mutable or immutable
# i,e the values can be string, int, tuples(), list[] or even a whole dictionary {}

# Properties
# Mutable
# unordered till version 3.7 then became ordered in later versions
# Dynamic (variable size)

#Dictionaries are used to access data by a name(key) rather than a numeric position (index) in a list
# 
# SYNTAX:
# dictionary_name = {key1: value, key2: value, key3: value}

data = {
    "Name": "Vishal Pandey", "age": 20, "DOB": "27-11-2005", "other":(1,2,3,4)
    }
#values can be of any datatypes, tuples, list, dictionary

print(data)
 
#if key value is not unique then the last value will be considered for that key
#[updation]
data = {"Name": "Vishal Pandey", "age": 20, "DOB": "27-11-2005", "age": 21}
print(data)
 
# Creation using dict() constructor 
# SYNTAX 
# dictionary_name = dict(key1=value, key2=value)
b = dict(name="Sam", age=20)
print(b)