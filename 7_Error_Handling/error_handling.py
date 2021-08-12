"""
Error Handling
- An error that happen during code interpreting, is called an exception.
- Types of errors (exceptions) in Python:
    - SyntaxError like when we forget a semicolon, a bracket..etc
    - NameError   happens when calling a variable before defining it first.
    - IndexError  item we r trying to call is not in the dataset range.
    - ZeroDivisionError  when we try to divide by zero
    - Error handling allows our code to continue running, even there's an error.
    - Error handling syntax:
        try:
            try something

        except ErrorType as err:
            return custom_message or err

        else:
            return something

        finally:
            return this regarding what happens.

    - finally is useful, a good use of finally is to logout users or sessions.

    - raise is good to throw errors and break out.

"""

# example of syntax error
# def hello() # forgetting to type : at the end of the function head, we return a syntax err.
#     return 'hello'


def ask_age():
    while True:
        try:
            # ValueError if user typed a different data type rather than int:
            input_age = int(input('What is your age? '))
            print(100/input_age)

        except ValueError:
            print('Input must be an integer.')

        except ZeroDivisionError:
            print('Error dividing by zero')

        except KeyboardInterrupt:
            return 'User aborted. Good Bye!'

        else:
            return f'Your age is {input_age}'

        # finally prints whether an error occurred or not.
        finally:
            print('finally :o)')


# print(ask_age())

print('\n')


def addition(num1, num2):
    while True:
        try:
            return num1 + num2

        except TypeError as error:
            return f'Please enter number only.\nError: {error}'


print(addition(10, 5))