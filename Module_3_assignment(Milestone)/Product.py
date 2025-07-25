class Policy_Product:
    def __init__(self, product_name, product_id, price):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price

    def display_info(self):
        return f"Product Name: {self.product_name}, Product ID: {self.product_id}, Price: {self.price}"

    def create_product(self):
        return f"Product {self.product_name} with ID {self.product_id} has been created at a price of {self.price}."
    
    def update_product(self, new_price):
        self.price = new_price
        return f"Product {self.product_name} with ID {self.product_id} has been updated to a new price of {self.price}."
    
    def delete_product(self):
        return f"Product {self.product_name} with ID {self.product_id} has been deleted."