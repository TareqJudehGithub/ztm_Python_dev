"""
Variables
 - Variables are a way for us to store information.
 - Python is dynamic programming language.
 - We assign (bind) values to variables. Example: number = 10
 - Variables values are stored in memory in a form of binary.
 - Variables in Python are snake_case.  example: first_name
 - Variables must start with lowercase or underscore (_)
 - Variables cannot start with a number.    wrong: 3rd_player
 - Variables do not accept spaces.          wrong: first name
 - Variables cannot override keyword reserved to Python. Examples: print, input, int.
 - Variables should be descriptive.
 - Variables can be re-assigned. example: number = 10   addition = 10 + number
 - Constants should not be changed, and should be declared in uppercase. Example: PI = 3.14
 - danders variable __ are Python reserved, and should be left alone.
 - A statement is an entire line of code, that perform some sort of action. example: score = 10 + 15
 - An expression is a piece of code that produces a value. The part that follows the assignment
   operator. - 10 + 15
 - Augmented assignment operator. (operator)=   example  score += 10
"""
first_name = 'john'

# assign variables multiple times
a, b, c = 1, 2, 3

x, y = 5, 10
print(x, y)

y, x = x, y
print(x, y)

# - Expression vs Statements

score = 10

#            This part is the expression
user_score = 20 + score

# Augmented assignment operator

counter = 0
counter += 5    # >>> 0 + 5 = 5
counter -= 2    # >>> 5 - 2 = 3
counter *= 3    # >>> 3 * 3 = 9
counter /= 3    # >>> 9/3 =   3
print(int(counter))

