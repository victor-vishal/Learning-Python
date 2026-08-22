#Nested loops are loops inside loops,
#the inner loop is executed for each iteration of the outer loop.
#syntax:
# for variable in sequence:
    # for variable in sequence:
        # code to be executed

#for Example:
for i in (0,2):
    for j in (0,3):
        print(f"{i}, {j}")
#this prints: 0,0 0,3 2,0 2,3
#its because we have not used range function
#thus the number passed are treated as a single element in the sequence or tuples
print("\n\n")
#we can also use range function in nested loops

for i in range(1,3): #from 1 to 2
    for j in range(2,4):#from 2 to 3
        print(f"{i}, {j}")

for i in range(1,4):
    j = 1
    while j<=i:
        print("*", end=" ")
        j+=1
    print() #this is used to move to the next line after each iteration of the outer loop
print()
#printing a pattern using nested for loop
for i in range(1,6):
    for j in range(1, i+1):
        print("*", end=" ")
    print() #this is used to move to the next line after each iteration of the outer loop