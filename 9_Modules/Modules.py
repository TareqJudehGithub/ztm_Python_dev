# imports
import name

"""
Modules in Python

- Modules are simply just Python files.
- __pycache__
    __pycache__ is created everytime we run a script (file) with import statement.


- Packages In Python
    - A package is folder containing files.
        /folder_name/file_name.py

__main__
    # Only run code of the MAIN file, so that we make sure no other modules
      are executed but the main one.
    if __name__ == "__main__":
        print("Hello, world!")    
"""

# Only run code of the MAIN file
if __name__ == "__main__":

    print('This is the main file')

    print('')
    print(name)
    print(f'printing __main__: {__name__}')


