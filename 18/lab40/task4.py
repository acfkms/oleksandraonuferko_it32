from pathlib import Path
class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment
    def describe(self):
        return (
            f"{self.date} {self.category} "
            f"{self.amount:.2f} ({self.comment})"
        )
class ExpenseBook:
    def __init__(self):
        self.expenses = []
    def add(self, expense):
        self.expenses.append(expense)
    def total(self):
        return sum(expense.amount for expense in self.expenses)
    def by_category(self, category):
        return sum(
            expense.amount
            for expense in self.expenses
            if expense.category == category
        )
    def top(self, n):
        return sorted(
            self.expenses,
            key=lambda expense: expense.amount,
            reverse=True
        )[:n]
BASE = Path(__file__).resolve().parent
CSV = BASE / "data" / "expenses.csv"
book = ExpenseBook()
with open(CSV, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(";")
        if len(parts) < 4:
            continue
        expense = Expense(
            parts[0],
            parts[1],
            float(parts[2]),
            ";".join(parts[3:])
        )
        book.add(expense)
print("Total expenses:", f"{book.total():.2f}")
categories = sorted(set(
    expense.category for expense in book.expenses
))
print("\nExpenses by category:")
for category in categories:
    print(category, f"{book.by_category(category):.2f}")
print("\nTop 3 expenses:")
for expense in book.top(3):
    print(expense.describe())