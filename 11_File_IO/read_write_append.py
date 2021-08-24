"""
 - mode='r'     read file.  Mode is read by default
 - mode='r+'    read and write to file.
 - mode='w'     writes to file. automatically creates the file if not already
                exist, and overrides existing one.
 - mode='a'     write new lines to an existing file.

"""
from pathlib import Path

p = Path('.')
print('\n')
print('file A')

# .read()
with open('file_A.txt', mode='r') as file:
    file_a = file.read()
    print(file_a)

print('\n')


# read + write
print('file B')
with open('file_B.txt', mode='r+') as file:
    file.write('This is file B!')

print('\n')

print('file C')
# .write()
with open('files/file_C.txt', mode='w') as file:
    file.write('This is file C!')

print('\n')

# .append()

print('\n')

with open('files/file_C.txt', mode='a') as file:
    file.write('\nAdding new line to file C using append() method!')


# Accessing files from other parent folder

with open('../files_folder_root/file_D.txt', mode='w') as file:
    file.writelines('This is file D!\n2nd line: hi there! \n3rd line: Hello world!')