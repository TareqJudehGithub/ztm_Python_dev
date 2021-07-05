"""
Strings str()
 - String is a peace of text. Example: "Hello, world!"
 - Strings are immutable ordered sequence of characters.
 - String Concatenation.
    - Adding string together
    - Only string values can be concat together
    - We can convert other data types using Type Conversion.
 - Escape Sequences
    - \'s enables us to add quotations inside strings.
        Example: 'Name\'s John '
    - \t add a tab spacing.  Example: "Column1\t Column2\t Column3\t"
    - \n Adds a new line.   "Thank you\n Have a lovely day!"

 - formatted Strings
    greet = 'Hi {0}! You are {1} old.'.format(account_name, age)
     - We could also ignore indexing and the code will would still work.
    greet_2 = f'Hi {account_name}! Your are {age} old.'
     - f'string' is more clean and is the way to go I'd say.

 - String Indexing (Slicing)
    string[start, stop, optional: step over]

 - Strings are immutable. Strings contents cannot be edited or changed.
    name = 'john'
    name[0] = 'J'  >>> TypeError
    The only way to change a string value, is to reassign a new value (name = 'John')

"""
print(type("Hello"))

username = "tj.coder"
password = "Pa$$@"
long_string = """
WOW
o o
/\
"""

first_name = 'john'
last_name = 'smith'

# string concatenation:

print('string concatenation')
full_name = first_name + "" + last_name
full_name_f = f"{first_name} {last_name}"
print(full_name_f, end='\n')

# Type Conversion
edit_username = username + str(75)
print(edit_username)

# Escape Sequences
print("Escape Sequences")
print("It\"s going to rain today!")
print("Column1\tColumn2\tColumn3\t")
print("Thank you\nHave a lovely day!")

# Formatted Strings
print('Formatted Strings')
account_name = 'john'
age = 45
greet = 'Hi {}! You are {} old.'.format(account_name, age)
print(greet, end='\n')

# Or we could use f''
greet_2 = f'Hi {account_name}! Your are {age} old.'
print(greet_2, end='\n')


print("String Indexing (Slicing)")
# Strings are ordered sequence of character
student_name = 'sarah cole'
# Index:        0123456789


print(student_name[0:5], end='\n')
# >>> Sarah

print(student_name[::1])     # start at 0: stop after last index

print(student_name[-1])      # return the last index from the right
print(student_name[-2])      # return the 2nd index from the right
print(student_name[::-1])    # reverse the string order

print('\n')
print('String Methods', '\n')

print('title()')
print(student_name.title(), '\n')     # Capitalize the first letter of every string

print('find()')
print(student_name.find('c'), '\n')   # returns the first occurrence it finds and stopped the search.

print('replace()')
print(student_name.replace('cole', 'coleman').title())

print('')
print('.isalnum()')
# This method checks if all string character are alphanumeric (a-zA-z0-9)
my_username = 'GoldiE75'
print(my_username.isalnum())

print('')
print('.isalpha()')
# .isalpha() checks if all string characters are alphabetical (a-zA-z)
print(my_username.isalpha())

print('')
print('.isdigit()')
# This method checks if all string character are digits (0-9)
print('111212312523562340907'.isdigit())

print('')
print('.islower()')
# This method checks if all string character are lowercase (a-z)
print('gold smith'.islower())

print('')
print('.isupper()')
# This method checks if all string character are uppercase (A-Z)
print('GOLD SMITH'.isupper())