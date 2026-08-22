#Methods in dictionary are built in functions that perform specific operations on the dictionary.
data = {"Name": "Vishal Pandey", "age": 20, "DOB": "27-11-2005"}

print("\n")
#GET
#get() method is used for returning value of the specified key.
#Syntax: dict.get(key, default=None)
print(data.get("Name")) #Output: Vishal Pandey
print(data.get("Name1")) # if key doesn't exist it will return None
# we can also specify a default value to return if the key doesn't exist
print(data.get("Name1", "Key not found")) #Output: Key not found
#syntax: dictionary_name.get(key, default_value_to_return_if_key_not_found)


print("\n")
#KEYS
# key() is a method that returns a view object that displays a list of all the keys in the dictionary.
# a view object is a dynamic view of the dictionary's keys, which means that if the dictionary changes, the view object will reflect those changes.

print(data.keys()) #Output: dict_keys(['Name', 'age', 'DOB'])
                        #here in dict_key is a view object
#keys() method accepts no parameters and retrievs all the keys

key = list(data.keys()) # converting the view object to a list
print(key) #Output: ['Name', 'age', 'DOB']


print("\n")
#VALUES
# values() is a method that returns a view object that displays a list of all the values in the dictionary.
print(data.values()) #Output: dict_values(['Vishal Pandey', 20, '27-11-2005'])
#values() method accepts no parameters and retrievs all the values

print(f"Values in the dictionary in list format: {list(data.values())}")

print("\n")
#ITEMS
# items() is a method that returns a view object that displays a list of all the key-value pairs in the dictionary as tuples.

print(data.items()) #Output: dict_items([('Name', 'Vishal Pandey'), ('age', 20), ('DOB', '27-11-2005')])
#items method accepts no parameters and retrievs all the key-value pairs as tuples
print(f"Items in the dictionary in list format: {list(data.items())}")

print("\n")
# POP
# pop() method removes the a specified key and returns its both key and value...
print(data.pop("Name")) #Output: Vishal Pandey
print(data) #Output: {'age': 20, 'DOB': '27-11-2005'}



print("\n")
# POPITEM
# popitem() method removes the last item(key-value pair) inserted in the dictionary and returns it as a tuple.
print(data.popitem()) #Output: ('DOB', '27-11-2005')
print(data) #Output: {'age': 20}



print("\n")
#CLEAR
# clear() method removes empty the whole dictionary

data1 = {"Name": "Vishal Pandey", "age": 20, "DOB": "27-11-2005"}
print(data1) #Output: {'Name': 'Vishal Pandey', 'age': 20, 'DOB': '27-11-2005'}
data1.clear()
print(data1) #Output: {}