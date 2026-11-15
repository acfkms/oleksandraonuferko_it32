import requests
import json
import os
import time
import sys
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
CACHE_FILE = "cache/rates.json"
def get_rates():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, encoding="utf-8") as file:
            cache = json.load(file)
        age = time.time() - cache["timestamp"]
        if age < 3600:
            print("Source: cache (age", int(age), "seconds)")
            return cache["rates"]
    response = requests.get(
        URL,
        params={"json": ""},
        timeout=10
    )
    response.raise_for_status()
    rates = response.json()
    cache = {
        "timestamp": time.time(),
        "rates": rates
    }
    os.makedirs("cache", exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump(cache, file, ensure_ascii=False, indent=4)
    print("Source: api (cache saved)")
    return rates
try:
    print("Oleksandra Onuferko, IT-32")
    rates = get_rates()
    for currency in rates:
        if currency["cc"] in ["USD", "EUR"]:
            print(
                currency["cc"],
                currency["rate"],
                currency["exchangedate"]
            )
except requests.RequestException as error:
    print("Network error:", error, file=sys.stderr)
    sys.exit(1)
except (ValueError, KeyError, OSError) as error:
    print("Cache error:", error, file=sys.stderr)
    sys.exit(1)