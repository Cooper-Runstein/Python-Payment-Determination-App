from Person import Person


class Group:
    def __init__(self, people, bills = 0):
        self.people = people
        self.bills = bills

    def people_names_return(self):
        for person in self.people:
            print(person.name)

    def add_new_person(self, name):
        name = Person(name)
        self.people.append(name)

    def remove_person(self, name):
        for person in self.people:
            if person.name == name:
                self.people.remove(person)

    def record_bill(self, amount):
        self.bills += amount

    def print_bills(self):
        return float(self.bills)

    def record_debt_event(self, person_owing, person_owed, amount):
        try:
                person_owing.add_charge(float(-1*amount))
                person_owed.add_charge(float(amount))
        except TypeError:
            print("Amount needs to be a numerical value. Try Again.")

    def return_individuals_netamount(self):
        for person in self.people:
            name = person.name
            print(person.net_amount, '----', str(name), "amount in account")

    def return_amount_to_pay(self):
        for person in self.people:
            name = person.name
            amount = self.bills/len(self.people)+person.return_net_amount()
            if amount > 0:
                print("{0} needs to pay {1}".format(name, amount))
            elif amount == 0:
                print("Nothing is owed by {0} month".format(str(name)))
            elif amount < 0:
                print("{0} is owed {1}".format(name, amount))

    def indv_pays_bill(self, person, amount):
        person.add_charge(amount*-1)
