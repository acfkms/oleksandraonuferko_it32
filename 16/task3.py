import json
import sys
print("Oleksandra Onuferko, IT-32")
settings = {
    "owner": "Oleksandra Onuferko",
    "group": "IT-32",
    "currency": "UAH",
    "monthly_limit": 6000,
    "categories": ["food", "transport", "fun"]
}
try:
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)
except FileNotFoundError:
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=2, ensure_ascii=False)
    print("settings.json not found, default created")
    sys.exit(0)
except json.JSONDecodeError as error:
    print("JSON error on line", error.lineno, file=sys.stderr)
    sys.exit(1)
with open("data/expenses.json", "r", encoding="utf-8") as file:
    expenses = json.load(file)
spent = sum(item["amount"] for item in expenses)
limit = settings["monthly_limit"]
left = limit - spent
print(f"limit: {limit:.2f} UAH, spent: {spent:.2f} UAH, left: {left:.2f} UAH")