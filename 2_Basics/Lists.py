"""
Lists
 - List is sequenced order of values of any type.
 - List is a part of the *Data Structure.
 - List are mutable.
 - Copy VS Modify:
     - If we assigned a new variable list to our original list, then any
       modification to the new list, will also affect the original list; because
       assigning a variable to an existing list, will cause both variables to share
       the same value stored in memory.
            Example: new_cart = amazon_cart

     - If we needed to create a COPY of an existing list, and without altering that
       list values, use colon.
            Example: new_cart = amazon_cart[:]

 - Matrix is what we call a list that has other lists inside it as elements.
 - Matrix is a two-dimensional lists.
 - List methods modify an existing list, but does not returns it not it creates a new copy.
 - A method is a function of an object.
 - printing a list method returns None.  Example: print(basket.append(10))


 * Data structure is a way to organize data and store it into a contained fashion.


"""
# Lists format
my_list = list([1, 2, 3, 4, 5])
or_list = [1, 2, 3, 4, 5]
a_list = ['a', 'b', True, 'E', 1.5, 100]


amazon_cart = [
    'notebooks',
    'sunglasses'
]

# Accessing items in a list (list elements)
print('Accessing items in a list')

# first item in a list:
print(amazon_cart[0])
# 2nd item in a list:
print(amazon_cart[1])


print('list Slicing\n')
# Remember [start, stop, step over]

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

# return the first and the 2nd item:
print(amazon_cart[0:2])

# return all items using slicing:
print(amazon_cart[::])

# step over elements bu 2
print(amazon_cart[::2])
print(amazon_cart[1::2])

# Lists are mutable, we could replace/edit elements inside a list
amazon_cart[0] = 'PC'
print(amazon_cart)

# creating a NEW copy list:
new_cart = amazon_cart[:]
new_cart[1] = 'glasses'
print(new_cart, '\n')

# Matrix
print('Matrix')
"""
Matrix is what we call a list that has other lists inside it as elements (a two-dimensional list).
"""
matrix = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    [True, False],
    ['car', 'apple', 'tomato', 'potato', 'banana']
]
# Access the 2nd item in the 2nd list and print it out. Output should return b
print(matrix[1][1])

# Access the last item in the 3rd list and print it out. Output should return False
print(matrix[2][-1])

# return the 2nd list reversed
print(matrix[1][::-1])

# sort out the last list inside matrix
matrix[3].sort()
print(matrix[3])

# return the length of matrix list
print(len(matrix), end='\n')  # >>> 4


# List methods
print('List methods')

basket = [1, 2, 3, 4, 5]
# Adding methods in lists:
# .append()     adds an item to the end of the list.
basket.append(6)
print(basket, end='\n')

# .insert(index, value)  adds a new element in a specified  position
basket.insert(2, 2.5)
print(basket, end='\n')

# .extend(iterable)     adds an iterable (like a list) to the end of ane existing list.
basket.extend([7, 8, 9])
print(basket, '\n')

# removing items from a list
print('remove items from a list')
print('')
print('.pop()')
# .pop() methods removes the last element in a list, unless we provided an index as argument.
basket.pop()    # removes last item
print(basket)
basket.pop(2)   # removes a specific item
print(basket)

print('')
print('.remove()')
# .remove() delete an item by providing its value (not index)
basket.remove(8)
print(basket)
print('')

print('del() function')
# del() removes a specific item inside a list using its index
# If no index was provided, then the whole list gets dropped/deleted.
del basket[0]
print(basket)

print('')
print('.clear()')
# .clear() clears out all of the list elements
print(f'Clearing basket returns: {basket.clear()}')
print('')

print('.index() ')
# returns a value index
# .index() format:  list.index(value, start, stop)
fruits = ['apple', 'orange', 'banana', 'strawberries', 'kiwi', 'water melon', 'cherry', 'banana']
print(fruits.index('banana'))   # >> 2
print(fruits.index('cherry', 0, len(fruits)))
print('')

print('.count()')
# .count() counts how many times a value occurred in a list
print(fruits.count('banana'))
print('')

