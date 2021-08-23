"""
 - mode='r'     read file.  Mode is read by default
 - mode='r+'    read and write to file.
 - mode='w'     writes to file. automatically creates the file if not already exist.
 - mode='a'     write new lines to an existing file.

"""
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
with open('file_C.txt', mode='w') as file:
    file.write('This is file C!')

print('\n')

# .append()

print('\n')

with open('file_C.txt', mode='a') as file:
    file.write('\nAdding new line to file C using append() method!')
