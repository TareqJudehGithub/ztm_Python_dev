"""
FILE I/O   (input/output)
 - I/O means to input something from the outside world, and output something
   into the outside world.
 - Example of I/O is inputting an image, and outputting it in a different format.
 - open is a built-in function to read and write files.
 - Using open demands closing any opened file using .close() method
 - with built-in function auto-close opened files
"""
# assign a txt file to a python variable
file_1 = open('test_file.txt')

# .read() method to read files
# print(file_1.read())

# We could also use readline() to read a line..just one line.
# print(file_1.readline())    # reads the first line
# print(file_1.readline())    # reads the next line

# Or, readlines() to read the whole contents of a file.
print(file_1.readlines())

# opened files should be closed after being done with them, to save memory and
# prevent memory leakage.
file_1.close()

