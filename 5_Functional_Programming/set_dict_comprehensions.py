"""
Set & dict comprehensions
 - Set comprehensions eliminates duplicates.
 -
"""

# Set Comprehensions

zero_to_100 = {num for num in range(101) if num % 2 == 0}
print(zero_to_100, '\n')

print('')
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
# creating a new dict
new_dic2 = {k: v ** 2 for (k, v) in simple_dict.items() if v % 2 == 0}
print(new_dic2)
print('')

# creating a new list
new_list = [v for (k,v) in simple_dict.items()]

print(new_list)
print('')

new_dict = {num: num * 2 for num in [1, 2, 3]}
print(new_dict)

list3 = [3, 4, 5, 7, 9]
# create a dict using dict comprehension where items list are keys, and items squared are
# values.





