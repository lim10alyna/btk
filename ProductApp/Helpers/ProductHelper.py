from Models.Product import Product

class ProductHelper:

    @staticmethod
    def create_item_from_text(text):
        items = text.split(',')
        name = items[0].strip()
        price = float(items[1].strip())
        quantity = int(items[2].strip())
        return Product(name, price, quantity)

    @staticmethod
    def get_total_balance(products):
        total_balance = 0
        for product in products:
            total_balance += product.get_total_price()
        total_balance *= 1.20  # %20 KDV ekle
        return total_balance
