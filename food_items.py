
class FoodItems:
    food_items_list = []

    def __init__(self, item, price, allergies=None):
        self.item = item
        self.price = price
        if allergies is None:
            allergies = []
        self.allergies = allergies
        FoodItems.__add_food_item_to_list(self)

    @classmethod
    def __add_food_item_to_list(cls, food):
        cls.food_items_list.append(food)

    @classmethod
    def get_food_items_dict(cls):
        for i in range(0, len(FoodItems.food_items_list)):
            food_data = (cls.food_items_list[i])
            print(vars(food_data))
        return

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




