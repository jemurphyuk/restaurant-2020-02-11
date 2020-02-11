from people import People, Customer
from food_items import *
from order import Order

customer1 = Customer('John', 32, 'SW4')
customer2 = Customer('Ana', 24, 'EC1A')

seabass = Main('seabass', 14.5, ['Fish'])
omlette = Main('omlette du fromage', 9, ['Egg', 'Dairy'])
pizza_f = Main('pizza florentine', 5.5, ['Egg', 'Dairy', 'Gluten'])

garlic_bread = Side('Garlic Bread', 4, ['Gluten', 'Dairy'])
fries = Side('Fries', 3.5)
salad = Side('Salad', 3.5)

water = FoodItems('Water', 2)
coke = FoodItems('Coca-Cola', 3, ['Sulfites'])
milkshake = FoodItems("Reese's Milkshake", 3.5, ['Dairy', 'Nuts'])

# opening tab to order
# order1 = Order(customer1)
#
# order1.add_items_order([pizza_f, milkshake])
#
# #print(seabass, omlette, pizza_f)
# order_total = 0
# for item in range(0, len(order1.items)):
#     price = order1.items[item].price
#     order_total = order_total + price
#     price_order_total = "{0:.2f}".format(order_total)
#
#
# print(price_order_total)