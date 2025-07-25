import datetime

from enum import Enum


class PaymentStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Payment:
    def __init__(self, amount, payment_date, policy_number, status=PaymentStatus.PENDING):
        self.amount = amount
        self.payment_date = payment_date
        self.policy_number = policy_number
        self.status = status

    def display_info(self):
        return f"Payment Amount: {self.amount}, Payment Date: {self.payment_date}, Policy Number: {self.policy_number}, Status: {self.status.value}"

    def process_payment(self):
        if self.status == PaymentStatus.PENDING:
            self.status = PaymentStatus.COMPLETED
            return f"Payment of {self.amount} for policy number {self.policy_number} has been processed successfully."
        else:
            return f"Payment for policy number {self.policy_number} is already {self.status.value}."
    
    def remind_payment(self):
        payment_dt = datetime.datetime.strptime(self.payment_date, "%Y-%m-%d")
        reminder_dt = payment_dt - datetime.timedelta(weeks=1)
        today = datetime.datetime.today()
        if today >= reminder_dt and today < payment_dt:
            return f"Reminder: Payment of {self.amount} for policy number {self.policy_number} is due on {self.payment_date}."
        
    def add_penalty(self, penalty_amount):
        self.amount += penalty_amount
        return f"Penalty of {penalty_amount} has been added. New payment amount is {self.amount}."