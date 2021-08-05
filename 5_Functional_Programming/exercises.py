'''
Use enumerate to modify the cast list so that each element contains
the name followed by the character's corresponding height.
'''

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]


def name_height(name, height):
    # write your for loop here
    for index, item in enumerate(name):
        name[index] = f'Name: {name[index]}, Height: {height[index]}'

    return cast


print(name_height(cast, heights))
print('\n')

# return full name as a string
full_name = ['Noor AbuZaid', 'Tareq Judeh', 'Dina Judeh', 'Leen Judeh']

for i in full_name:
    name = "".join(i)
    print(name)

print('\n')

# sort first name and last name in dict, where dict keys are 'first name' and
# 'last name'


full_name = ['Noor AbuZaid', 'Tareq Judeh', 'Dina Judeh', 'Leen Judeh']



firstname_lastname = dict()
def first_last(names):

    for item in names:
        first_name = item.split(" ")[0]
        last_name = item.split(" ")[1]
        firstname_lastname['name'] = "".join(first_name + ' ' + last_name)


    # for k, v in firstname_lastname.items():
    #     print(f'Firstname: {k}, Lastname: {v}')


first_last(names=full_name)
print(firstname_lastname)

print('\n')
full_name = ['Noor AbuZaid', 'Tareq Judeh', 'Dina Judeh', 'Leen Judeh']
name = str()
for i in full_name:
    name += ''.join(i) + ' '
print(name)

print('\n')
print('===============')
# Exercises: map, filter, and reduce
print('Exercises: map, filter, and reduce')


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize(string):
    return string.capitalize()


pets_capitalize = list(map(capitalize, my_pets))
print(pets_capitalize)


print('\n')
#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]


def zip_lists(list_a, list_b):

    sorted_dict = dict()
    list_b.sort()

    new_list = zip(list_a, list_b)
    for i in new_list:
        # Add strings as keys, and numbers as value in a new dict
        sorted_dict[i[0]] = i[1]
    return sorted_dict


print(zip_lists(my_strings, my_numbers))

print('\n')
#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def score_over_50(iter):
    return iter >= 50


passing_scores = list(filter(score_over_50, scores))
print(passing_scores)

print('\n')
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
from functools import reduce
def accumulator(acc, iter):
    return acc + iter


total = reduce(accumulator, (my_numbers + scores))
print(total)


# ================
print('\n')

some_list = ['a', 1, 'b', 2, 5, 'g']

def return_str(item):
    if type(item) is str:
        return item


str_item = list(filter(return_str, some_list))
print(str_item)


# ================
print('\n')
# lambda exercises

random_numbers = [5, 4, 9]

# using lambda expression, return all items in random_numbers squared.
squared_nums = list(map(lambda num: num ** 2, random_numbers))
print(squared_nums)

print('')
# sort items inside random_tuples based on 2nd value.
random_tuples = [(0, 2), (4, 3), (9, 9), (10, -1)]
random_tuples.sort(key=lambda item: item[1])

print(random_tuples)

print('\n')

list_of_strings = ['a', 'b', 'a', 'c', 'd', 'm', 'n', 'n']

# return duplicates in list_of_strings

duplicates = []

for i in list_of_strings:
    if list_of_strings.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)

print(duplicates)
print('\n')

# using comprehensions, solve the above problem
duplicates_v2 = set([i for i in list_of_strings if list_of_strings.count(i) > 1])
result = list(duplicates_v2)
print(result)


