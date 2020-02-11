
class FoodItems:
    def __init__(self, item, price, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.ingredients = ingredients
        self.item = item
        self.price = price

class Side(FoodItems):
    pass

class Main(FoodItems):
    pass

class Combo(FoodItems):
    def __init__(self, item, price, ingredients=None, list_individual_items=None):
        super().__init__(item, price, ingredients)
        if list_individual_items is None:
            list_individual_items = []
        self.list_individual_items = list_individual_items


