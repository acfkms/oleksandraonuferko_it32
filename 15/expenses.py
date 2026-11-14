def parse_line(line):
    parts = line.strip().split(";")
    if len(parts) != 4:
        raise ValueError("Invalid number of fields")
    date = parts[0]
    category = parts[1]
    amount = parts[2]
    comment = parts[3]
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("Amount must be a number")
    record = {
        "date": date,
        "category": category,
        "amount": amount,
        "comment": comment
    }
    return record
def total_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        amount = record["amount"]
        if category not in totals:
            totals[category] = 0
        totals[category] += amount
    for category in totals:
        totals[category] = round(totals[category], 2)
    return totals
def load_expenses(path):
    records = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            record = parse_line(line)
            records.append(record)
    return records