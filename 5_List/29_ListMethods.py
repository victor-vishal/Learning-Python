#List Methods
#List methods are built-in functions that can be used to perform various operations on lists
#dir(list) will give you a list of all the methods available for lists in python
print(dir(list))#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#append()       method is used to add an element at the end of the list
#syntax: list.append(element)
#it only adds the element at the end
myList = [1, 2, 3]
print(f"Before appending: {myList}")
myList.append(4)
print(f"After appending: {myList}")


#pop()          to remove an element from the list 
#by default it removes the last
#but if we provide an index it will remove the element at that index
#syntax: list.pop(index) or list.pop() to remove the last element
myList.pop(1) #removes the element at index 1 from the list and returns it
print(f"After popping: {myList}")


#copy()         to create a copy of the list
#syntax: list.copy()
a = [1, 2, 3]
b = a.copy() #creates a copy of list a and assigns it to b
print(f"List a: {a}")
print(f"List b: {b}")

#clear()        to remove all the elements from the list
b.clear() #removes all the elements from list b
print(f"After clearing list b: {b}")

#count()        to count the number of occurrences of an element in the list
#syntax: list.count(element)
b = [1, 2, 3, 1, 2, 1]
num = b.count(1) #counts the number of occurrences of 1 in list b and assigns it to num
print(f"Number of occurrences of 1 in list b: {num}")

#extend()       to add all the elements of an iterable (like a list) to the end of the list
#syntax: list.extend(iterable)
a = [1, 2, 3]
b = (4, 5, 6)
a.extend(b) #adds all the elements of tuple b to the end of list a
print(f"After extending list a with tuple b: {a}")

#index()        to find the index of the first occurrence of an element in the list
#syntax: list.index(element)
a = [1, 2, 3, 4, 5, 3]
index = a.index(3) #returns the index of the first occurrence of 3 in list a
print(f"Index of the first occurrence of 3 in list a: {index}")

#insert()       to insert an element at a specific index in the list
#syntax: list.insert(index, element)
a = [1, 2, 3]
a.insert(0, "YO") #inserts "yo" at index 0 and shifts all the other elements to the right
print(f"After inserting 'YO' at index 0 in list a: {a}")

#remove()       to remove the first occurrence of an element from the list
#syntax: list.remove(element)
a =[1, 3, 6, 7, 4, 3]
a.remove(3) #removes the first occurrence of 3 from list a
print(f"After removing the first occurrence of 3 from list a: {a}")

#difference between pop() and remove()
#pop() removes an element at a specific index and returns it, while remove() removes the first occurrence of a specific element from the list
#pop() can be used to remove an element at a specific index, while remove() can only be used to remove the first occurrence of a specific element from the list
#pop() accepts an index as an argument, while remove() accepts an element as an argument

#reverse()      to reverse the order of the elements in the list
#syntax: list.reverse()
a = [1, 2, 3, 4, 5]
a.reverse() #reverses the order of the elements in list a
print(f"After reversing list a: {a}")

#sort()         to sort the elements of the list in ascending order
#syntax: list.sort()
a = [5, 2, 3, 1, 4]
a.sort() #sorts the elements of list a in ascending order
print(f"After sorting list a: {a}")
#sort() can also be used to sort the elements of the list in descending order by passing the reverse=True argument
a.sort(reverse=True) #sorts the elements of list a in descending order
print(f"After sorting list a in descending order: {a}")


#when a method returns an item, we can store that item in a variable and use it later
#for example, the pop() method returns the element that was removed from the list, so we can store that element in a variable and use it later
a = [1, 2, 3, 4, 5]
popped_element = a.pop() #removes the last element from list a and stores it in popped_element
print(f"Popped element: {popped_element}")