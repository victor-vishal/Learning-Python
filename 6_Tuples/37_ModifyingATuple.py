# Since tuples are immutable (they can't be changed after creation
# Convert the tuple to a list using list().
# Modify the list (add, remove, or change items).
# Convert it back to a tuple using tuple().

x = ("apple", "banana", "mango", "cherry")
print("tuple: ", x)

y = list(x)#creates a new object
print("tuple to list:", y)
y.append("Aam falo ka raja h!!")
print("After appending/modifying: y list: ",y)

x = tuple(y)
print("List y to tuple,  assigned to x :",x)


