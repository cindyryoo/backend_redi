
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


class Chef(Person):
    def __init__(self, name, phone, email, address, salary, cuisine_expertise):
        super().__init__(name, phone, email)
        self.address = address
        self.salary = salary
        self.cuisine_expertise = cuisine_expertise

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


# customer1 = Customer("Julie", 123456789, "xxx@gmail.com")
# customer1.send_book_table_request()
# customer1.give_order()
# customer1.ask_bill()

# restaurant_manager1 = Restaurant_manager(
#     "Thomas", 123456789, "abc@gmail.com", "Munich", "3000")

# restaurant_manager1.staff_payroll()
# restaurant_manager1.calculate_billing()
# restaurant_manager1.provide_bill()

# server1 = Servers("Eric", 123456789, "xxx@gmail.com", "Kalrsplatz", "2000")
# server1.fulfill_book_table_request()
# server1.take_customer_order()
# server1.send_order_to_kitchen()

# chef1 = Chef("Gerhard", 123456789, "xxx@gmail.com",
#              "Marienplatz", "4000", "Itelian dish")
# chef1.take_dish_name("pasta")
# chef1.prep_dish_name("pasta")
