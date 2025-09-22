"""
with open("case_notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("File Content:\n", content)

import re
text = "Contact: qwerty@google.com, Phone: +91-98765-43210"
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
phones = re.findall(r"\+?\d[\d\-() ]{7,}\d", text)
print("Emails:", emails)
print("Phones:", phones)
"""

import csv
with open("visits.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], "visited on", row["visit_date"])
