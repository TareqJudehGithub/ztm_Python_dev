"""
Debugging
 - Debugging is the art of finding bugs and errors in our code.
 - Tips in finding bugs and errors
    1. linting
     - Built-in linting detects errors.
    2. USE IDE/Code editors
    3. print()
    4. Python Debugger (pdb) built-in library
    5. Python Debugger (pdb)
        - import pdb
        - import pdb.set_trace() to start debugging
        - pdb commands:
            - a returns a list of arguments.
            - w returns a line of code of where are at.




"""
import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


print(add(10, '5'))

