from pathlib import Path
class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
    def is_big(self, limit):
        return self.amount > limit
    def describe(self):
        return (
            f"{self.date} {self.category} "
            f"{self.amount:.2f} ({self.comment})"
        )
BASE = Path(__file__).resolve().parent
CSV = BASE / "data" / "expenses.csv"
expenses = []
with open(CSV, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(";")
        if len(parts) < 4:
            continue
        date = parts[0]
        category = parts[1]
        amount = float(parts[2])
        comment = ";".join(parts[3:])
        expense = Expense(date, category, amount, comment)
        expenses.append(expense)
limit = 100
print("All expenses:", len(expenses))
print("Big expenses:")
for expense in expenses:
    if expense.is_big(limit):
        print(expense.describe())