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
import typing

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

print('\n')
# Tesla exercise
print('Tesla exercise')


#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
def checkDriverAge(age=0):
    # age = int(input('Please enter you age: '))
    if int(age) < 18:
        return "Sorry, you are too young to drive this car. Powering off"
    elif int(age) > 18:
        return "Powering On. Enjoy the ride!"
    elif int(age) == 18:
        return "Congratulations on your first year of driving. Enjoy the ride!"

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
print(checkDriverAge(46))
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.


print('\n')
# Create a function called highest_even that will take a list of numbers as a parameter.
# highest_even should return the highest even number in the list.
def highest_even(my_list: typing.List) -> int:
    # solution the pythonic way:
    even = list()
    for i in my_list:
        if i % 2 == 0:
            even.append(i)
    return max(even)

    # solution old school  way:
    # highest_num = 0
    # for i in my_list:
    #     if i % 2 == 0 and i > highest_num:
    #         highest_num = i
    # return highest_num


print(highest_even([11, 10, 4, 8, 9, 15, 16, 17, 20, 26]))

print('\n')
