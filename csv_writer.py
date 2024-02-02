"""
    csv.writer:
        1). writer.writerow(list):
            
"""

import csv

questions = ["name","breed","age","evaluate"]
answers = []

for question in questions:
    answers.append(input(f"what's your {question} ? "))

with open("colleagues.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow(answers) 