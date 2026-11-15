import requests
import sys
URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 50.75,
    "longitude": 25.34,
    "current": "temperature_2m,wind_speed_10m"
}
try:
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    current = data["current"]
    print("Oleksandra Onuferko, IT-32")
    print("Lutsk (50.75, 25.34):")
    print("Temperature:", current["temperature_2m"], "C")
    print("Wind:", current["wind_speed_10m"], "km/h")
except requests.RequestException as error:
    print("Network error:", error, file=sys.stderr)
    sys.exit(1)