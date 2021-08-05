"""
List Comprehensions
 - my_list = [char for char in iterable]
"""

hello = [i for i in 'hello']
print(hello)

print('')

zero_to_100 = [i * 2 for i in range(101)]
print(zero_to_100)

print('')

# iterate from zero to 100, squaring each number, and returning only the even ones.

result = [i**2 if i % 2 == 0 else 'Odd' for i in range(101)]
print(result)
