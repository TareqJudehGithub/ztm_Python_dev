"""
 For loop
 - For loop iterates over each item inside an object (str and data structure) until the
   last object is iterated over.
 - Iterable: an object or a collection of items that can iterates over.
 - Iterable can be a list, dict, or even a string.
 - iterate to go through an iterable (collection) items one by one.
 - range()  range iterates over integers objects or integers variables.
    range(start, stop, stepover)

"""
greet = 'hello world!'
for letter in greet:
    print(letter)

print('')

# enumerate:
cart_list = ['apples', 'milk', 'bread']
for index, index in enumerate(cart_list):
    print(index)

print('')
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
# loop over keys only:
for index in user.keys():
# OR for item in user:
    print(index)
print('')

# loop over key and values (Dict unpacking):
for k, v in user.items():
    print(f'{k}: {v}')
print('')

# loop over values only:
for key in user.keys():
    print(key)

print('\n')
# range() function
print('range()')

# iterate from 0 to 10, stepping over even numbers.
for _ in range(0, 10, 2):
    print(_)
print('')

# iterating backwords from 10 to 0
for _ in range(10, 0, -1):
    print(_)
print('')

# create a list with 10 integers as the list elements/items:
new_list = list(range(0, 10 + 1))
print(new_list)
print('')

print('\n')
print('enumerate()')
# enumerate() function returns an index counter, and the item of that index.

for index, char in enumerate('Hello world!'):
    print(index, char)

print('')
for index, item in enumerate(new_list):
    print(index, item)
print('')


print('')
# Quiz: print index of char 50
print('Quiz: print index of char 50')
for index, char in enumerate(list(range(100))):
    if index == 50 and char == 50:
        print(f'The index of 50 is {index}')

