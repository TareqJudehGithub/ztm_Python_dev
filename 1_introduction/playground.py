print('Hello, World!')

# string = "abracadabra"
# string = string[:5] + "---" + string[6:]
# # print(string)
# print(string[:5])
# print(string[6:])
# print(string)


# def mutate_string(string, position, character):
#     # solution #1: using string slice and joining
#     # string = string[:position] + character + string[position + 1:]
#     # return string
#
#     # solution #2: converting string into a list, editing the list, and joining it back to string:
#     string_list = list(string)
#     string_list[position] = character
#     new_string = "".join(string_list)
#     return new_string
#
#
# if __name__ == '__main__':
#     s = input()                 # original string
#     i, c = input().split()      # index, new_char
#
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

new_list = [15, 12, 3, 4]

# delete first item from a list
del new_list[0]
print(new_list)

if 5 not in new_list:
    print("a is not in b")
else:
    print('a is in b')

new_list.sort()
print(new_list)

# remove an item from a list by its string/number
if 12 in new_list:
    new_list.remove(12)

print(new_list)
print(new_list.count(3))

# Find a string challenge
# Count how many a sub string appears in a string
print('\n')

# def count_substring(string, sub_string):
#     """This function counts how many times a sub-string appears in a string"""
#     counter = 0
#     # iterate through string variable:
#     for i in range(0, len(string)):
#         if string[i:].startswith(sub_string):
#             counter += 1
#     return counter
#
#
# if __name__ == '__main__':
#     string = input('Enter a string: ').strip()
#     sub_string = input('Enter a substring: ').strip()
#     print('')
#     count = count_substring(string, sub_string)
#     print(count)
#


# String Validators

# print('String Validators')
# my_name = 'qA2'
#
#
# def string_validator(string):
#     # any() function only works on iterable; so we will use List Comprehension
#     # to iterate through string elements
#     print(any(char.isalnum() for char in string))
#     print(any(char.isalpha() for char in string))
#     print(any(char.isdigit() for char in string))
#     print(any(char.islower() for char in string))
#     print(any(char.isupper() for char in string))
#
#
# string_validator(my_name)
#
# print('')
# # Check this dict, if it's keys & values characters contain any digits or alphanumeric
# # values.
# mydict = {'123': "Apple", 'ds': "Orange"}
#
# has_digit = [k.isdigit() and v.isalpha() for (k, v) in mydict.items()]
# print(has_digit)

print('\n')
# Introduction to Sets problem

# def average(array):
#     # your code goes here
#     new_set = set(array)
#     return round(sum(new_set) / len(new_set), 3)
#
# if __name__ == '__main__':
#     n = int(input('Enter the total of numbers: '))
#     arr = list(map(int, input('Enter numbers here: ').split()))
#     result = average(arr)
#     print(result)

print('\n')

# Finding the percentage
print('Finding the percentage')

# 'John': [52, 56, 60]
# student_marks = dict()
# # print(len(student_marks.values()))
# marks = list()

# def avg_marks():
#
#     for k, v in student_marks.items():
#         for i in v:
#             marks.append(i)
#
#     return sum(marks) / len(marks)
#     # return sum(student_marks.values()) / len(student_marks.values())
#
#
# print(avg_marks())

if __name__ == '__main__':
    n = int(input('score total: '))
    student_marks = {}
    marks = list()
    for _ in range(n):
        name, *line = input('Scores: ').split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input('query: ')

    for k, v in student_marks.items():
        if k == query_name:
            print(format(sum(v)/len(v), '0.2f'))


    # print(sum(marks) / len(marks))