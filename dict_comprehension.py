"""
    1. dict comprehension: 
        1). d = {k:v for k, v in iterable};
    2.
"""

students = [
    "Hermione",
    "Harry",
    "Ron",
]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
# print(f"gryffindors is {gryffindors}")

gryffindors_dict = { student: "Gryffindor" for student in students}
print(f"gryffindors_dict is {gryffindors_dict}")
