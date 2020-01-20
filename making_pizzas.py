"""Importing modules from other files"""

# import pizza_func file for making pizzas)

import pizza_func

# call the make_pizza function from the pizza_func file
pizza_func.make_pizza(16, 'pepperoni')
pizza_func.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

""" Importing using from module import function"""

from pizza_func import make_pizza

make_pizza(17, 'pepperoni', 'sausage')


"""Importing using alias"""

from pizza_func import make_pizza as mp

mp(18, 'green peppers', 'mushrooms', 'extra cheese')
