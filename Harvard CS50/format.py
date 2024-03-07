"""
    format data:
        1. str.split:
            don't support regular express;

        2. group ideas:
            (): either A or B;
            (...): a group, as capture;
            (?:...), non-capturing:
                ?: use the parentheses but don't capture the result;

        3. (), capturing purpose:
            1). re.search() return matches;
            2). matches.groups() return capture content;
            3). first, second... match first ()、second () and so on;
            4). matches.group(index), index is the () sequence, start with 1;
            5). ❕ groups() vs group();

        4. := operator:
            1): if a := 1+1;
            2): := allow to assign a value from right to left and ask a boolean question about it;
        

"""

import re

name = input("What's your name? ").strip()

# version 1, replace ", "
# if "," in name:
#     # [firstname, lastname] = name.split(", ") # right too
#     firstname, lastname = name.split(", ") # right and simple 😊
#     name = f"{firstname} {lastname}"

# version 2 , replace ", "、","
pattern = r"^(.+),\s*(.+)$"
# matches = re.search(pattern, name) # matches will be none(False) or Match object(True)
# print(f"matches is {matches}")
# if matches:

if matches := re.search(pattern, name):
    # firstname, lastname = matches.groups()
    # print(f"firstname is {firstname}, lastname is {lastname}")
    # name = f"{firstname} {lastname}"

    name = f"{matches.group(1)} {matches.group(2)}"


print(f"hello, {name.title()}")
