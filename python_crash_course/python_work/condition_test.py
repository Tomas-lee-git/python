# print(f"car == CAR is { 'car' == 'CAR'}") # False
# print(f"car == CAR.lower() is { 'car' == 'CAR'.lower()}") # True

# print(f"5 > 3 is { 5 > 3 }") # True
# print(f"5 < 3 is { 5 < 3 }")  # False
# print(f"5 >= 3 is { 5 >= 3 }") # True
# print(f"5 <= 3 is { 5 <= 3 }") # False
# print(f"5 != 3 is { 5 != 3 }") # True

# print(f"5 >= 3 and 4 <= 8 is { 5 >= 3 and 12 <= 8 }")  # False
# print(f"5 >= 3 or 4 <= 8 is { 5 >= 3 or 42 <= 8 }") # True

n_list = [1, 2, 3, 4, 5]

# print(f"5 in n_list is {5 in n_list}") # True
# print(f"8 not in n_list is { 8 not in n_list}") # True

alien_color = "green"
if alien_color == "green":
    # print("You got 5 points")
    ...
elif alien_color == "yellow":
    # print("You got 10 points")
    ...
elif alien_color == "red":
    # print("You got 15 points")
    ...

age = 18
if age < 2:
    # print("You are a baby!")
    ...
elif age < 4:
    # print("You are a toddler!")
    ...
elif age < 13:
    # print("You are a child!")
    ...
elif age < 18:
    # print("You are a youngster!")
    ...
elif age < 65:
    # print("You are a young and middle-aged people!")
    ...
else:
    # print("You are an old man!")
    ...

fruit = "watermelon"
favorite_fruits = ["apple", "banana", "strawberry", "grape", "orange", "watermelon"]
if fruit in favorite_fruits:
    # print(f"You really like {fruit}")
    ...

# names = []
names = ["ada", "bill", "dowson", "admin", "collie"]

if names:
    for name in names:
        if name == "admin":
            # print(f"Hello {name}, would you like to see a status report?")
            ...
        else:
            # print(f"hello {name}, thank you for logging in again.")
            ...
else:
    # print("we need to find some users!")
    ...

current_users = ["Ada", "bill", "dowsOn", "admIn", "collie"]
new_users = ["Dowson", "adMin", "toms", "CollIe", "eric"]
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        # print(f"{new_user} is exist, please set a new username")
        ...
    else:
        # print(f"{new_user} is ok to be use")
        ...

number_list = list(range(1, 10))
# print(number_list)

for number in number_list:
    if number == 1:
        print(f"1 is {number}st")
    elif number == 2:
        print(f"2 is {number}nd")
    elif number == 3:
        print(f"3 is {number}rd")
    else:
        print(f"{number} is {number}th")
