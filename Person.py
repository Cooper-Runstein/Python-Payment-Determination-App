class Person:

    def __init__(self, name, amount = 0):
        self._name = name
        self.net_amount = amount

    @ property
    def name(self):
        return self._name

    def add_charge(self, amount):
        self.net_amount += amount

    def return_net_amount(self):
        return self.net_amount
