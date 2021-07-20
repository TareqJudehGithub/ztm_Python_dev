"""
Walrus Operator
 - Walrus operator := assigns values to variables as part of a larger expression.

"""
a = 'hello world!'
print('')

if len(a) > 10:
    print(f'Too long {len(a)} with elements.')

# same if statement above using Walrus operator:
if (b := len(a)) > 10:
    print(f'This variable has {b} characters.')

while (c := len(a)) > 1:
    print(c)
    # remove 1 char from the end of the string
    a = a[:-1]
print('')
print(a)
