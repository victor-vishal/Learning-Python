# not closing an opened file can lead to issues like data corruption, memory leaks, and resource exhaustion. 

# with statement automatically closes the file after the block of code is executed,

with open("11_FileHandling/file2.txt","r") as file:
    print(file.read()) #file is automatically closed after this block of code is executed