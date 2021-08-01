"""
Inheritance
 - Inheritance allows new object to take on the properties of existing objects.
 - classes inheriting from a class, is called sub-classes or derived classes.
 - isinstance is a built-in  function in Python, that returns a bool value
   whether an instance is part of a class or not.
 - issubclass() checks if class is a sub class of another list.
"""


class User:

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Wizard Attack Power: {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'Arrows: {self.arrows}')


# users:
wizard_1 = Wizard('Merlin', 15)
archer_1 = Archer('Legolas', 100)

wizard_1.attack()
archer_1.attack()

wizard_1.sign_in()

print('')
print('isinstance()')

print(isinstance(wizard_1, User))
print(isinstance(archer_1, Archer))
print(isinstance(wizard_1, Archer))

print('')
# issubclass()
print(issubclass(Wizard, User))

