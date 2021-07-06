"""
Tuples
- Tuples are immutable ordered data structured type.
- Tuples are less flexible than lists, but performs faster.
- Tuples cannot be changed, unlike lists. Tuples are immutable.
- Tuples are valid keys in dictionaries.

"""

my_tuple = 1, 2, 3, 4

# access tuple index:
print(my_tuple[1])
print('')

# swap variables values using tuples
print('swap variables values using tuples')
a = 1
b = 2
print(f'a={a}, b={b}')
# Swap a and b, so a's value become b's, and b's value becomes a's.
a, b = b, a

print(f'a={a}, b={b}')
print('')

# old school solution:
print('old school solution:')
value_a = 1
value_b = 2
print(f'value_a={value_a}, value_b={value_b}')

value_c = value_a
value_a = value_b
value_b = value_c

print(f'value_a={value_a}, value_b={value_b}')

print('')
print('Tuples slicing (indexing)')

some_tuple = 1, 2, 3, 4, 5, 6, 2, 8, 10, 2
print(some_tuple[1])
print(some_tuple[1:4])
print(some_tuple[:2])
print(some_tuple[::-1])

x, y, z, *other = 1, 2, 3, 4, 5, 6
print(x, y, z)
print(other)

# tuples methods

# .index()  returns the index of a provided value as an argument
print('.index()')
print(some_tuple.index(8))

# .count() counts a certain value in a tuple
print('count()')
print(some_tuple.count(2))

