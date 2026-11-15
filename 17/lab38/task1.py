import requests
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
try:
    response = requests.get(URL, params={"json": ""}, timeout=10)
    response.raise_for_status()
    rates = response.json()
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Currencies:", len(rates))
    for currency in rates:
        if currency["cc"] in ["USD", "EUR"]:
            print(
                currency["cc"],
                currency["rate"],
                currency["exchangedate"]
            )
except requests.RequestException as error:
    import sys
    print("Network error:", error, file=sys.stderr)
    sys.exit(1)