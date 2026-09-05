file = open("11_FileHandling/file2.txt","w")

text = input("Enter some text to put in a file: ")
file.write(text)

# print("You entered ", file.read()) #error because file is opened in write mode only
# to fix this either close and reopen the file in read mode or open the file in read and write mode "r+"

file.close() 

file = open("11_FileHandling/file2.txt","r+")
print("You entered: ", file.read())

content = input("Enter some more text to append to the file: ")
file.write(content) #appends the content to the file, but cursor is at the end of the file, so if we call file.read() again, it will return an empty string.
file.seek(0) #resets the cursor to the begining of the file

file.read()
file.close()