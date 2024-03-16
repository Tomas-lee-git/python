people_info = {
    "first_name": "Tomas",
    "last_name": "Lee",
    "age": 30,
    "city": "Tokyo",
}
first_name = people_info["first_name"]
last_name = people_info["last_name"]
age = people_info["age"]
city = people_info["city"]

print(f"{first_name} {last_name} is {age} and live in {city}.")


favorite_number = {
    "james": [12, 23, 24, 24],
    "lee": [698],
    "jack": [345, 33, 23523, 52, 33],
    "tom": [939, 1234, 351, 423],
}
for name, numbers in favorite_number.items():
    # print(f"{name}'s favorite number is {number}.")
    numbers_str = ""
    unique_numbers = set(numbers)
    for number in unique_numbers:  # unique
        if number == list(unique_numbers)[-1]:  # check is end
            numbers_str += f"{number}."
        else:
            numbers_str += f"{number}, "
    v = "are" if len(numbers) > 1 else "is"  # check len
    print(f"{name.title()}'s favorite number {v}: {numbers_str} ")

friends = ["tom", "eli", "james"]
for friend in friends:  # check if someone has written down their favorite number
    if friend in favorite_number.keys():
        print(f"good job,thank you, my friend {friend}.")
    else:
        print(f"hey! {friend}, quickly to write down your favorite number.")
