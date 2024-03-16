# empty object {}
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

new_point = alien_0["points"]
print(f"You just earned {new_point} points!")

# add new key-value pair
alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

# modify value
alien_0["color"] = "yellow"

print(alien_0)

alien_0["speed"] = "fast"

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment

print(alien_0)

# delete key-value pair
del alien_0["points"]
print(alien_0.get("points", "Sorry, points is not exist"))  # dict(key, default)
# print(alien_0["points"]) # KeyError: 'points'
print(alien_0)

favorite_languages = {
    "jen": "python",
    # 一种不错的做法是，在最后一个键值对后面也加上逗号，为以后添加键值对做好准备
    "phil": "python",
}

for name in favorite_languages:
    favorite_language = favorite_languages[name].title()
    print(f"{name}'s favorite language is {favorite_language}")

# dict.items() D.items() -> a set-like object providing a view on D's items
print("============")
for name, language in favorite_languages.items():
    print(f"{name}'s favorite language is {language.title()}")

items = favorite_languages.items()
keys = favorite_languages.keys()
values = favorite_languages.values()

# dict_items([('jen', 'python'), ('phil', 'python')]) type is <class 'dict_items'>
print(f"{items} type is {type(items)}")
# dict_keys(['jen', 'phil']) type is <class 'dict_keys'>
print(f"{keys} type is {type(keys)}")
# dict_values(['python', 'python']) type is <class 'dict_values'>
print(f"{values} type is {type(values)}")

# sorted
# sorted() # Return a new list containing all items from the iterable in ascending order.

# set
set()  # set() -> new empty set object set(iterable) -> new set object

print(
    set(favorite_languages.values())
)  # {'python'} <= 花括号里面没有键值对，只有元素，称之为“集合”


aliens = []
for i in range(5):
    if i % 2 == 0:
        aliens.append(
            {
                "color": "green",
                "speed": "slow",
                "points": 5,
            }
        )
    else:
        aliens.append(
            {
                "color": "yellow",
                "speed": "medium",
                "points": 10,
            }
        )
print(aliens)
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
        # 必须得用 dict 的引用，通过 key 来修改 value，直接替换 dict 引用不会生效
        # alien = {
        #     "color": "yellow",
        #     "speed": "medium",
        #     "points": 10,
        # }
    else:
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15
        # 必须得用 dict 的引用，通过 key 来修改 value，直接替换 dict 引用不会生效
        # alien = {
        #     "color": "red",
        #     "speed": "fast",
        #     "points": 15,
        # }
print("========")
print(aliens)

"""
    当函数调用 print() 中的字符串很长，需要分成多行书写时：
        1. 在合适的位置分行，在每行的末尾都加上"";
        2. 对于除第一行外的其他各行，都在行首加上引号并缩进;
        3. 这样，Python 将自动合并括号内的所有字符串；
"""
word = "hello"
print(
    f"{word} it's too long {word} it's too long"
    f" {word} it's too long {word} it's too long"
)

# A if condition == True else B
string = "hello" if 3 < 2 else "hi"
print(string)
