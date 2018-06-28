import unittest
import Person

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

if __name__ == '__main__':
    unittest.main()