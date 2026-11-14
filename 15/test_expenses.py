import pytest
from expenses import parse_line
from expenses import load_expenses
from expenses import total_by_category
def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["date"] == "2026-09-21"
    assert record["category"] == "food"
    assert record["amount"] == 85.5
    assert record["comment"] == "lunch"
def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")
def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")
@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-09-21;food;85.50;lunch", "food", 85.50),
        ("2026-09-22;food;14.50;coffee", "food", 14.50),
        ("2026-09-23;transport;30.00;bus", "transport", 30.00),
        ("2026-09-24;health;120.00;medicine", "health", 120.00),
        ("2026-09-25;entertainment;50.00;movie", "entertainment", 50.00),
    ]
)
def test_parse_line_parametrize(line, expected_category, expected_amount):
    record = parse_line(line)
    assert record["category"] == expected_category
    assert record["amount"] == expected_amount
def test_total_by_category(tmp_path):
    path = tmp_path / "expenses.csv"
    path.write_text(
        "# date;category;amount;comment\n"
        "2026-09-21;food;85.50;lunch\n"
        "\n"
        "2026-09-22;food;14.50;coffee\n",
        encoding="utf-8"
    )
    records = load_expenses(path)
    totals = total_by_category(records)
    assert totals == {"food": 100.0}
def test_real_expenses_file():
    records = load_expenses("data/expenses.csv")
    totals = total_by_category(records)
    assert isinstance(totals, dict)
    assert len(totals) > 0