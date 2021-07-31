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
    # class Object Attribute
    membership = True

    # constructor method
    def __init__(self, name, gender):
        self.char = name
        self.gender = gender

        if self.membership:     # or PlayerCharacter.membership:
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
player3 = PlayerCharacter('Noor', 'Female', )

print('')
print(player3.membership)
print('\n')


print('Character class')
class Character:

    # class object attribute
    membership = True

    def __init__(self, name, age):
        self.age = age
        if self.age > 18:
            self.name = name

        # methods
    def shout(self):
        print(f'My name is {self.name}')

    def test_self(self):
        return self

char_1 = Character('Noor', 19)
char_2 = Character('Dina', 15)

print(char_1.name)

# age is under 18, so attribute 'name' is not accessible
# print(char_2.name)
print('')
print('testing self')
print(char_1.test_self())
print('')

char_3 = {'name': 'John', 'age': 25}
print(char_3['name'])
print(char_3['age'])