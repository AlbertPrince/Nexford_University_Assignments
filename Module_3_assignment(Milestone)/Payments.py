class Payments:
    def __init__(self, amount, payment_date, policy_number):
        self.amount = amount
        self.payment_date = payment_date
        self.policy_number = policy_number

    def display_info(self):
        return f"Payment Amount: {self.amount}, Payment Date: {self.payment_date}, Policy Number: {self.policy_number}"