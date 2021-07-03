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
