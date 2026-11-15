import requests
import sys
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
def test_request(url, timeout):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        print("Request successful")
    except requests.ConnectionError:
        print("Connection error: no internet connection", file=sys.stderr)
        sys.exit(1)
    except requests.Timeout:
        print("Timeout error: request took too long", file=sys.stderr)
        sys.exit(1)
    except requests.HTTPError as error:
        print("HTTP error:", error, file=sys.stderr)
        sys.exit(1)
    except requests.RequestException as error:
        print("Network error:", error, file=sys.stderr)
        sys.exit(1)
print("Test 1: Connection error")
test_request(URL, 10)
print("Test 2: HTTP 404 error")
test_request(
    "https://bank.gov.ua/this-page-does-not-exist",
    10
)
print("Test 3: Timeout error")
test_request(URL, 0.001)