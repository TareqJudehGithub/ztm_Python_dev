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
