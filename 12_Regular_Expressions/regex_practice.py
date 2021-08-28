import re

text = 'Python has a built-in package called re, ' \
       'which can be used to work with Regular Expressions'

# search a string located at the start and return it
print(re.search(r'^Python', text).group())
""" 
.group() returns the pattern string we are searching for

"""
# search more than one string but in sequence
print(re.search('has.*package', text).group())

# .findall() return matching result in a list
print(re.findall('has a built-in package', text))

# end with
print(re.search(r'Expressions$', text).group())

# .sub replaces one or many matches with a string
print(re.sub('a', 'A', text))

# [] for matching specific characters
print(re.findall(r'[on]', text))

# exclude char we use [^char to be excluded]

greet = 'Hello Bello'
print(re.search(r'[^H]ello', greet).group())

greet_2 = 'Hello'
add_str = []
for char in greet_2:
    print(re.search(r'[^H]', char))

print('')
# pattern{2, 4} # find a repeated pattern 4 times, but not more than 2.
ll = re.search(r'l{2}', text).group()
print(ll)

print(re.search(r'l{2}', greet_2).group())

print('')
# solution using old school for loop:
l_char = str()
for char in greet_2:
    if char == 'l':
        l_char += char

print(l_char)