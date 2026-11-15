import json
from datetime import date
print("Oleksandra Onuferko, IT-32")
data = {
    "name": "Oleksandra",
    "date": date.today()
}
try:
    json.dumps(data)
except TypeError as error:
    print("Error:", error)
def date_to_string(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("Cannot serialize this object")
json_data = json.dumps(data, default=date_to_string)
print("First method:", json_data)
def prepare_data(data):
    return {
        "name": data["name"],
        "date": data["date"].isoformat()
    }
def restore_data(data):
    return {
        "name": data["name"],
        "date": date.fromisoformat(data["date"])
    }
with open("date.json", "w", encoding="utf-8") as file:
    json.dump(prepare_data(data), file, indent=2)
with open("date.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
loaded_data = restore_data(loaded_data)
print("Second method:", loaded_data)
print("Data equal:", data == loaded_data)
print("Date type:", type(loaded_data["date"]))