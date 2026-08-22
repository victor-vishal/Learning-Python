age = int(input("Please enter your age: "))

if age>= 18:
    print("You can vote.")

#in python insread of using else if we use elif
elif age<0:
    print("Invalid age.")

else:
    print("You cannot vote.")