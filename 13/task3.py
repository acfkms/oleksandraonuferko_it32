import sys
import math
from pathlib import Path
from datetime import datetime
NAME = "Oleksandra"
SURNAME = "Onuferko"
GROUP = "IT-32"
print(f"{NAME} {SURNAME}, {GROUP}")
args = sys.argv[1:]
dry_run = False
if len(args) == 2 and args[0] == "--dry-run":
    dry_run = True
    directory = Path(args[1])
elif len(args) == 1:
    directory = Path(args[0])
else:
    print("usage: python3 task3.py [--dry-run] <dir>")
    sys.exit(2)
if not directory.exists() or not directory.is_dir():
    print(f"error: {directory} is not a directory",
          file=sys.stderr)
    sys.exit(1)
files = [p for p in directory.iterdir() if p.is_file()]
if not files:
    print("No files found")
    sys.exit(0)
files.sort(key=lambda p: p.stat().st_mtime)
plan = []
units = ["B", "KB", "MB", "GB"]
for file in files:
    info = file.stat()
    size = info.st_size
    modified = datetime.fromtimestamp(info.st_mtime)
    if size == 0:
        unit_index = 0
        size_value = 0
    else:
        unit_index = min(
            int(math.log(size, 1024)),
            3
        )
        size_value = size / (1024 ** unit_index)
    folder_name = modified.strftime("%Y-%m")
    destination = directory / folder_name / file.name
    plan.append((
        file,
        destination,
        size_value,
        units[unit_index],
        modified
    ))
for file, destination, size, unit, modified in plan:
    if destination.exists():
        print(
            f"error: {destination} already exists, nothing was moved",
            file=sys.stderr
        )
        sys.exit(1)
for file, destination, size, unit, modified in plan:
    print(
        f"{file.name:<20} "
        f"{size:6.1f} {unit:2}  "
        f"{modified.strftime('%d.%m.%Y %H:%M')}  "
        f"-> {destination.parent.name}/"
    )
folders = set(
    destination.parent.name
    for file, destination, size, unit, modified in plan
)
if dry_run:
    print(
        f"{len(files)} files, {len(folders)} folders "
        "(dry run, nothing moved)"
    )
    sys.exit(0)
for file, destination, size, unit, modified in plan:
    destination.parent.mkdir(exist_ok=True)
    file.rename(destination)
print(f"{len(files)} files, {len(folders)} folders")
script_directory = Path(__file__).resolve().parent
reports_directory = script_directory / "reports"
reports_directory.mkdir(exist_ok=True)
now = datetime.now()
report_name = now.strftime("organize_%Y%m%d_%H%M.txt")
report_path = reports_directory / report_nam
with report_path.open("w", encoding="utf-8") as report:
    for file, destination, size, unit, modified in plan:
        report.write(
            f"{file.name} -> {destination.parent.name}/\n"
        )
print(f"report saved to: reports/{report_name}")
