import typing

"""
Functions
    - functions eliminates code repetition
    - functions returns an expression or modifies a variable
    Function structure
    # function head (parameter)
     def (define) say_hello():
        # function body
        print('hello')

    # call the function (arguments)
    say_hello()

    arguments vs parameters
    - arguments are used as the actual values we provide for a function
    - parameters are used when we define the function (in the function header)
    - positional arguments/parameters are arguments/parameters that are required
      to be in specific position
    - keyword arguments assign a value for each argument
    - default parameters assigns a default value for a parameter, in case no argument
      were assigned. Assigning an argument in the function call though overrides the
      default parameter.
    - return keyword returns an expression and exit the function (ignore lines below return)
    - Methods vs Functions
        - functions (like list(), print(), and sum()) are not associated with any object.
        - Methods are built-in associated with the objects of the class they belong to.
    - Docstrings in functions
        Docstrings describes a function in a comment form, using triple double quotation.
    - Clear code
    - *args and **kwargs
    - Parameters and arguments order:
        params, *args, default params (name='John'), **kwargs
    - Scopes.  Who has access to who?
        - Scopes reserves resources like memories(RAM), help prevent crashes, and run our
          application efficiently.
        - Python interpreter execution rules it follows:
            1. *local scope. Return the local scope if found
            2. Parent local scope. Return the Parent local scope.
            3. Global scope. if neither a local or a parent local scope were founds, then
               return the global scope.
            4. Built-in defined functions.
                  
        - global keyword. A way to access global variables inside functions. However, global
          keyword usage can be confusing as files get bigger and bigger. A better way is to 
          use dependencies injections by using the global variable as parameter for the 
          function.
        - nonlocal keyword. Assigns a new value to parent/local variable. Again, try avoiding
          the nonlocal keyword as it causes confusion and makes code less predictable and less
          clean.
        
            
    
    * Local scope is a scope that is a part of a function.
    
        
    



"""


# positional arguments/parameters
def greet(name: str, emoji: str) -> str:  # function head(parameters)
    # function body
    return f'Hello, {name}!'


# call/invoke the function
print(greet('John', 'smile'))

print('\n')


# keyword arguments
def hello_world(greetings, symbol):
    return greetings + symbol


print(hello_world(greetings='Hello world', symbol='!'))

print('\n')


# default parameters

def star_wars(char='BB8'):
    return f'Hello, {char}'


print(star_wars(char='Darth Vader'))

print('\n')


def arithmetic(num1, num2) -> int:
    return num1 + num2


print(arithmetic(5, 5))

print('\n')


# The below function here edits a variable (ele list)
def edit_list():
    ele[0] = 45


ele = [5, 10, 15]
edit_list()
print(ele)

print('\n')
print('Clear code')


# clean code

def is_odd_or_even(num):
    """Example of a clean code"""
    return num % 2 == 0
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False


print(is_odd_or_even(22))

print('\n')
print('*args and **kwargs')


def super_func(name: str, *args: int, friend='ali', **kwargs: int):
    """return the sum of all arguments"""
    print(name, friend)
    total = 0
    for v in kwargs.values():
        total += v
    return sum(args) + total
    # expected outcome = 35


print(super_func('john', 1, 3, 4, 5, 7, friend='micheal', num1=5, num2=10))

print('\n')
# scope
print('scope')

total = 200  # global scope


def total_func():
    total = 100  # local scope


print(total, '\n')  # >>> 200

a = 1  # global scope


def parent():
    a = 10  # parent local scope

    def confusion():
        return a

    return confusion()  # local scope


print(parent())
print(a)
print('\nglobal keyword')
total = 0


def count():
    global total
    total += 1
    return total


print(count())
print('')
counter = 0

def count2(counter):
    counter += 5
    return counter


print(count2(counter))
print('')
print('nonlocal keyword')
def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner: {}'.format(x))
    print('outer: {}'.format(x))
    inner()


outer()

print('\n')
print(format(1000, '0.2f'))
print('\n')

