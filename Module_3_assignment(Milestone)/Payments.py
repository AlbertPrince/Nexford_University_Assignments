import datetime


class Payments:
    def __init__(self, amount, payment_date, policy_number):
        self.amount = amount
        self.payment_date = payment_date
        self.policy_number = policy_number

    def display_info(self):
        return f"Payment Amount: {self.amount}, Payment Date: {self.payment_date}, Policy Number: {self.policy_number}"
    
    def process_payment(self):
        return f"Payment of {self.amount} for policy number {self.policy_number} has been processed on {self.payment_date}."
    
    def remind_payment(self):
        payment_dt = datetime.datetime.strptime(self.payment_date, "%Y-%m-%d")
        reminder_dt = payment_dt - datetime.timedelta(weeks=1)
        today = datetime.datetime.today()
        if today >= reminder_dt and today < payment_dt:
            return f"Reminder: Payment of {self.amount} for policy number {self.policy_number} is due on {self.payment_date}."