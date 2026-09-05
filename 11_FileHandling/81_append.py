with open("11_FileHandling/file2.txt", "a+") as file:
    file.write("\nThis is the appended Text!")
    # print(file.read())#prints null
    # in append cursor is sent to last, to insert text
    file.seek(0)
    print(file.read())
