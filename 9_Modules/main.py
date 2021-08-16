# import filename
import utility

# import by function
# This is the recommended import way
from fruits_shop.basket import basket_func
from shop.cart.my_basket import item_basket

# Using alias with modules
from random import shuffle as sh







trans_1 = utility.multiply(0.23, 18000)
print(trans_1)
print('')
trans_2 = utility.divide(3327, .19)
print(trans_2)
print('')

cereal = basket_func('Cereal')
print(cereal)


grocery_list = item_basket(
    ['Potato', 'Tomato', 'Lettece', 'Cucumber'],
    ['Milk', 'Cereal', 'Bread']
)
print(grocery_list[0][1])


