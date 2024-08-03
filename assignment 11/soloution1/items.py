

class Item:
    # Class variable for the default discount
    default_discount = 0.20

    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price  # Use a protected variable for price
        self.quantity = quantity

    def calculate_total_price(self):
        # Calculate total price before discount
        total_price = self._price * self.quantity
        return total_price

    def apply_discount(self):
        # Apply discount and calculate final price
        total_price = self.calculate_total_price()
        discounted_price = total_price * (1 - Item.default_discount)
        return discounted_price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        raise AttributeError("Price cannot be directly modified. Use a method to update it.")

    @classmethod
    def all_items(cls, items):
        # List all items with their discounted prices
        print("Items and their discounted prices:")
        for item in items:
            discounted_price = item.apply_discount()
            print(f"Name: {item.name}, Price: ${item.price:.2f}, Quantity: {item.quantity}, Discounted Price: ${discounted_price:.2f}")

    @staticmethod
    def load_items_from_csv(file_path):
        items = []
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, price, quantity = row
                item = Item(name, float(price), int(quantity))
                items.append(item)
        return items