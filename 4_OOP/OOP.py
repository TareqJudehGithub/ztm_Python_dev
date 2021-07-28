# OOP

"""
 - OOP is paradigm, and a way to think and structure our code.
 - OOP is a way to structure out code, as it gets bigger, we are the able
    to keep it organized.
 -OOP allows us to create objects that have their own methods and attributes.
 - Python supports OOP
 - OOP applied the DRY principle
 - class
    - class uses CamelCase
    - class naming should always be singular and not plural.
    - class is like a blueprint, where I can create other objects (instances).
    - class can be instantiated to create other instances. When somebody
      says: "Hey I just instantiated a class". It means he or she has created
      a new object of a class.
    - class is stored in memory.
    - objects instantiated from a class, searches memory for that class and run
      it.
    - __init__(self):
        - __init__ is a dunder method.
        - self refers to the class variable name (PlayerCharacter in example #2).
        - params following self in the __init__ dunder method are called attributes.
            - Attributes are pieces od data that are dynamic. When we instantiate an
            object, these attributes are going to be unique for that object (like
            name and age in our example).
            - Attribute are dynamic. We use self keyword to manipulate them.
            - In order to access attributes, we need to use self keyword.
            - class object attribute. Unlike attributes, class object attributes are
              static. We can't modify it, it's just all objects instantiated have
              access to it.
            - We don't have to use self to access class object attribute, we could
              use the class it self.

"""

# Creating the class

# Example #1
class BigObject:
    print('I\'m a class!')


print(type(BigObject))

# Instantiating the class (BigObject) creating a new object (obj1):
obj1 = BigObject()

print('\n')
# Example #2
# We work for a gaming company. We need to create a class for players characters.

class PlayerCharacter:
    # class Object Atrribute
    membership = True
    # constructor method
    def __init__(self, name, gender):
        self.char = name
        self.gender = gender
        if self.membership:
        # or if PlayerCharacter.membership:
            print(self.run())

    def run(self):
        return f'Hi, I\'m {self.char}! I\'s a {self.gender}.'


# Instantiate class PlayerCharacter:
player1 = PlayerCharacter('Ali', 'Male')
print('')

# We could also call a method inside a class:
player2 = PlayerCharacter('Sarah', 'Female')
player2.run()
print('')

# We could also add attributes outside the class
player2.height = 180
print(player2.height)

print('')
player3 = PlayerCharacter('Noor', 'Female')

print('')
print(player3.membership)

print('\n')









