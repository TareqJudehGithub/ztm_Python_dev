# Cats everywhere
# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
tom = Cat('Tom', 3)
rob = Cat('Rob', 2)
kitty = Cat('Kitty', 4)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)


# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat(tom.age, rob.age, kitty.age)} years old.')

print('\n')
# 'Exercise: Pets everywhere'
print('Exercise: Pets everywhere')


class Pets():
    # class object attributes:
    animals = []

    def __init__(self, animals):
        # instance attributes
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add another Cat
class Tom(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [
    Simon('Simon', 5), Sally('Sally', 7), Tom('Tom', 3)
]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()

print('\n')


# Char and Classes


class Stats:
    def __init__(self, str, int, agi, sta):
        self.strength = str
        self.intellect = int
        self.agility = agi
        self.stamina = sta

    def introduce(self):
        return


class Char(Stats):
    characters = list

    def __init__(self, name, race, gender, str, int, agi, sta):
        super().__init__(str, int, agi, sta)
        self.name = name
        self.race = race
        self.gender = gender

    def char_details(self):
        return f'Character Details:\n' \
               f'Name: {self.name}\n' \
               f'Race: {self.race}\n' \
               f'Gender: {self.gender}\n' \
               '\n' \
               f'Stats:\n' \
               f'Str: {self.strength}\n' \
               f'Int: {self.intellect}\n' \
               f'Agi: {self.agility}\n' \
               f'Sta: {self.stamina}\n' \
               '\n'


human_paladin = Char('Uther', 'Human', 'Male', 22, 18, 16, 23)
gnome_mage = Char('Chrome', 'Gnome', 'Female', 16, 25, 17, 20)
print(human_paladin.char_details())

chars_list = list()
chars_list.append(human_paladin)
chars_list.append(gnome_mage)

for char in chars_list:
    print(char.name)

print('')
print('============================================')

print('Exercise: Extending List')


# Exercise: Extending List


class SuperList(list):
    def __init__(self, item_name, my_list):
        super().__init__(my_list)
        self.item = item_name

    def list_sum(self):
        return sum(self)
    # or return sum(instance_name)

    def avg_calc(self):
        return sum(self) / len(self)

    def add_item(self):
        return super_list2.append(self.item)

super_list1 = SuperList(100, my_list=[1, 2, 3, 4, 5])


# super_list1 length
print(len(super_list1))

# super_list1 sum
print(super_list1.list_sum())
print(sum(super_list1))

# super_list1 average
print(super_list1.avg_calc())

print('')
super_list2 = SuperList('Mango', list(['Apple', 'Orange', 'Bananas', 'Cherry']))
super_list2.append('Peaches')
super_list2.add_item()

for item in super_list2:
    print(item)

print('')

print(issubclass(SuperList, list))



