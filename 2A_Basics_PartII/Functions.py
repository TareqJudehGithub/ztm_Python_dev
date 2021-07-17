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

