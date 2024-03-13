# list can contain multiple elements, so its name should be plural(+s)
bicycles = ["trek", "cannondale", "readline", "specialized"]

# start with 0
first_element = bicycles[0]
second_element = bicycles[1]
# print(f"first_element is {first_element.title()}")
# print(f"second_element is {second_element.title()}")

# negative number can be used to represent counting from the end
last_element = bicycles[-1]
second_to_last_element = bicycles[-2]
# print(f"last_element is {last_element.title()}")
# print(f"second_to_last_element is {second_to_last_element.title()}")

motorcycles = ["honda", "yamaha", "suzuki"]
# print(f"motorcycles is {motorcycles}")

# access element by index
motorcycles[0] = "ducati"
# print(f"motorcycles is {motorcycles}")

# append element as last element
motorcycles.append("honda")
# print(f"motorcycles is {motorcycles}")

# add element to special position
motorcycles.insert(1, "bmw")
# print(f"motorcycles is {motorcycles}")

# del element and don't use anymore
del motorcycles[1]
# print(f"motorcycles is {motorcycles}")

# pop element and save popped element
popped_last_motorcycle = motorcycles.pop()
# print(f"motorcycles is {motorcycles}")
# print(f"popped_last_motorcycle is {popped_last_motorcycle}")

popped_index_motorcycle = motorcycles.pop(1)
# print(f"motorcycles is {motorcycles}")
# print(f"popped_index_motorcycle is {popped_index_motorcycle}")

# remove element by value
too_expensive = "ducati"
motorcycles.remove(too_expensive)
# print(f"motorcycles is {motorcycles}")
# print(f"I remove {too_expensive} because its too expensive for me")

motorcycles = ["ducati", "bmw", "yamaha", "suzuki", "honda"]

# Sort the list in ascending order and return None.
sort_motorcycles = motorcycles.sort(reverse=True)
# print(f"motorcycles is {motorcycles}")
# print(f"sort_motorcycles is {sort_motorcycles}") # None

# Return a new list containing all items from the iterable in ascending order.
sorted_motorcycles = sorted(motorcycles, reverse=True)
# print(f"motorcycles is {motorcycles}")
# print(f"sorted_motorcycles is {sorted_motorcycles}") # None

# reverse original list and return none
reverse_motorcycles = motorcycles.reverse()
# print(f"motorcycles is {motorcycles}")
# print(f"reverse_motorcycles is {reverse_motorcycles}") # None

# get list length
length = len(motorcycles)
# print(f"motorcycles's length is {length}")

# [][0] # IndexError: list index out of range

# for in
magicians = ["alice", "david", "carolina"]

# print("\t=== start cycle ===")
for magician in magicians:  # magician is a dynamic variable
    # print(f"{magician.title()}, that was a great trick!")
    # print(f"I cant't wait to see your next trick, {magician.title()}.\n")
    ...

# print("Thank you, everyone. That was a great magic show!\n")
# print("\t=== end cycle ===")

"""
    IndentationErrors:
        1. IndentationError: expected an indented block after ...;
        2. IndentationError: unexpected indent;
        
    SyntaxError:
        1. SyntaxError: expected:':';
        
"""
japanese_foods = ["うどん", "そば", "お弁当", "お茶", "お粥", "親子丼", "卵"]
for japanese_food in japanese_foods:
    # print(f"I like {japanese_food}")
    ...
# print("I really love japanese food!")

# range(stop) -> range object range(start, stop[, step]) -> range object
for n in range(3, 5):
    # print(n)
    ...
# print(type(range(3))) # <class 'range'>
# print(type(list(range(3)))) # <class 'list'>

even_numbers = list(range(0, 11, 2))
# print(f"even_numbers is {even_numbers}") # [0, 2, 4, 6, 8, 10]

pow_2_even_numbers = []

for number in range(1, 11):
    pow_2_even_numbers.append(number**2)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(f"pow_2_even_numbers is {pow_2_even_numbers}")


# min(), max(), sum()
max_n = max(pow_2_even_numbers)
min_n = min(pow_2_even_numbers)
sum_total = sum(pow_2_even_numbers)
# print(f"pow_2_even_numbers is {pow_2_even_numbers}")
# print(f"the largest element in pow_2_even_numbers is {max_n}")
# print(f"the smallest element in pow_2_even_numbers is {min_n}")
# print(f"the sum of pow_2_even_numbers is {sum_total}")

# list comprehension, create new list in one line code
pow_2_even_numbers_ = [number**2 for number in range(1, 11)]
# print(f"pow_2_even_numbers_ is {pow_2_even_numbers_}")

# slice => list[start:stop:step]
player = ["charles", "martina", "michael", "florence", "eli"]
# print(player[0:1]) # ['charles']
# print(player[1:3]) # ['martina', 'michael']

# if ignore start index, slice from list[0]
# print(player[:3]) # ['charles', 'martina', 'michael']

# print(player[2:-1]) # ['michael', 'florence']

# if ignore end index, slice to list[-1], include list[-1]
# print(player[2:]) # ['michael', 'florence', 'eli']

# if ignore start index and end index, a copy of the whole array
# print(player[:]) # ['michael', 'florence', 'eli']

# step: 代表每隔多少个元素提取一个
# print(player[0:5:2]) # ['michael', 'florence', 'eli']

# copy list: ignore start and end
player_copy = player[:]
print(f"player is {player}, length is {len(player)}")
print(f"player_copy is {player_copy}, length is {len(player_copy)}")
