"""
    >、>=, <、<=, ==、!=

    if
        条件语句没有()
        : 之后的缩进行代表条件分支内容

    elif => else if 的简写

    else catch-all（兜底条款），如果前面的条件都是true，会进入这里的逻辑

    or  连接多个条件，符合其中一个条件，都会进入相关的逻辑

    and 连接多个条件，符合其中所有的条件，才会进入相关的逻辑

    注意 = 和 == 的区别，如果在 if 条件语句中使用了 = ，就会得到下面的报错：
        SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
"""

x = int(input("What's x? "))
y = int(input("What's y? "))

if x > y:
    print("x is greater than y")

elif x < y:
    print("x is less than y")

else:
    print("x is equal y")

if x > y or x < y:
    print("x is not equal y")
else:
    print("x is equal y 😊")

if x != y:
    print("x is not equal y")
else:
    print("x is equal y 😊😊😊")
