"""
Conditional Logic
- Python uses : colon at the end of the conditional head
- Python does not use {curly brackets for the conditional body}
- and: both expressions must be true to run
-  or: either one of the expressions needs to be true
- If we included a string/int/float value right after the if keyword, Python
  interpreter will check if that value exists or not.
    Example:
        username = 'john45'

        if username:
            print(f"Hello, {username}")
        else:
            print("No username is available.")

- Ternary Operator (Conditional Expressions)
    output (if expression is true) else (if expression if false)
    example:
    has_ticket = True
    print('You can enter the theatre') if has_ticket else print('You need a ticket.')

- Short Circuiting
  Short Circuiting happen when the interpreter ignore the rest of the source code in case
  the first session returned True, followed by an or logical operator. Also Short Circuiting
  takes place if the interpreter read a False value. It will then ignore the rest of the code.

- Logical Operators in Python:
    and
    or
    not
- Comparison Operators:
    = > < <= >= !=
"""

is_old = False
is_licenced = True


if is_old and is_licenced:
    print('You are old enough! you can drive now!')
else:
    print('You are not old enough to drive.')


print('\nPrint this no matter what the condition in the above if statement is.\n')

# Ternary Operator (Conditional Expressions)
print('Conditional Expressions (Ternary Expressions)')

is_rain = True
print('Take an umbrella') if is_rain else print('Enjoy your day!\n')

# Short Circuiting
print('Short Circuiting')
is_friend = True
is_user = True
if is_friend or is_user:
    print('best friends forever\n')


# Operators : (Logical and Comparison)
print('Operators : (Logical and Comparison)')
print('a' > 'b')
print('5' == 5)
print('5' is 5)
print(5 is 5)
print(not 1 == '1')

print('\n')
#Quiz:
is_magician = True
is_expert = True

# If both magician and expert are true: print('Master magician')
# If magician is true: print('Apprentice Magician')
# if magician is false: print('You are not a magician')

if is_magician and is_expert:
    print('Master magician')
elif is_magician and not is_expert:
    print('Apprentice Magician')
else:
    print('You are not a magician')












