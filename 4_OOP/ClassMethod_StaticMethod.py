"""
Class methods
    - Class methods are referred as @classmethod in Python
    - cls, which stands for the class, is the first parameter in a class method function.
    - cls parameter refers to the class it self.
    - cls is used to instantiate objects.
    - We use class methods, when we care about class attributes.

Static methods
    - static methods @staticmethod, performs like functions.
    - unlike class methods, static methods do not require cls as an argument.
    - - We use static methods, when we don't need to use class attributes.
"""

class PlayerChar:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    # class method (decorator)
    @classmethod
    def adding_things(cls, num1, num2):
        # return num1 + num2
        # using cls, we instantiated a new instance
        return cls('Teddy', num1 + num2)

    #static method
    @staticmethod
    def multiply_things(num1, num2):
        return num1 * num2


player_1 = PlayerChar('John', 25)
player_1.shout()
print('')
print('class methods')
player_3 = PlayerChar.adding_things(15, 25)
print(player_3.age)
