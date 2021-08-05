import random
import emoji
from time import time
"""
Decorators
 - Decorators supercharge our functions, adding extra functionality and features to it.

 Higher Order Function
  - A function that accepts inside of it another function as a parameter, or returns
    a function.
  - map(), filter(), and reduce() are all examples of higher order functions.
"""


def hello_world():
    print('Hello, world!')


def some_func(func):
    # call/run the function
    func()


some_func(hello_world)

print('')

'''
greet would still run even if we deleted hello, because greet is still pointing to
 the same location in memory. So, Python deletes the function hello, but not it's location
 in memory.  
 
 @decorator
 def func_name
 
 
'''

def hello():
    print('Hello there!')


greet = hello
del hello

greet()

print('')
print('==================')
# Decorator
print('# Decorator')
print('')




def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func


@my_decorator
def hello():
    print(f'Hellllooooo!')


hello()


print('')
print('Decorators with arguments')

username = random.choice(['Noor', 'Dina', 'Leen'])
# emoji = '\U0001F917'
emoj = emoji.emojize(':cat_with_wry_smile:')



def user_decorator(func):
    def wrapped_func(*args):
        print('<3')
        func(*args)
        print('<3')
    return wrapped_func


@user_decorator
def welcome_user(*args):
    print(f'Hello, {args}')


welcome_user(username, emoj)


print('')
print('We do we need Decorators?')
# We do we need Decorators?

# Decorator
def performance(func):
    def wrapper(*args, **kwargs):
        # check time before running the function
        t1 = time()
        result = func(*args)
        # check time after running the function
        t2 = time()
        print(f'Time to run the function = {format(t2 - t1, "0.3f") } ms')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000):
        print('Running function..please wait..')


long_time()