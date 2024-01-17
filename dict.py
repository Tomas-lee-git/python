"""
    dict => dictionaries
        associate one value with another literally
        keys、values
        访问value的方法 => dict[key]


"""

students = {
    "Tom": "Cat",
    "Jimmy": "Mouse",
    "Bob": "Cat",
    "Down": "Dog"
}

print(students["Tom"])

#⚠️ for in 循环，在dict 中拿到的是 key，在 list 中拿到的 value
for student in students:
    match students[student]:
        case "Cat":
            print(student, "meow", sep=", ")
        case "Dog":
            print(student, "wow", sep=", ")
        case _:
            print(student, "zizi", sep=", ")