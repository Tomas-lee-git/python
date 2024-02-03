"""
    1. csv.writer:
        1). add row data by list [column1 content, column1 content……]:
            writer = csv.writer(file)
            writer.writerow(list)
        2).add row data by dict {key1: value1;key2: value2……}:
            csv.DictWriter(f, fieldnames) 
                The fieldnames parameter is a sequence of keys that identify the order in which values in the dictionary passed to the writerow() method are written to file
                    fieldnames is a required parameter because dict has no order and we need to tell the writer how to add the values in order
            writer.writerow(dict)

    2. ❕don’t mess with csv files manually😂；


"""

import csv

# option1: add row data by list

# questions = ["name","breed","age","evaluate"]
# answers_list = []

# for question in questions:
#     answers_list.append(input(f"what's your {question} ? "))

# with open("colleagues.csv","a") as file:
#     writer = csv.writer(file)
#     writer.writerow(answers_list) 


# option2: add row data by dict {key1: value1;key2: value2……}

questions = ["name","breed","age","evaluate"]
answers_dict = {}

for question in questions:
    answers_dict[question] = input(f"what's your {question} ? ")

print(f"answers_dict is {answers_dict}")

with open("colleagues.csv","a") as file:
    writer = csv.DictWriter(file, questions)
    writer.writerow(answers_dict) 