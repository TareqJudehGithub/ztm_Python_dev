# Create a class for cars, showing car model, color, and price.
class Car:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        self.car_info()

    def car_info(self):
        print('f Model: {}\nColor: {}\nPrice: {}'.format(self.model, self.color, self.price))


bmw = Car('BMW', 'Grey', '$1000')
print('')

GMC = Car('GMC', 'Charcoal', '$15000')
print('')

print(GMC.price)


