
class Order:
    __order_integer = 1000
    order_list = []

    def __init__(self, customer):
        self.order_id = Order.__order_integer
        Order.__order_integer += 1
        self.customer = customer
        self.items = []
        self.status = 'Open'

    def add_items_order(self, item):
        self.items.extend(item)


    def order_calculator(self):
        order_total = 0
        for item in range(0, len(self.items)):
            price = self.items[item].price
            order_total = order_total + price
            price_order_total = "{0:.2f}".format(order_total)
    # def calculate_total(self):
