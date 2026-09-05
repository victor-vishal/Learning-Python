# Synatx
# open('filename', 'mode')

file = open(r"11_FileHandling\file.txt", "r")#r before the path is used for telling python its a raw string, otherwise it treasts \ as an escape character.
# or use / or \\ in the path instead of \

print(file.read()) #reads the entire file
print("================================")
# print(dir(open)) 
# print(file.readline()) #reads the first line of the file
#BUT RETURNS empty string, as cursor is at the end of file, need to reset cursor
# print("================================")

# print(file.readlines()) #reads all the lines of the file and returns a list of lines
# print("================================")

#file.read() reads the entire file and puts the cursor at the end of the file, so if we call file.read() or file.readline() again, it will return an empty string. 
# to fix this we reset curson to the begining of the file using file.seek(0)
file.seek(0) #resets the cursor to the begining of the file
print(file.readline()) #reads the first line of the file 
print("================================")
file.seek(0)
print(file.read(10)) #reads the first 10 characters of the file


file.close() #closes the file/ releases the resource

#
