# tuple is immutable

# () 只是让元祖看起来更整洁、更清晰，可以不加的，但每个元素后面都需要加逗号
dimensions = (100, 200, 300)
print(f"dimension is {dimensions}, type is {type(dimensions)}")  # <class 'tuple'>

# dimensions.append(23) # AttributeError: 'tuple' object has no attribute 'append'

# del dimensions[0] # TypeError: 'tuple' object doesn't support item deletion

# dimensions[0] = 120 # TypeError: 'tuple' object does not support item assignment

print(f"slice is {dimensions[0: 2]} ok")  # slice is (100, 200) ok

# AttributeError: 'tuple' object has no attribute 'pop'
# print(f"pop is {dimensions.pop()} ok")

for dimension in dimensions:
    print(dimension)

dimensions = (20, 30, 40)  # reassign new tuple to variable is ok
print(f"dimension is {dimensions}, type is {type(dimensions)}")
