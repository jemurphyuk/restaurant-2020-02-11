from general_functions import *
class Order:
    __order_integer = 1000
    order_list = []

    def __init__(self, customer):
        self.order_id = Order.__order_integer
        Order.__order_integer += 1
        self.customer = customer
        self.items = []
        self.status = 'Open'

    def add_multiple_to_order(self, item):
        self.items.extend(item)

    def add_item_to_order(self, item):
        self.items.append(item)

    def remove_last_item(self):
        self.items.pop()


    def order_calculator(self):
        order_total = 0
        for item in range(0, len(self.items)):
            price = self.items[item].price
            order_total = order_total + price
            return (set_two_dp_price(order_total))
    # def calculate_total(self):
