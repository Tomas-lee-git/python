cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# 条件测试即布尔值（bool）：值为 True 或 False 的表达式；

# = assign, == equal;

# !=, not equal;

# > greater, < less, >= greater and equal, <= less and equal;

# A and B, A and B all is True;

# A or B, either A or B is True;

# 为了改善可读性，可以在 and 和 or 的两边使用 ();

# in, check if element in list;
print(f"'suzuki' in cars is { 'suzuki' in cars}")

# not in, check if element not in list;
print(f"'suzuki' in cars is { 'suzuki' not in cars}")

# condition statement
age = 18
if age < 18:
    # print(f"Sorry, you are too young to vote, wait another {18 - age} years!")
    # print(f"Please registered to vote as soon as you turn 18")
    ...
elif age <= 100:
    # print(f"Your age {age} is enough old to vote!")
    # print("Have you registered to vote yet?")
    ...
else:
    # print(f"OMG, you are {age} years old, you are so lucky!")
    ...


# False => 0, '', "", None, [], (), {}
if 0 and '' and "" and None and [] and () and {}:
    print("Those are False")
else:
    print("False => 0, '', " ", None, [], (), {}")
