from people import People, Customer
from food_items import *

customer1 = Customer('John', 32, 'SW4')
customer2 = Customer('Ana', 24, 'EC1A')

seabass = Main('seabass', 14.5, ['Fish'])
omlette = Main('omlette du fromage', 9, ['Egg', 'Dairy'])
pizzaF = Main('pizza florentine', 5.5, ['Egg', 'Dairy', 'Gluten'])

garlic_bread = Side('Garlic Bread', 4, ['Gluten', 'Dairy'])
fries = Side('Fries', 3.5)
salad = Side('Salad', 3.5)

water = FoodItems('Water', 2)
coke = FoodItems('Coca-Cola', 3, ['Sulfites'])
milkshake = FoodItems("Reese's Milkshake", 3.5, ['Dairy', 'Nuts'])