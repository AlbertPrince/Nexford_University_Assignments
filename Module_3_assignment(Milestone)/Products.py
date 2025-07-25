class Products:
    def __init__(self, product_name, product_id, price):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price

    def display_info(self):
        return f"Product Name: {self.product_name}, Product ID: {self.product_id}, Price: {self.price}"