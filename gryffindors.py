"""
    1. list comprehension:
        1). gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]
            i.  in the middle position: 
                is for in logic;
            ii. before for loop:
                is new list's element;
            iii. after for loop:
                can add condition to filter element;
        2).filter(function or None, iterable) --> filter object: 
            i. return an iterator yielding those items of iterable for which function(item) is true;
            ii. if function is None, return the items that are true.

    2. Python ternary expressions:
        1). A if condition else B:
            i. if condition == True, expression select A;
            ii. if condition == False, expression select B;

    3. 
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

# print(gryffindors)
# print(slytherins)
# print(houses)

def gryffindor(student):
    return student["house"] == "Gryffindor"

gryffindors_2 = filter(gryffindor, students)

gryffindors_3 = filter(lambda student: student["house"] == "Gryffindor", students)

# print(gryffindors_2) # <filter object at 0x1039eb010>
# print(gryffindors_3) # <filter object at 0x1039eb160>

def print_student(students):
    for student in students:
        print(student["name"])

print_student(gryffindors_3)
