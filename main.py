'''with open("case_notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("File Content:\n", content)

import re
text = "Contact: qwerty@google.com, Phone: +91-98765-43210"
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
phones = re.findall(r"\+?\d[\d\-() ]{7,}\d", text)
print("Emails:", emails)
print("Phones:", phones)

import csv
with open("visits.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], "visited on", row["visit_date"])


import random

def genNum(start, end):
    return random.randint(start, end)

def guessNum(number_to_guess, max_trials):
    for i in range(max_trials):
        guessedNum = int(input("Guess a number between 1 and 10: "))
        if guessedNum == number_to_guess:
            print("Hurray!! You guessed it right!")
            return True
        else:
            attempts_left = max_trials - i - 1
            if attempts_left == 0:
                print("Sorry! You've exhausted all trials. The correct number was", number_to_guess)
            else:
                print("Try again! You have", attempts_left, "trials left.")
            
    return False

if __name__ == "__main__":
    max_trials = 3
    number_to_guess = genNum(1, 10)
    guessNum(number_to_guess, max_trials)
'''


try:
    with open("case_notes_2.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print("File Content:\n", content) 
except FileNotFoundError:
    print("Error: The file 'case_notes_2.txt' was not found.")


