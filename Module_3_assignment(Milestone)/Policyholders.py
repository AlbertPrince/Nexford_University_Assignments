class Policyholders:
    def __init__(self, name, age, policy_number, is_suspended=False, is_registered=False):
        self.name = name
        self.age = age
        self.policy_number = policy_number
        self.is_suspended = is_suspended
        self.is_registered = is_registered

    def display_info(self):
        return f"Policyholder Name: {self.name}, Age: {self.age}, Policy Number: {self.policy_number}"
    
    def register_policyholder(self):
        self.is_registered = True
        return f"Policyholder {self.name} has been registered."

    def suspend_policyholder(self):
        self.is_suspended = True
        return f"Policyholder {self.name} has been suspended."
    
    def reactivate_policyholder(self):
        self.is_suspended = False
        return f"Policyholder {self.name} has been reactivated."