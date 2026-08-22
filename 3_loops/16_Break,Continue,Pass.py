#Break statement is used to exit a loop when a certain condition is met.
# It can be used in both for and while loops.

print("Using break statement:")
for i in range(10):
    if i == 5:
        break
    print(i)


#Continue statement is used to skip the current iteration of a loop and move to the next iteration.
print("\nUsing continue statement:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#Pass statement is used as a null operation, it does nothing when executed.
print("\nUsing pass statement:")
for i in range(10):
    if i == 5:
        pass
    print(i)