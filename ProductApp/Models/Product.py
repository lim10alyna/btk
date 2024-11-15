from datetime import datetime

class Product:
    def __init__(self, name="Unknown", price=0, quantity=1):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._validate_attributes()
        print(f"Product {self._name} created at {datetime.now()}")

    def _validate_attributes(self):
        if len(self._name) < 3 or len(self._name) > 8:
            raise ValueError("Name must be between 3 and 8 characters.")
        if self._price < 0:
            raise ValueError("Price cannot be negative.")
        if self._quantity < 1:
            raise ValueError("Quantity must be at least 1.")

    def get_total_price(self):
        return self._price * self._quantity

    def __str__(self):
        return f"Product Name: {self._name}, Price: {self._price}, Quantity: {self._quantity}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3 or len(value) > 8:
            raise ValueError("Name must be between 3 and 8 characters.")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 1:
            raise ValueError("Quantity must be at least 1.")
        self._quantity = value
