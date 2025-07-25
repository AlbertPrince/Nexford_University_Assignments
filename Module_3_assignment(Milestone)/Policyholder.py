from enum import Enum

class AccountStatus(Enum):
    ACTIVE = "Active"
    SUSPENDED = "Suspended"

class Policyholder:
    def __init__(self, name, age, policy_number, status=AccountStatus.ACTIVE):
        self.name = name
        self.age = age
        self.policy_number = policy_number
        self.status = status
        self.products = []
        self.payments = []

    def display_info(self):
        return f"Policyholder Name: {self.name}, Age: {self.age}, Policy Number: {self.policy_number}, Status: {self.status.value}, Products: {len(self.products)}, Payments: {len(self.payments)}"
    
    def register_policyholder(self):
        self.status = AccountStatus.ACTIVE
        return f"Policyholder {self.name} has been registered."

    def suspend_policyholder(self):
        self.status = AccountStatus.SUSPENDED
        return f"Policyholder {self.name} has been suspended."
    
    def reactivate_policyholder(self):
        self.status = AccountStatus.ACTIVE
        return f"Policyholder {self.name} has been reactivated."
    
    def add_product(self, product):
        self.products.append(product)
        return f"Product {product.product_name} has been added to policyholder {self.name}."
    
    def add_payment(self, payment):
        self.payments.append(payment)
        return f"Payment of {payment.amount} has been added for policyholder {self.name}."
    
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            return f"Product {product.product_name} has been removed from policyholder {self.name}."
        else:
            return f"Product {product.product_name} not found for policyholder {self.name}."
        
    def remove_payment(self, payment):
        if payment in self.payments:
            self.payments.remove(payment)
            return f"Payment of {payment.amount} has been removed for policyholder {self.name}."
        else:
            return f"Payment of {payment.amount} not found for policyholder {self.name}."
    
    def display_products(self):
        return [product.display_info() for product in self.products]

    def display_payments(self):
        return [payment.display_info() for payment in self.payments]