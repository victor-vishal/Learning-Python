data = {"Name": "Vishal Pandey", "age": 20, "DOB": "27-11-2005"}
# Access using square brackets
print(data)

# ACCESS
# dictionary_name[Key]
print(data["Name"])

# using get() method for multiple keys SYNTAX: dictionary_name(key1, key2)
print(data.get("Name", "age"))

#Insertion      SYNTAX: dictionary_name[key] = value
data["Weight"]=65
print(data)

#Updation   SYNTAX: dictionary_name[key] = value
#updation and insertion have same syntax, 
# if the key is already present then it will update the value otherwise it will insert a new key-value pair

data["age"]=21
print(data)

# Deletion
# we use del keyword to delete a key-value pair from the dictionary
# SYNTAX: del dictionary_name[key]
print(f"Before deleting {data}")
del data["DOB"]                         # Before deleting {'Name': 'Vishal Pandey', 'age': 21, 'DOB': '27-11-2005', 'Weight': 65}
print(f"After Deleting {data}")         # After Deleting {'Name': 'Vishal Pandey', 'age': 21, 'Weight': 65}


