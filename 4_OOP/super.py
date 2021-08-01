"""
super()
 - super() is used in class inheritance, in the sub-class for passing attributes from
   the parent class.
 - super() refers to the class inherited from.
   super().__init__(params)


Object Introspection
 - The ability to determine the type of an object at run-time (when the code is running).
 - dir(object_name) will return all attributes and methods an instance has.

"""
print('')


class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email=email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Wizard Attack Power: {self.power}')


class Archer(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Archer Attack Power: {self.power}')


# users:
wizard_1 = Wizard('Merlin', 15, 'merlin@avalon.com')

archer_1 = Archer('Robin', 100, 'robin@cherrywood.com')

# function
print('function')


def player_attack(char):
    return char.attack()


player_attack(wizard_1)
player_attack(archer_1)

print('for loop')
for char in [archer_1]:
    archer_1.attack()

print('')
print(wizard_1.email)

print('')
print('Object Introspection')
# object introspection
print(dir(wizard_1))