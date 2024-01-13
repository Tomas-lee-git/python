"""
    bool, python 的 boolean 类型数据，只有两个值: True、False（首字母必须大写）
"""

X = int(input("What's X ? "))

def isOdd(n):
    return n % 2


# 版本1
if X  % 2 == 0:
    print("X is even")
else:
    print("X is odd")




# if 0:
#     print("0 is true")
# else:
#     print("0 is false")

# 版本2
if X % 2:
    print("X is odd")
else:
    print("X is even")