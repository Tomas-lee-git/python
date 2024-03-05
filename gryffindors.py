"""
    1. list comprehension:
        1). gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]
            i.  in the middle position: 
                is for in logic;
            ii. before for loop:
                is new list's element;
            iii. after for loop:
                can add condition to filter element;
        2).
    2.
"""

students = [
    {"name":"Hermione", "house":"Gryffindor"},
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Ron", "house":"Gryffindor"},
    {"name":"Draco", "house":"Slytherin"},
    {"name":"Padma", "house":"Ravenclaw"},
]

gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]
slytherins = [ student["name"] for student in students if student["house"] == "Slytherin" ]
houses = [ student["house"] for student in students]

print(gryffindors)
print(slytherins)
print(houses)
