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
print(f"motorcycles is {motorcycles}")

# access element by index
motorcycles[0] = "ducati"
print(f"motorcycles is {motorcycles}")

# append element as last element
motorcycles.append("honda")
print(f"motorcycles is {motorcycles}")

# add element to special position
motorcycles.insert(1, "bmw")
print(f"motorcycles is {motorcycles}")

# del element and don't use anymore
del motorcycles[1]
print(f"motorcycles is {motorcycles}")

# pop element and save popped element
popped_last_motorcycle = motorcycles.pop()
print(f"motorcycles is {motorcycles}")
print(f"popped_last_motorcycle is {popped_last_motorcycle}")

popped_index_motorcycle = motorcycles.pop(1)
print(f"motorcycles is {motorcycles}")
print(f"popped_index_motorcycle is {popped_index_motorcycle}")

# remove element by value
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(f"motorcycles is {motorcycles}")
print(f"I remove {too_expensive} because its too expensive for me")
