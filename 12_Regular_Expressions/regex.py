"""
Regular Expressions REGEX
    - REGEX built-in module in Python is called re

    re.compile() for searching/finding strings
     - Assign it to a variable:
            pattern = re.compile('string_to_find')

            pattern.search('string_to_find')
            pattern.findall('string_to_find')
"""
import re

pattern = re.compile('this')

string_1 = 'search inside this text please this!'

search_for_search = re.search('search', string=string_1)
print(search_for_search)
# >>> <re.Match object; span=(0, 6), match='search'>
# span=(0, 6) starts in index 0 and ended in index 6

print(search_for_search.span())    # returns start/end index in a tuple for the 1st find
print(search_for_search.end())     # returns end index as an int
print(search_for_search.group())   # useful for multiple searches
print('')


print('using .compile()')
# using .compile()
search_for_this = pattern.search(string_1)
print(search_for_this)
print(search_for_this.span())

# .findall()
print(pattern.findall(string_1))

# .fullmatch()
# here, the pattern should exactly match the full string.

# .match() # matches the string
print(pattern.match(string_1))


