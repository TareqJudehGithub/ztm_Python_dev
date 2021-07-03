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


def count_substring(string, sub_string):
    """This function counts how many times a sub-string appears in a string"""
    counter = 0
    # iterate through string variable:
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string):
            counter += 1

    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    print('')
    count = count_substring(string, sub_string)
    print(count)