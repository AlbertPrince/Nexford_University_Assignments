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