from datetime import datetime as date

# Exercise #1: Guess user's age
print('Exercise #1: Guess user\'s age')
# extract current year
date_now = date.now()
year = date_now.strftime('%G')

# calculate age:
birth_year = int(input('What year were you born? '))

# if we dont wrap input() with int() we will be getting a TypeError
print(type(birth_year))
print(f'Your age is {2021 - birth_year}')

print('\n\n')

# Exercise #2: Password Checker
print('Exercise #2: Password Checker')

# ask for username
username = input('Type in your username: ')

# ask for password
password = input('Type in a password: ')

# hash the password
hashed_password = '*' * len(password)

# show the user how many characters his/her password is.
print(f"{username}, your password {hashed_password} is {len(password)} letters long.")

print('\n\n')
print('Exercise: Lists')
#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])
# >>> b
print(new_list[-2])
# >>> b
print(new_list[1:3])
# >>> [b, c]
new_list[0] = 'z'
print(new_list)
# >>> ['z', 'b', 'c']

my_list = [1, 2, 3]

my_list[0] = 'z'
print(my_list)
# >>> ['z', 2, 3]
bonus = my_list + [5]
print(bonus)
print(type(bonus))
# >>> ['z', 2, 3]

print('\n')


# You are working for the school Principal. We have a database of school students:
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list.
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

#using what you learned about sets, create a piece of code that the school principal
# can use to immediately find out who missed class so they can call the parents.
# (Imagine if the list had 1000s of students. The principal can use the lists generated
# by the teachers + the school database to use python and make his/her job easier):
# Find the students that miss class!

# 1. No need to convert attendance_list to a set, but doing so won't harm either
attendance_set = set(attendance_list)

# 2. using difference() set method to find out who's missing from attendance_list:
absent_students = school.difference(attendance_list)

# 3. iterate over absent_students for a cleaner result (return it as a string)
for student in absent_students:
    print(f'The absent student(s) is/are:\n{student}')

print('\n')
# dict quick quiz
a = {'a': 1, 'b': 2, 'c': [1, 2, 3]}
print(a['c'][1])

print('\n')
# Sets practice
friends = {'Jack', 'Ali', 'Salem', 'Bernard', 'Sarah'}
my_friends_list = {'Jack', 'Ali'}

print(friends)
not_in_my_list = friends.difference(my_friends_list)
print(not_in_my_list)
common_friends = friends.intersection(my_friends_list)
print(common_friends)


my_friends_list.add('Waleed')
print(my_friends_list)

print('\n')
