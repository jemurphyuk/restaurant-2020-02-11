class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Customer(People):
    __customer_integer = 1
    customer_list = []

    def __init__(self, name, age, address=None):
        super().__init__(name, age)
        self.customer_id = Customer.__customer_integer
        Customer.__customer_integer += 1
        if address is None:
            address = []
        self.address = address
        self.__payment_details = {}
        Customer.append_customer_to_list(self)

    def add_payment_details(self, address, card_no):
        self.__payment_details['address'] = address
        self.__payment_details['card_no'] = card_no

    def send_payment_details(self):
        return self.__payment_details

    @classmethod
    def append_customer_to_list(cls, customer):
        cls.customer_list.append(customer)