"""
Dictionaries (dict)
 - dict is an unordered key-value pair data structure type.
 - dict can contain any type of data
 - dict keys MUST be immutable. i.e a list data type cannot be a dict key.
 - a key in a dict has to be unique. The last repeatable key will override
   the ones before it.

"""
print('\n', 'Dictionaries (dict)')
new_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
# access 'a'
print(new_dict['a'])

# access an item that
print(new_dict.get('d', 'Key not found'))

my_list = [
    {
        'name': 'John Smith',
        'email': 'tareq@gmail.com',
        'age': 45,
        'address': 'Amman, Jordan',
        'tel': ['0796969904', '065852094']
    }
]
# access the 2nd telephone #
print('')
print('dict methods')
print(my_list[0]['tel'][1])

shopping_dict = {
    'cart': ['Bananas', 'Bread', 'Milk', 'Eggs', 'Orange Juice'],
    'is_logged_in': True,
    'username': 'goldie45'
}
print('.get()')
# .get() prevents code error in case key is not found, and can provide a default value.
print(shopping_dict.get('age', 'value not found.'))
print(shopping_dict)

# We could also create a new dict using built-in function dict()
user2 = dict(username='john32', age=32, tel=['079654', '0658789'])
print(user2)
print('')


# looking for keys in dicts
print('Searching keys and values in dicts')
print('')

# .key()
print('username' in shopping_dict.keys())
# also we could provide a key as an argument:
print(shopping_dict['is_logged_in'])
print('')

# .values()
print('goldie45' in shopping_dict.values())
print('')

# .items()  returns both keys and items
print(shopping_dict.items())
print('')

# .copy()   creates a new separate copy of the original dict
dict_copy = shopping_dict.copy()
print('')
# .clear()  clear the dict contents
shopping_dict.clear()
print(shopping_dict)    # {}
print(dict_copy)
print('')

# .pop()
dict_copy.pop('is_logged_in')
print(dict_copy)
print('')

# .popitem()    removes a random item from the dict
# dict_copy.popitem()
# print(dict_copy)

# .update()     updates a value, and adds a key-value pair item if they don't
# already exist.
dict_copy.update({'username': 'goldie46'})      # updates an existing key-value pair
dict_copy.update({'tel': ['079654', '069858']}) # adds a new key-value pair

# We could also provide a key and a value as arguments to update/add new entries:
dict_copy['cart'][0] = 'Cereal'     # 'Banana' => 'Cereal'
dict_copy['password'] = '*******'   # add a new key-value pair at the end of the dict.
print(dict_copy)

print('\n')









