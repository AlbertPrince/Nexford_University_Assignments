from policyholder import Policyholder
from product import Policy_Product
from payment import Payment
    

if __name__ == "__main__":
    # Create two policyholders
    policyholder1 = Policyholder(name="John Doe", age=30, policy_number="POL12345")
    print(policyholder1.register_policyholder())
    
    policyholder2 = Policyholder(name="Jane Smith", age=28, policy_number="POL12346")
    print(policyholder2.register_policyholder())
    
    # Create 2 products
    product1 = Policy_Product(product_name="Health Insurance", product_id="PROD001", price=500.0)
    print(product1.create_product())
    
    product2 = Policy_Product(product_name="Car Insurance", product_id="PROD002", price=300.0)
    print(product2.create_product())
    
    # Add product to policyholder
    print(policyholder1.add_product(product1))
    print(policyholder2.add_product(product2))
    
    # Create 2 payments
    payment1 = Payment(amount=500.0, payment_date="2023-10-01", policy_number="POL12345")
    print(payment1.display_info())

    payment2 = Payment(amount=300.0, payment_date="2023-10-02", policy_number="POL12346")
    print(payment2.display_info())

    # Process the payments
    print(payment1.process_payment())
    print(payment2.process_payment())

    # Add payment to policyholder
    print(policyholder1.add_payment(payment1))
    print(policyholder2.add_payment(payment2))

    # Display policyholder info
    print(policyholder1.display_info())
    print(policyholder2.display_info())