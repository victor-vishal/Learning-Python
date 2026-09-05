# File Handling in Python is a way to read and write files. Python provides built-in functions to create, read, update, and delete files.

# There are two types of files in Python:
# Text files(.txt, .csv, .json, etc.) - store data in text format
# Binary files(.jpg, .png, .pdf, etc.) - store data in binary format

#syntax to open a file in Python:
# file_object = open("filename", "mode")

# Modes to open a file in Python:
# "r" - Read mode - Opens a file for reading (default mode)
# "w" - Write mode - Opens a file and overwrites the content or creates a new file
# "a" - Append mode - Opens a file and appends the content to the end of the file
# "x" - Exclusive creation - Creates a new file, gives error if the file already exists

#combination of modes can also be used:
# "r+" - Read and Write mode
# "w+" - Write and Read mode
# "a+" - Append and Read mode
# "x+" - Exclusive creation and Read mode


#THESE MODES define how the file will be opened, it is mostly used to define the type of file 
#  "b" - Binary mode - Opens a file in binary mode
#  "t" - Text mode - Opens a file in text mode (default)

# SINCE text mode is default, we dont need to specify it, thus we use w instead of wt
# but for binary files we need to specify it, and we use wb instead of w
# python is blind to extensions, thus we need to specify the type of file we are opening, 