# # leap year exercise
# def leap_year(year):
#     if year % 400 == 0:
#         print(f'{year} is a leap year')
#     elif year % 100 == 0:
#         print(f'{year} is not a leap year')
#     elif year % 4 == 0:
#         print(f'{year} is a leap year')
#     else:
#         print(f'{year} is not a leap year')
#
#
#
# if __name__ == '__main__':
#     year = int(input('Enter a year: '))
#     leap_year(year)
#
# print('\n')
# # Exercise: Tricky counter
# # Build a simple counter, calculating sum of items in a list
# num_list = list([1, 6, 22, 17, 6])
# counter = 0
# for item in num_list:
#     counter += item
#
# print(counter)
#
# # solution using sum() functions
# counter = 0
# list_sum = sum(num_list)
# print(list_sum)
#
# print('\n')

print('\n')
# loop exercise: GUI exercise
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
# solution:
# iterate over each list, and over each item inside each list:
for l in picture:
    for index, item in enumerate(l):
        # modifying picture list, replacing 0 items with a '', and 1 items with a '*':
        if item == 0:
            l[index] = ' '
        else:
            l[index] = '*'

# convert picture list to string:
for l in picture:
    print("".join(l), end='\n')


print('\n')
# Exercise: print out duplicates in a list:
print('Duplicates')
dup_list = ['a', 'b', 'c', 'a', 'c', 'd', 'e']

# solution:

# declaring a new list to contain duplicates from dup_list:
duplicates = list()

# iterating over dup_list, and adding only 1 duplicate to duplicates list:
for i in dup_list:
    if dup_list.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

# OR
# check_dup = list()
# for i in dup_list:
#     check_dup.append(i)
#     if check_dup.count(i) > 1:
#         duplicates.append(i)

duplicates_str = "\n".join(duplicates)
print(duplicates_str, end='\n')


