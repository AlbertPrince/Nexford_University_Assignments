from decimal import Decimal

class User:
    def __init__(self, name, age, gender, income, expenses):
        self.name = name
        self.age = age
        self.gender = gender
        self.income = float(income) if income is not None else 0.0
        # Only include expenses that were checked or entered
        self.expenses = {k: float(v) for k, v in expenses.items() if v is not None and v != 0}

    def to_dict(self, categories):
        """
        Return a dictionary suitable for CSV export.
        categories: list of all possible expense categories to ensure consistent columns.
        """
        row = {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "income": self.income
        }
        for cat in categories:
            row[cat] = self.expenses.get(cat, 0)
        return row
