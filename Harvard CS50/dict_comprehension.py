"""
    1. dict comprehension: 
        1). d = {k:v for k in iterable};

    2. for in:
        1). to dict, for key in dict, get every key;
        2). to list, for element in dict, get every element;

    3. enumerate(iterable, start = 0):
        1). return an enumerate object:
                the enumerate object yields pairs containing a count (from start, which defaults to zero) 
                and a value yielded by the iterable argument;
        2). for index,val in enumerate(iterable, start = 1):
            i. index is iterable's sequence, from 0 + start;
            i. val is iterable's element(list), key(dict);
"""

students = [
    "Hermione",
    "Harry",
    "Ron",
]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
# print(f"gryffindors is {gryffindors}")

gryffindors_dict = { student: "Gryffindor" for student in students}
# print(f"gryffindors_dict is {gryffindors_dict}")

for i in range(len(students)):
    # print(f"{i + 1} {students[i]}")
    ...

for index,val in enumerate(students, start = 1):
    # print(f"{index} {val}")
    ...


# for key,val in enumerate(gryffindors_dict, start = 1):
#     print(f"{key} {val}")
    
# for key, val in gryffindors_dict:
#     # print(f"{key} {val}")
    ...
print(f"gryffindors_dict {gryffindors_dict}")

d = {k:k+"123" for k in gryffindors_dict}

print(f"d is {d}")