from Helpers.ProductHelper import ProductHelper
from Models.Product import Product

def main():
    # Ürün dosyasını oku
    with open("Products.txt", "r") as file:
        products = []
        for line in file.readlines():
            product = ProductHelper.create_item_from_text(line)
            products.append(product)
    
    # Ürünlerin toplam fiyatını hesapla
    total_balance = ProductHelper.get_total_balance(products)
    print(f"Total Balance with 20% VAT: {total_balance:.2f}")

if __name__ == "__main__":
    main()
