# Build following classes for restaurant related persons:
# Chef -
# It has name, phone, email, address, salary, cuisine_expertise as data variables.
# It has take_dish_name() and prep_dish() methods.
# Restaurant_manager -
# It has name, phone, email, address, salary as data variables.
# It has staff_payroll(), calculate_billing() and provide_bill() methods.
# Servers -
# It has name, phone, email, address, salary as data variables.
# It has fulfill_book_table_request(), take_customer_order() and send_order_to_kitchen() methods.
# Customer -
# It has name, phone, email as data variables.
# It has send_book_table_request(), give_order() and ask_bill() as methods.

class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class Servers(Person):
    def __init__(self, name, phone, email, address, salary):
        super().__init__(name, phone, email)
        self.address = address
        self.salary = salary

    def fulfill_book_table_request(self):
        print(f"{self.name} fulfill book table request")

    def take_customer_order(self):
        print(f"{self.name} takes customer_order")

    def send_order_to_kitchen(self):
        print(f"{self.name} sends order to kitchen")


class Chef(Servers):
    def __init__(self, name, phone, email, address, salary, cuisine_expertise):
        super().__init__(name, phone, email)

    def take_dish_name(self, dish_name):
        self.dish_name = dish_name
        print(f"{self.name} takes {dish_name}")

    def prep_dish_name(self, dish_name):
        self.dish_name = dish_name
        print(f"{self.name} prepare {dish_name}")


class Restaurant_manager(Person):

    def __init__(self, name, phone, email, address, salary):
        super().__init__(name, phone, email)
        self.address = address
        self.salary = salary

    def staff_payroll(self):
        print(f"{self.name} calculates staff payroll")

    def calculate_billing(self):
        print(f"{self.name} calculates billing")

    def provide_bill(self):
        print(f"{self.name} provides bill")


class Customer(Person):

    def __init__(self, name, phone, email):
        super().__init__(name, phone, email)

    def send_book_table_request(self):
        print(f"{self.name}  sends book table request")

    def give_order(self):
        print(f"{self.name} gives order")

    def ask_bill(self):
        print(f"{self.name} asks bill")


customer1 = Customer("Julie", 123456789, "xxx@gmail.com")
customer1.send_book_table_request()
