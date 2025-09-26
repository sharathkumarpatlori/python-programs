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

try:
    with open("case_notes_2.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print("File Content:\n", content) 
except FileNotFoundError:
    print("Error: The file 'case_notes_2.txt' was not found.")

import pandas as pd

df = pd.read_csv("sales.csv")
df["revenue"] = df["units"] * df["price"] 
print(df)
'''

# Task: Ask user for their favorite color and print: 'Your favorite color is BLUE'.
input_color = input("Enter your favorite color: ")
print(f"Your favorite color is {input_color}.")

# Task: Store your name and age in variables and print: 
# 'Hello, my name is X and I am Y years old.'    
name = "Ram"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")

# Task: Make a list of 3 fruits and print them one by one.
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

# Task: Create a dictionary for a student: {'name': 'Alice', 'grade': 'A'} and 
# print values.
my_dict = {"name": "Alice"}
print(my_dict["name"])

# Create a dictionary with key and multiple pairs
students_dict = {'students': {'name' : 'Ram', 'roll_no' : '2005'}}
print(students_dict['students'])
print(students_dict['students']['roll_no'])

# Task: Write a program that checks if a number is positive or negative.
if number := int(input("Enter a number: ")):
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# Task: Write a function square(x) that returns the square of a number.
def square(x):
    return x * x
print(square(5))

# Task: Ask user for a number and handle the case if they type text instead.
try:
    user_input = int(input("Enter a number: "))
    print(f"You entered the number: {user_input}")
except ValueError:
    print("That's not a valid number. Please enter a numeric value.")