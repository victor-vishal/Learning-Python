def revcount(num):
    x=1
    while(x<=num):
        yield x
        x +=1

# for number in revcount(5):
#     print(number)

lst1=[]
for n in revcount(4):
    lst1.append(n)

print(lst1)


x =  revcount(5)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x))


















# def revcount(num):
#     x=1
#     while(x<=num):
#         yield x
#         x +=1

# # for number in revcount(5):
# #     print(number)

# lst1=[]
# for n in revcount(4):
#     lst1.append(n)

# print(lst1)


# x =  revcount(5)

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# # print(next(x))