for n in range(1, 21):
    # print(f"n is {n}")
    ...

list_1_1000000 = [n for n in range(1, 1000001)]
for n in list_1_1000000:
    # print(n)
    ...
# print(f"max is {max(list_1_1000000)}")
# print(f"min is {min(list_1_1000000)}")
# print(f"sum is {sum(list_1_1000000)}")

n_1_20 = [n for n in range(1, 21, 2)]
for n in n_1_20:
    # print(f"n is {n}")
    ...

n_3_30 = [n for n in range(3, 31) if n % 3 == 0]
for n in n_3_30:
    # print(f"n is {n}")
    ...

n_1_10 = [n**3 for n in range(1, 11)]
for n in n_1_10:
    # print(f"n is {n}")
    ...

player = ["charles", "martina", "michael", "florence", "eli"]

print(f"this first three items in the list are {player[:3]}")
print(f"three items from the middle of the list are {player[1:4]}")
print(f"this last three items in the list are {player[-3:]}")
