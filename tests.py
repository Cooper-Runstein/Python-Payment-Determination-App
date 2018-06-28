import unittest
import Person
import Group

class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person1 = Person.Person("Bob")
        self.person2 = Person.Person("Jim", 500)

    def test_name(self):
        assert self.person1.name == "Bob"
        assert self.person2.name == "Jim"
    
    def test_value(self):
        assert self.person1.return_net_amount() == 0
        assert self.person2.return_net_amount() == 500
    
    def test_add_charge(self):
        self.person1.add_charge(500)
        self.person2.add_charge(-200)
        assert self.person1.return_net_amount() == 500
        assert self.person2.return_net_amount() == 300

class GroupTests(unittest.TestCase):
    def setUp(self):
        self.person1 = Person.Person("Bob")
        self.person2 = Person.Person("Jim", 500)
        self.person3 = Person.Person("Jen", -700)
        self.person4 = Person.Person("Billy", 300)
        self.group1 = Group.Group([self.person1, self.person2, self.person3, self.person4])
        self.group2 = Group.Group([self.person1, self.person2, self.person3, self.person4], 1000)
        self.group3 = Group.Group([self.person1, self.person2], 700)
    
    def test_initial_bills(self):
        assert self.group1.print_bills() == 0
        assert self.group2.print_bills() == 1000
        assert self.group3.print_bills() == 700
    
    def test_altered_bills(self):
        self.group1.record_bill(100)
        self.group2.record_bill("F")
        self.group3.record_bill(-200)
        assert self.group1.print_bills() == 100
        assert self.group2.print_bills() == 1000
        assert self.group3.print_bills() == 500

    def test_added_debt(self):
        self.group1.record_debt_event(self.person1, self.person2, 500)
        assert self.person1.return_net_amount() == -500
        assert self.person2.return_net_amount() == 1000


if __name__ == '__main__':
    unittest.main()