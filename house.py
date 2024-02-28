"""
    1. set:
        1). python's data type;
        2). collection of values wherein there are no duplicates, 
            in that somehow any duplicates are eliminated;
        3). use set() to generate a set type data;
        4). use add to add element for set: set().add(element);

    2. list vs set:
        1). [] or list() vs set();
        2). [].append(element) vs set().add(element);
    3. sorted(list):
        1). sorted list by alphabetically;
"""

students = [
    {"names":"Hermione", "house":"Gryffindor"},
    {"names":"Harry", "house":"Gryffindor"},
    {"names":"Ron", "house":"Gryffindor"},
    {"names":"Draco", "house":"Slytherin"},
    {"names":"Padma", "house":"Ravenclaw"},
]

# collect unique house name

# version 1
house = []
for student in students:
    if student["house"] not in house:
        house.append(student["house"])
print(f"version 1, house is {sorted(house)}")

# version 1
house = set()
for student in students:
    house.add(student["house"])
print(f"version 1, house is {sorted(house)}")
