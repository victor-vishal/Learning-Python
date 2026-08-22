list1 = [1, 2, 3]
list2 = list1 #list2 is an alias of list1

#unlike in other programming languages here list2 is not a copy of list1
#both list1 and list2 point to the same memory location where the list is stored
#Thus change list 2 will affect list1 as well

print(f"Before updating: {list1}, {list2}")
list2[0] = 10
print(f"After updating list2[0] = 10: {list1}, {list2}")

#to prevent this and to create an actual copy of the list we can use the copy() method of list

list3 = list1.copy() #creates a shallow copy of list1
print(f"Before updating: {list1}, {list3}")
list3[0] = 100
print(f"After updating list3[0] = 100: {list1}, {list3}")

#Here list 1 and list2 are still pointing to the same memory but list3 is pointing to a different memory location where the copy of list1 is stored
#Unlike in other programming languages, variables in python don't act like buckets that hold data, intead they are like labels
