import re, csv
from collections import Counter

# Read notes file
with open("case_notes.txt", "r", encoding="utf-8") as f:
    notes = f.read()

indian_pattern = r"\+91-\d{5}-\d{5}" # r"\+91-\d{10}" 
us_pattern = r"\(\d{3}\) \d{3}-\d{4}"

phones = re.findall(indian_pattern, notes) + re.findall(us_pattern, notes)
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", notes)
artifacts = re.findall(r"ART-\d{4}-[A-Z0-9]{4}", notes)

# Analyze visitor logs from CSV
names = []
with open("visits.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        names.append(row["name"])

visit_counts = Counter(names)

# Write Investigation Report
report = []
report.append("MUSEUM INVESTIGATION REPORT\n")
report.append(f"Phones found in notes: {phones}")
report.append(f"Emails found in notes: {emails}")
report.append(f"Artifact codes mentioned: {artifacts}")
report.append("Visitor frequency:")
for name, count in visit_counts.items():
    report.append(f" - {name}: {count} visits")
# print(report)

with open("museum_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("Museum investigation report generated -> museum_report.txt")