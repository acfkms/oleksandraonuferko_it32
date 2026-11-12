import math
import sys
from pathlib import Path
from datetime import date, timedelta
NAME = "Oleksandra"
SURNAME = "Oleksandra"
GROUP = IT-32"
print(f"{NAME} {SURNAME}, {GROUP}")
file_path = Path(__file__).parent / "data" / "expenses.csv"
expenses = {}
try:
    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                parts = line.split(";")
                if len(parts) != 4:
                    raise ValueError("Invalid number of fields")
                expense_date = date.fromisoformat(parts[0])
                amount = float(parts[2])
                if amount < 0:
                    raise ValueError("Negative amount")
                expenses[expense_date] = (
                    expenses.get(expense_date, 0) + amount
                )
            except ValueError as error:
                print(
                    f"Warning: line {line_number}: {error}",
                    file=sys.stderr
                )
except FileNotFoundError:
    print("Error: expenses.csv not found", file=sys.stderr)
    sys.exit(1)
if not expenses:
    print("No valid expenses found")
    sys.exit(0)
first_date = min(expenses)
last_date = max(expenses)
days_count = (last_date - first_date).days + 1
print(
    f"period: {first_date.strftime('%d.%m.%Y')} "
    f"({first_date.strftime('%A')}) - "
    f"{last_date.strftime('%d.%m.%Y')} "
    f"({last_date.strftime('%A')}), "
    f"{days_count} days"
)
daily_totals = []
current_date = first_date
while current_date <= last_date:
    daily_totals.append(expenses.get(current_date, 0))
    current_date += timedelta(days=1)
weekday_totals = [0.0] * 7
for current_date, amount in expenses.items():
    weekday_totals[current_date.weekday()] += amount
print()
print("weekday      total")
for i in range(7):
    weekday = date(2026, 1, 5 + i).strftime("%A")
    print(f"{weekday:<12} {weekday_totals[i]:.2f}")
total = math.fsum(daily_totals)
average = total / days_count
variance = math.fsum(
    (amount - average) ** 2 for amount in daily_totals
) / days_count
standard_deviation = math.sqrt(variance)
top_date = max(expenses, key=expenses.get)
top_amount = expenses[top_date]
no_spend_days = sum(
    1 for amount in daily_totals if amount == 0
)
print()
print(f"total:        {total:.2f}")
print(f"per day:      {average:.2f} +- {standard_deviation:.2f}")
print(
    f"top day:      {top_date.strftime('%d.%m.%Y')} "
    f"({top_date.strftime('%A')}), {top_amount:.2f}"
)
print(f"no-spend days: {no_spend_days}")
month_start = last_date.replace(day=1)
if last_date.month == 12:
    next_month = date(last_date.year + 1, 1, 1)
else:
    next_month = date(last_date.year, last_date.month + 1, 1)
days_in_month = (next_month - month_start).days
days_left = days_in_month - last_date.day
month_name = last_date.strftime("%B")
forecast = average * days_in_month
print(
    f"days in {month_name}: {days_in_month}, "
    f"left after {last_date.strftime('%d.%m')}: {days_left}"
)
print(f"month forecast: {forecast:.2f}")
