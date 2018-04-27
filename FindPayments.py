from Group import Group
from Person import Person


class FindPayments:
    def __init__(self):
        # Initialize an empty list of people to add to when prompted
        self.people_in_group = []
        self.group = Group(self.people_in_group)
        # Print Program Introduction
        print(("=" * 28) + "\n Group Payment "
              "Transfer App \n" + ("="*28))
        # Set run the program to true
        self.run_program = True
        self.start_program()

    # Takes user input and creates people and group
    def start_program(self):
        while self.run_program:
            start = input("To create a group, press 1 \n, To load your last group, press 2 \n To exit, press 0 \n"
                          + "Press h for help \n" + ("-"*28) + "\n")
            # Determine if User wants to continue, make sure they input an int.
            try:
                if int(start) == 1:
                    user_person_input = input(("-" * 28) + "\n""Enter a list of people that share bills, each separated by a comma\n")
                    self.create_group(user_person_input)
                    self.group = Group(self.people_in_group)
                    if self.group.people:
                        self.select_program_options()
                    else:
                        print("Invalid Group, must include at least one person. \n"
                              "Exiting Program")
                        self.end_program()
                # If a valid int is used that is NOT 1, even if not 0, program will exit
                if int(start) == 0:
                    self.run_program = False
                if int(start) == 2:
                    load = Load()
                    self.group = load.create_group()
                    if self.group.people:
                        self.select_program_options()
            except ValueError:
                if start == "h":
                    self.start_help(0)
                else:
                    print("That was not a valid option, exiting")
                    self.run_program = False



    def create_group(self, person):
        person = str(person)
        cont = True
        while cont:
            # End people adding
            if person == "0":
                    cont = False
            elif person == "":
                pass
            # Create Person object, and add to group list
            else:
                person = person.replace(" ", "")
                person = person.split(',')
                for ppl in person:
                    ppl = Person(ppl)
                    self.people_in_group.append(ppl)
                break
        confirm = input("These are the people you want to add to your group? \n {0}"
                    "\n Do you want to continue? \n Press 0 start over \n"
                    .format([p.name for p in self.people_in_group]))
        if confirm == "0":
            self.people_in_group = []
            self.group.people = []
            self.create_group(input(("-" * 28) + "\n""Enter a list of people that share bills, each separated by a comma\n"))
        else:
            pass

    # Display and execute user options
    def select_program_options(self):
        while self.run_program:
            main_options = input("Please Select an Option\n" +
                                 ("="*20) +
                                 "\nPress 0 to end program\n"
                                 "Press 1 to add monthly bills\n"
                                 "Press 2 to add a new person to this group\n"
                                 "Press 3 to record someone paying a bill\n"
                                 "Press 4 to record debt between two people\n"
                                 "Press 5 to list people in group\n"
                                 "Press 6 to review current bill amount \n"
                                 "Press 7 to see how much each person in your group needs to pay\n"
                                 "Press 8 to remove a member from the group\n"
                                 "Press 9 to save your info for later use\n"
                                 "Press h for help\n"
                                 )
            try:
                if main_options == "h":
                    self.start_help(1)
                    continue
                if int(main_options) == 0:
                    self.end_program()
                if int(main_options) == 1:
                    print(self.add_monthly_bill())
                if int(main_options) == 2:
                    self.create_person_entry()
                if int(main_options) == 3:
                    self.pay_towards_bill()
                if int(main_options) == 4:
                    self.debt_between_two()
                if int(main_options) == 5:
                    print(self.list_people())
                if int(main_options) == 6:
                    print(self.view_bill())
                if int(main_options) == 7:
                    self.per_person_owed()
                if int(main_options) == 8:
                    self.remove_member()
                else:
                    pass
            except ValueError:
                print("Invalid Option --- Please Select an Option")

    # Options in menu
    def end_program(self):
        self.run_program = False

    def add_monthly_bill(self):
        amount = input("How much is the bill?\n")
        self.group.record_bill(int(amount))
        return "Your current monthly bill total = {0}".format(self.group.print_bills())

    def create_person_entry(self):
        person = input("Enter a person\n")
        self.group.add_new_person(person)

    def pay_towards_bill(self):
        person = input("Person paying?\n")
        amount = input("Amount paying?\n")
        for p in self.group.people:
            if p.name == person:
                self.group.indv_pays_bill(p, int(amount))

    def debt_between_two(self):
        person_owing_name = input("Who owes money?")
        person_owed_name = input("Who is owed money?")
        amount = input("How Much?")

        for person in self.group.people:
            if person.name == person_owing_name:
                person_owing = person

        for person in self.group.people:
            if person.name == person_owed_name:
                person_owed = person
        self.group.record_debt_event(person_owed, person_owing, float(amount))

        print(person_owing.return_net_amount())

    def list_people(self):
        return [p.name for p in self.group.people]

    def view_bill(self):
        return "Your current monthly bill total = {0}".format(self.group.print_bills())

    def per_person_owed(self):
        self.group.return_amount_to_pay()

    def remove_member(self):
        name = input("Who would you like to remove?\n")
        self.group.remove_person(name)


    def start_help(self, func):
        if func == 0:
            print("This program allows you to see how much each person in a household or group needs to pay towards"
                  " the bills or collective debt. \n"
                  "Pressing 1 will allow you to enter the people in your group. 0 will end the program.")
        if func == 1:
            print("To calculate how much you'll need to pay, you need to first add in your bills using 1,\n"
                  "record how much individual members in your group owe each other with 4, and enter the amount\n"
                  "each individual has already paid this month with 3. When you're ready to calculate how much everyone"
                  "\nowes use option 7.\n"
                  "To save your group settings for future use, use option 9")

if __name__ == "__main__":
    run = FindPayments()
# FindPayments()
