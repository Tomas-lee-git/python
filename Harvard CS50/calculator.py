# int

# +(plus), -(subtract), *(multiply), /(divide), %(take the remainder)

# interactive model
# 在 CLI（Command Line Interface) 中用关键字“ python/python3 ”，可以进入 python 的运行环境，直接运行 python 代码

"""
    x = input("What's x? ")
    y = input("What's y? ")
    z = x + y

    print(z)

    n = int(x) + int(y)
    print(n)
"""
# input function return str(string)

# Nest function, 从里向外逐个执行

"""
    x1 = int(input("What's x1? "))
    y1 = int(input("What's y1? "))

    print(x1 + y1)
"""

# 太多的嵌套会导致难以阅读，增加错误的风险，难以 debug
# print(int(input("What's x1? ")) + int(input("What's y1? ")))

# float

x1 = float(input("What's x1? "))
y1 = float(input("What's y1? "))

print(f"{z1:.2f}")

z1 = round(x1 + y1)

print(f"{z1:,}")
