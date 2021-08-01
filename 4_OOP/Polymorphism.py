"""
Polymorphism
 - Polymorphism (meaning many forms), refers to the way in which object classes can share
   the same method name.
 - Polymorphism enables us to redefine methods for sub-classes.
 - Polymorphism is useful because we are able to modify our classes to our specific needs.
 - Polymorphism is useful it prevents repetition.

"""
print('')

class User:

    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do nothing!')


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
        User.attack(self)
        print(f'Arrows: {self.arrows}')


# users:
wizard_1 = Wizard('Merlin', 15)
archer_1 = Archer('Robin', 100)

print('')
print('functions')
# creating a function to access classes methods
def player_attack(char):
    char.attack()


player_attack(wizard_1)


print('')
print('for loop')
# for loop
for char in [wizard_1, archer_1]:
    char.attack()


