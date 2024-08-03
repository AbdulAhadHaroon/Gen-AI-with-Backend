# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date()

    def calculate_age(self):
        today = datetime.today().date()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def __str__(self):
        return f"Name: {self.name}\nCountry: {self.country}\nDate of Birth: {self.date_of_birth.strftime('%m/%d/%Y')}\nAge: {self.calculate_age()}"

name = input("Enter name: ")
country = input("Enter country: ")
date_of_birth = input("Enter date of birth (MM/DD/YYYY): ")

person = Person(name, country, date_of_birth)
print("\nPerson Information:")
print(person)

# Write a Python program to create a calculator class. Include methods for basic arithmetic operations
class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        
        print("Addition:", calc.add(a, b))
        print("Subtraction:", calc.subtract(a, b))
        print("Multiplication:", calc.multiply(a, b))
        print("Division:", calc.divide(a, b))
    except ValueError as e:
        print(e)


# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name]['quantity'] <= quantity:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity
        else:
            print(f"Item '{item_name}' not found in the cart.")
    
    def calculate_total(self):
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total
    
    def __str__(self):
        if not self.items:
            return "The shopping cart is empty."
        
        cart_contents = []
        for item_name, details in self.items.items():
            cart_contents.append(f"{item_name}: ${details['price']} x {details['quantity']}")
        
        cart_contents.append(f"Total: ${self.calculate_total():.2f}")
        return "\n".join(cart_contents)

if __name__ == "__main__":
    cart = ShoppingCart()
    
    while True:
        action = input("Would you like to 'add', 'remove', or 'view' your cart? (Type 'quit' to exit): ").lower()
        
        if action == 'quit':
            break
        elif action == 'add':
            item_name = input("Enter the item name: ")
            price = float(input("Enter the price of the item: "))
            quantity = int(input("Enter the quantity of the item: "))
            cart.add_item(item_name, price, quantity)
        elif action == 'remove':
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity to remove: "))
            cart.remove_item(item_name, quantity)
        elif action == 'view':
            print("\nShopping Cart:")
            print(cart)
        else:
            print("Invalid action. Please choose 'add', 'remove', or 'view'.")




# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
class Customer:
    def __init__(self, name, account_number, initial_balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Customer: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name, account_number, initial_balance=0):
        if account_number not in self.customers:
            self.customers[account_number] = Customer(name, account_number, initial_balance)
            return True
        return False

    def remove_customer(self, account_number):
        if account_number in self.customers:
            del self.customers[account_number]
            return True
        return False

    def deposit(self, account_number, amount):
        customer = self.customers.get(account_number)
        if customer:
            return customer.deposit(amount)
        return False

    def withdraw(self, account_number, amount):
        customer = self.customers.get(account_number)
        if customer:
            return customer.withdraw(amount)
        return False

    def get_balance(self, account_number):
        customer = self.customers.get(account_number)
        if customer:
            return customer.get_balance()
        return None

    def __str__(self):
        if not self.customers:
            return "No customers in the bank."
        return "\n".join(str(customer) for customer in self.customers.values())


# Example usage
if __name__ == "__main__":
    bank = Bank()

    while True:
        action = input("Would you like to 'add', 'remove', 'deposit', 'withdraw', 'balance', or 'view' all customers? (Type 'quit' to exit): ").lower()
        
        if action == 'quit':
            break
        elif action == 'add':
            name = input("Enter customer name: ")
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance (default 0): ") or 0)
            if bank.add_customer(name, account_number, initial_balance):
                print("Customer added successfully.")
            else:
                print("Account number already exists.")
        elif action == 'remove':
            account_number = input("Enter account number to remove: ")
            if bank.remove_customer(account_number):
                print("Customer removed successfully.")
            else:
                print("Account number not found.")
        elif action == 'deposit':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if bank.deposit(account_number, amount):
                print("Deposit successful.")
            else:
                print("Deposit failed. Check account number or amount.")
        elif action == 'withdraw':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if bank.withdraw(account_number, amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed. Check account number or insufficient funds.")
        elif action == 'balance':
            account_number = input("Enter account number: ")
            balance = bank.get_balance(account_number)
            if balance is not None:
                print(f"Account balance: ${balance:.2f}")
            else:
                print("Account number not found.")
        elif action == 'view':
            print("\nBank Customers:")
            print(bank)
        else:
            print("Invalid action. Please choose 'add', 'remove', 'deposit', 'withdraw', 'balance', or 'view'.")


# n this exercise, you will create a Python class named Student to represent students. 
# The class should have the following attributes and methods:
class Student:
    available_courses = ["English", "Urdu", "Physics", "Math", "Chemistry"]
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
    def enroll(self, course):
        if course in Student.available_courses:
            if course not in self.courses:
                self.courses.append(course)
                print(f"{self.name} has been enrolled in {course}.")
            else:
                print(f"{self.name} is already enrolled in {course}.")
        else:
            print(f"{course} is not available. Please choose from the available courses.")
    
    def list_courses(self):
        if self.courses:
            print(f"{self.name} is enrolled in the following courses:")
            for course in self.courses:
                print(f"- {course}")
        else:
            print(f"{self.name} is not enrolled in any courses.")
    
    @classmethod
    def list_available_courses(cls):
        print("Available courses:")
        for course in cls.available_courses:
            print(f"- {course}")

# Create instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 19)

# Enroll students in courses
student1.enroll("Math")
student1.enroll("Biology")  # Invalid course

student2.enroll("Physics")
student2.enroll("English")

student3.enroll("Chemistry")
student3.enroll("Math")
student3.enroll("Urdu")

# Call list_courses
print("\nStudent Courses:")
student1.list_courses()
student2.list_courses()
student3.list_courses()

# Call list_available_courses
print("\nAvailable Courses:")
Student.list_available_courses()