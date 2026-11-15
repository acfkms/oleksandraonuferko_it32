import requests
import csv
import sys
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
NAME = "Oleksandra Onuferko, IT-32"
def get_rate(code):
    response = requests.get(
        URL,
        params={"valcode": code, "json": ""},
        timeout=10
    )
    response.raise_for_status()
    data = response.json()
    return data[0]["rate"], data[0]["exchangedate"]
try:
    total = 0
    with open("expenses.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["amount"])
    usd, date = get_rate("USD")
    eur, date = get_rate("EUR")
    print(NAME)
    print("Rate date:", date)
    print(f"Total: {total:.2f} UAH")
    print(f"USD: {total / usd:.2f}")
    print(f"EUR: {total / eur:.2f}")
except requests.RequestException as error:
    print("Network error:", error, file=sys.stderr)
    sys.exit(1)
except (ValueError, KeyError, IndexError, OSError) as error:
    print("Data error:", error, file=sys.stderr)
    sys.exit(1)