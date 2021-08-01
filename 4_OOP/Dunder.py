"""
Dunder methods in classes
 - Allows us to use python specific functions no objects created through our class.
 - __str__ modifies methods
"""
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'John',
            'has_pets': False
        }

    # modify dunder method __str__
    def __str__(self):

        return "I'm modifying __str__ but only within action_figure object"

    # modify dunder method __len__
    def __len__(self):
        return 'Modifying the __len__'

    # modify dunder method __del__
    def __del__(self):
        print('Object Deleted!')

    # __call__
    def __call__(self, *args, **kwargs):
        return 'Yes??'

    # __getitem__(self, item)
    def __getitem__(self, item):
        return self.my_dict[item]


action_figure = Toy('red', 0)


print(action_figure.__str__())

print(action_figure.__len__())

# another way of calling a function, is using __call__ dunder method inside the class
print(action_figure.__call__())

print(action_figure['name'])
for k, v in action_figure.my_dict.items():
    print(k, v)

del action_figure

