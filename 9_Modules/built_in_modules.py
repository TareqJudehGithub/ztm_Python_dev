
"""
Built-in Python modules
    - Built-in modules are modules that are already included in Python.
    - In order to access a Built-in module, we need to import it.

"""
import random
import sys

# random built-in package
# return a random value between 0 and 1
random_num = random.random()

# returns a random integer between two specified integer values
random_int = random.randint(1, 10)
random_fruit = random.choice(['Apple', 'Orange', 'Lemon', 'watermelon'])

ordered_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# shuffles list sequence
random.shuffle(ordered_nums)


# sys built-in package
"""
sys.argv
    - Gives parameters to modules (files)

"""


if __name__ == '__main__':
    # dir() lists all methods available for a package.
    # print(dir(random))
    print('random built-in')
    print(random_num)
    print(random_int)
    print(random_fruit)
    print(ordered_nums)

    print('sys built-in')