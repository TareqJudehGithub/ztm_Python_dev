"""
Useful Modules
 - Modules starting with Capital letter are classes, while the ones
   starting with lower case are functions.
"""
# collections
from collections import Counter, defaultdict, OrderedDict

# Counter()  creates a dict that keeps track of how many items occurred in an
# iterable.
li = [1, 3, 5, 1, 1, 7, 5, 5, 7, 9, 9, 2]

# Counting list items using iterable.count() function
print(len(li))

# using Counter
print(Counter(li))

# Counter() is case sensitive when it comes to characters.
greet = 'Hello, world! hi!'
print(Counter(greet))

print('\n')

# defaultdict() dict subclass that calls a factory function to supply missing
# values
new_dict = {'a': 1, 'b': 2}
example = defaultdict(lambda: 'Value does not exist', {'a': 1, 'b': 2})
print(example['n'])

# Personally, I prefer dict.get() method
print(new_dict.get('c', 3))

print('\n')
# OrderedDict retain the order of a dict
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d1)
# >>> True

# Now try the same code without OrdereDdict() sub class

d1['a'] = 1
d1['b'] = 2


d2['a'] = 1
d2['b'] = 2

print(d2 == d1)
# >>> True

# But what about if we changed the order?
d1['a'] = 1
d1['b'] = 2

d2['b'] = 2
d2['a'] = 1

print(d2 == d1)
# >>> True

# Now, try the last comparison using OrderedDict()

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d1)
# >>> False. OrderedDict() remembers the order entries were added

# Dicts are now ordered, get used to it after 3.7
