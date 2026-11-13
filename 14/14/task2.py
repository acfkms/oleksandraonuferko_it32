import csv
from tabulate import tabulate
filename = "data/expenses.csv"
expenses = {}
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(",")
        if len(parts) < 3:
            continue
        category = parts[1].strip()
        amount = float(parts[2].strip())
        if category not in expenses:
            expenses[category] = {
                "count": 0,
                "total": 0.0
            }
        expenses[category]["count"] += 1
        expenses[category]["total"] += amount
table = []
total_count = 0
total_amount = 0.0
for category, values in expenses.items():
    table.append([
        category,
        values["count"],
        f'{values["total"]:.2f}'
    ])
    total_count += values["count"]
    total_amount += values["total"]
table.append([
    "TOTAL",
    total_count,
    f"{total_amount:.2f}"
])
print("Олександра Онуферко, ІТ-32")
print(tabulate(
    table,
    headers=["category", "count", "total"],
    tablefmt="github"
))
