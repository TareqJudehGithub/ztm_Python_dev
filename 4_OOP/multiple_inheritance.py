"""
Multiple Inheritance
 -
"""


class User:
    def sign_in(self):
        return 'Logged in!'


class Wizard(User):
    def __init__(self, name, intellect):
        self.name = name
        self.int = intellect

    def attack_power(self):
        return f'Wizard int: {self.int}'

    def frost_bolt(self):
        return 'Attack with Frost Bolt.'


class Archer(User):
    arrows = 10

    def __init__(self, name, agility, arrow):
        self.name = name
        self.agi = agility
        self.arrow = arrow

    def attack_power(self):
        return f'Archer agi: {self.agi}'

    def aim_shot(self):
        return 'Attack with Aimed Shot.'

    def use_arrow(self):
        # self.arrow = 1
        if True:
            Archer.arrows -= self.arrow
            return Archer.arrows


# create a character that has both the wizard and the archer power
class HybridBorg(Wizard, Archer):
    def __init__(self, name, agility, bolts):
        Archer.__init__(self, name=name, agility=agility, arrow=bolts)


ranger = HybridBorg('Dave', 15, 1)
print(ranger.frost_bolt())
print(ranger.aim_shot())
print(ranger.use_arrow())

print(ranger.name, ranger.agi, ranger.arrow)

ghandalf = Wizard('Ghandalf', 30)
print(ghandalf.name, ghandalf.int)

print(ranger.sign_in())
