# Lists
list_a = [1, 2, 3, 4, 5]
list_b = list_a[:]  # [:] is similar to list.copy()

list_a.insert(0, 0)

list_c = list_a.copy()
list_c.extend([6, 7, 8])
list_c.remove(8)
list_c.pop()
list_c += [7, '8']
list_c.append(True)

print(f'List A: {list_a}')
print(f'List B: {list_b}')
print(f'List C: {list_c}')
print('')

print(list_c[-1])
print(list_c[::-1])
print('\n')

matrix = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    [True, False],
    ['car', 'apple', 'tomato', 'potato', 'banana']
]

# sort out the last list in matrix
matrix[3].sort()
for l in matrix:
    print(l)

print('')
# return the length of matrix 2nd list
print(len(matrix[1]))


print('')
# add value of 1 to each item in the first list inside matrix

# test examples using enumerate and range() functions
test_list = [1, 2, 3]
for i, el in enumerate(test_list):
    test_list[i] = el + 1
print(test_list)

print()
for i in range(len(test_list)):
    test_list[i] += 1
print(test_list)

print('\n')
for index, item in enumerate(matrix[0]):
    matrix[0][index] = item + 1
print(matrix[0])
# OR
for item in range(len(matrix[0])):
    matrix[0][item] += 100
print(matrix[0])

# combine matrix1 and matrix 2 where matrix 1 items are the values of matrix 2
matrix_tup = list(zip(matrix[1], matrix[0]))
print(matrix_tup)

# Now unpack matrix_tup into two separate lists
item_name, item_quantity = zip(*matrix_tup)
print(item_name, item_quantity)
print('\n')
# Quiz: Zip Coordinates
print('Quiz: Zip Coordinates')
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = list()
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append('Label: {}, coords: {}, {}, {}'.format(*point))

print('')
for i in points:
    print(i)

print('\n')
# dicts
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast_details = dict()
for i in zip(cast_names, cast_heights):
    cast_details[i[0]] = i[1]

print([f'{k}: {v}' for (k, v) in cast_details.items() if v > 70])

print('\n')
fruits = [
    'apple', 'orange', 'banana', 'strawberries', 'kiwi', 'water melon', 'cherry', 'banana', 'peach'
]
print(fruits.index('kiwi', 0, 5)) # (value, start, stop)

print('\n')
print('Sets')
# Set
# Quiz: Convert the below list to a set
convert_me = [1, 2, 1, 3, 5, 5, 3, 5, 4, 4]
convert_to_set = set(convert_me)
print(convert_to_set)

set_a = set(fruits)
set_b = {'peach', 'blueberries', 'lemon'}

print(set_a)
print(set_b)
print('')


# print(set_a.difference_update(set_b))
# set_a.intersection_update(set_b)
set_a.update(set_b)
print(set_a)
set_a_sorted = sorted(set_a)
print(set_a_sorted)

print('\n')
# dicts
my_list = [
    {
        'name': 'John Smith',
        'email': 'tareq@gmail.com',
        'age': 45,
        'address': 'Amman, Jordan',
        'tel': ['0796969904', '065852094']
    }
]

# access the 2nd telephone number
print(my_list[0]['tel'][1])

# update the first tell no. to become '+962796969904'
my_list[0]['tel'][0] = '+962796969904'
print(my_list[0]['tel'][0])
# OR we could use .update()
my_list[0].update({'tel': ['+962796969904', '+96265854094']})
print(my_list[0]['tel'])

