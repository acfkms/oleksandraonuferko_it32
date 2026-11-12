import math
import random
from pathlib import Path
from datetime import datetime
NAME = "Oleksandra"
SURNAME = "Onuferko"
GROUP = "IT-32"
YEAR = 209
random.seed(YEAR)
print(f"{NAME} {SURNAME}, {GROUP}")
questions = []
number = random.randint(2, 20)
value = number * number
questions.append((
    f"sqrt({value})",
    math.isqrt(value)
))
number = random.randint(3, 6)
questions.append((
    f"{number}!",
    math.factorial(number)
))
a = random.randint(20, 100)
b = random.randint(10, 50)
questions.append((
    f"gcd({a}, {b})",
    math.gcd(a, b)
))
n = random.randint(5, 10)
k = random.randint(2, n - 1)
questions.append((
    f"comb({n}, {k})",
    math.comb(n, k)
))
percent = random.choice([5, 10, 15, 20])
number = random.randint(10, 50) * 10
questions.append((
    f"{percent}% of {number}",
    percent * number // 100
))
start_time = datetime.now()
score = 0
for i, (question, correct_answer) in enumerate(questions, 1):
    answer = input(f"{i}) {question} = ")
    try:
        user_answer = int(answer)
        if user_answer == correct_answer:
            print("   correct")
            score += 1
        else:
            print(f"   wrong, answer: {correct_answer}")
    except ValueError:
        print(f"   wrong, answer: {correct_answer}")
end_time = datetime.now()
seconds = (end_time - start_time).total_seconds()
print(f"score: {score}/5, time: {seconds:.1f} s")
script_directory = Path(__file__).resolve().parent
results_directory = script_directory / "results"
results_directory.mkdir(exist_ok=True)
history_file = results_directory / "history.csv"
if not history_file.exists():
    with history_file.open("w", encoding="utf-8") as file:
        file.write("# datetime;score;seconds\n")
attempt_date = end_time.strftime("%Y-%m-%d %H:%M")
with history_file.open("a", encoding="utf-8") as file:
    file.write(
        f"{attempt_date};{score};{seconds:.1f}\n"
    )
attempts = []
with history_file.open("r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split(";")

        if len(parts) == 3:
            attempts.append((
                parts[0],
                int(parts[1]),
                float(parts[2])
            ))
best = max(
    attempts,
    key=lambda item: (item[1], -item[2])
)
print(
    f"attempts: {len(attempts)}, "
    f"best: {best[1]}/5 in {best[2]:.1f} s "
    f"({best[0]})"
)
