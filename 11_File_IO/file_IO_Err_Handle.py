"""
Error Handling in file IO
 - IOError occurs when the machine is having issue reading, or writing a file.
"""


def file_IO():
    try:
        # if file do exist, read it:
        with open('./files/file_E.txt', mode='r') as file:
            file_e = file.read()

    except FileNotFoundError as err:

        print('File not found!')
        print('Creating new file now..')

        # if the file does not exist, then create a new one
        with open('./files/file_E.txt', mode='w') as file1:
            file1.write('This is file E!')

        # read the newly created file:
        with open('./files/file_E.txt') as file2:
            file2 = file2.read()

            print(f'Reading file:\n{file2}')

    except IOError as err:
        print('IO Error')
        raise err

    except ValueError as err:
        print('Value Error')
        raise err

    else:
        # if file do exist, print it out to console:
        print(file_e)


file_IO()
