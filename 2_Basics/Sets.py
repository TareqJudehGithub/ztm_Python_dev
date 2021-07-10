"""
Sets
 - Sets are data structured type
 - Sets are unordered collection of unique objects.
 - Sets only return unique objects (no duplicates).
 - Sets are useful for saving unique data, like username, emails (unique data).
"""

# instantiation a new set:
my_set = set()
# or
my_set ={1, 2, 3, 4, 5, 1, 4}
print(my_set)
print(len(my_set))

# Set methods:
print('Sets methods\n')
print('add()')
# .add()   adds a new value at the end of a set.
my_set.add(8)
print(my_set, '\n')

# Quiz: Convert the below list to a set
convert_me = [1, 2, 1, 3, 5, 5, 3, 5, 4, 4]
new_set = set(convert_me)
print(new_set)
print('')

print('copy()')
# copy()
set_copy = new_set.copy()

print('clear()')
new_set.clear()
print(new_set)
print(set_copy)


print('\n')
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}


# difference() Returns a set containing the difference between two or more sets without changing/modifying the set.
print('difference()')
print(set_A.difference(set_B), '\n')

# difference_update() Modifies the set with the items in this set that are NOT included in the other set.
print('difference_update()')
set_A.difference_update(set_B)
print(set_A, '\n')

# intersection()	    Returns a set, that is the intersection of two or more sets
print('intersection()')
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}
print(set_A.intersection(set_B))
# we could also use & to intersect between the two sets:
print(set_A & set_B, '\n')

# intersection_update() modifies a set, that is the intersection of two or more sets
print('intersection_update()')
set_A.intersection_update(set_B)
print(set_A, '\n')

print('isdisjoint()')
set_A = {1, 2, 3, 4, 5}
set_B = {6, 7, 8, 9, 10}
print(set_A.isdisjoint(set_B), '\n')
# isdisjoint()	        Returns boolean whether two sets have nothing in common (an intersection).

# issubset()	        Returns a boolean whether this set is  a subset of another set.
print('issubset()')
set_A = {4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}
print(set_A.issubset(set_B))
print('\n')

# issuperset()	        Returns a boolean if the other set is subset of the first set.
print('issuperset()')
set_A = {4, 5, 6, 7, 8, 9, 10}
set_B = {4, 5, 6, 7, 8}
print(set_A.issuperset(set_B))
print('\n')

# union()	             Return a set containing the union of sets, removing any duplicates.
print('union()')
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10}
one_set = set_A.union(set_B)
print(one_set)
# union() can be replaced with | and still unite the two sets:
print(set_A | set_B, '\n')


set_A = {4, 5, 6, 7, 8, 9, 10}
set_B = {4, 5, 6, 7, 8}

# update() overrides the first set contents with the other set.
print('update()')
set_A.update(set_B)
print(set_A, '\n')

# pop()	                Removes the first element from the set
print('pop()')
set_A = {4, 5, 6, 7, 8, 9, 10}
set_B = {4, 5, 6, 7, 8}
set_A.pop()
print(set_A, '\n')

# remove()	            Removes the specified element
print('remove()')
set_A = {4, 5, 6, 7, 8, 9, 10}
set_A.remove(9)
print(set_A, '\n')

# discard()	            Remove the specified item
print('discard(10)')
print(set_B)
set_B.discard(10)
print(set_B, '\n')






