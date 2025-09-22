import re, csv
from collections import Counter

# Read notes file
with open("case_notes.txt", "r", encoding="utf-8") as f:
    notes = f.read()

# 👉 TODO: extract phone numbers into 'phones'
# phones = ...

# 👉 TODO: extract emails into 'emails'
# emails = ...

# 👉 TODO: extract artifact codes like ART-2025-XY12 into 'artifacts'
# artifacts = ...

# Analyze visitor logs from CSV
names = []
with open("visits.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # 👉 TODO: collect names into the 'names' list
        pass  

# 👉 TODO: use Counter to count number of visits for each visitor
# visit_counts = ...

# Write Investigation Report
report = []
report.append("MUSEUM INVESTIGATION REPORT\n")

# 👉 TODO: append phones, emails, artifacts, and visit counts to report
# report.append(...)

with open("museum_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("Museum investigation report generated -> museum_report.txt")
