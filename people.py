class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Customer(People):

    def __init__(self, name, age, address=None):
        super().__init__(name, age)
        if address is None:
            address = []
        self.address = address
        self.payment_details = {}

    def add_payment_details(self, address, card_no):
        self.payment_details['address'] = address
        self.payment_details['card_no'] = card_no
