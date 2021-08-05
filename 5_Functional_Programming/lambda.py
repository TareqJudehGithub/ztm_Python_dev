from functools import reduce
"""
Lambda expression
    One time anonymous function that we don't need more than once.
    Lambda expression are useful when:
        - functions you only use once.
        - they are anonymous. We don't need to store them in variables and in memory.
    - lambda param: fractions(param)
"""

my_list = [10, 15, 20, 25, 30, 35]

# lambda: map
my_list_x2 = list(map(lambda item: item * 2, my_list))
print(my_list_x2)

# lambda: filter
my_list_even = list(filter(lambda item: item % 2 == 0, my_list))
print(my_list_even)

# lambda: reduce
my_list_total = reduce(lambda acc, item: (item + acc), my_list)
print(my_list_total)
