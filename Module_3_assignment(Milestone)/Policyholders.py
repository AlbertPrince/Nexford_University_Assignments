class Policyholders:
    def __init__(self, name, age, policy_number):
        self.name = name
        self.age = age
        self.policy_number = policy_number

    def display_info(self):
        return f"Policyholder Name: {self.name}, Age: {self.age}, Policy Number: {self.policy_number}"