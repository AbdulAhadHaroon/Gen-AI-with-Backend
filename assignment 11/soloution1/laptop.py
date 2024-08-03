from items import Item

class Laptop(Item):
    # Class variable for the laptop-specific discount
    laptop_discount = 0.30

    def __init__(self, name, price, quantity, gpu, port_count):
        super().__init__(name, price, quantity)
        self.gpu = gpu
        self.port_count = port_count

    def apply_discount(self):
        # Apply laptop-specific discount
        total_price = self.calculate_total_price()
        discounted_price = total_price * (1 - Laptop.laptop_discount)
        return discounted_price

    def __str__(self):
        return (f"Laptop: {self.name}, Price: ${self._price:.2f}, Quantity: {self.quantity}, "
                f"GPU: {self.gpu}, Ports: {self.port_count}, Discounted Price: ${self.apply_discount():.2f}")