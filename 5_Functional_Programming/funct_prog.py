"""
Functional Programming
 What is functional programming?
  - It is all about separating of concerns, like OOP does. Each part is concerned
    with one thing that it is good at.
  - Packaging our code into separate chunks, so that everything is well organized
    in each part of our code, and each part is organized in way that make sense,
    based on functionality.
  - Functional Programming separate data and functions, instead of combining methods
    and attributes; because they are two separate things.
  - In most functional programming we don't have the idea of classes and objects.
  - Functional programming operate on well defined data structure like lists and dicts.
  - Functional Programming aims to:
    - Clear and understandable code
    - Easy to Extend (scalable)
    - Easy to maintain
    - Memory efficient code
    - DRY principle

 What is Pure Functions?
    - A pure function is a function that takes an input, and always return the same output.
    - A pure function should not produce any side effects.
    -
"""

""" multiply_by2 func is pure func that does not produce any side effects.
In case we defined new_list outside the func, then it will produce side effects, because
it interacts with outside the function scope.
"""


def multiply_by2(li):
    new_list = list()
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))


# map, filter, and reduce

print('')
print('.map()')
print('')

"""
.map()
 - map simplifies the code and iterates over iterables.
 - .map(func_name, iterable)
 - .map() maps over each item in an iterable.
 - .map() does NOT modify the original list, but it creates a new one without
   side effects (not affecting outside the scope).
 - map() is useful for iterating over all the iterable items and modify them 
   based on the function provided in the first argument.
 - .map() returns the same number of items in the input (iterable in the 2nd argument).
"""

scores = [90, 80, 70, 80, 90]


def result(my_list):
    return my_list * 2


# print(result(scores))

#
result_map = list(map(result, scores))
print(result_map)

print('\n')
print('filter()')
"""
.filter()
 - list(filter(func_name, iterable))
 - .filter() filters an iterable based on the function provided as the first argument
 - Like the case in .map(), .filter() creates a new iterable and modify it, without touching
   the original iterable in the 2nd argument.

"""
num_list = [26, 13, 45, 26, 77, 85, 0]


def is_odd(iterable):
    return iterable % 2 != 0


filter_result = list(filter(is_odd, num_list))
print(filter_result)


print('\n')
print('zip()')

"""
zip()
 - zip() zips more than one iterable binding them together as a tuple.
"""
names = ['john', 'sarah', 'ali']
ages = 45, 32, 29
countries = ['USA', 'UK', 'JO']

user_details = list()

for i in zip(names, ages, countries):
    user_details.append('Name: {}, Age: {}, Country: {}'.format(*i))

print(user_details)


print('\n')
'''
Quiz: Enumerate & zip()

Use enumerate to modify the cast list so that each element contains 
the name followed by the character's corresponding height.
'''

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for index, item in enumerate(cast):
    cast[index] = f' Name: {cast[index]}, Height: {str(heights[index])}'

for item in cast:
    print(item)

print('')
# Now try solving that problem using zip()
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]

for index, height in zip(range(len(cast)), heights):
    cast[index] = 'Name: {}, Height: {}'.format(cast[index], str(height))

for item in cast:
    print(item)

print('\n')

"""
Reduce()
 - We need to import reduce from module functools in order to be abel to use it.
    from functools import reduce
 - reduce(func_name, sequence, init (optional))

"""
from functools import reduce

num_list2 = [44, 35, 87, 12, 95, 64, 78]
list_3 = [5, 5, 5]
even_list = list()

def even_sum(acc, x):
    return acc + x

    # if x % 2 == 0:
    #     even_list.append(x)
    # print(even_list)
    # return sum(even_list)


sum_of_even = reduce(even_sum, list_3)

print(sum_of_even)




