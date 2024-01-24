"""
    bool, python 的 boolean 类型数据，只有两个值: True、False（首字母必须大写）
"""

x = int(input("What's x ? "))

def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False

    # return True if n % 2 == 0 else False
    
    return n % 2 == 0

# 版本1
if x  % 2 == 0:
    print("x is even")
else:
    print("x is odd")




# if 0:
#     print("0 is true")
# else:
#     print("0 is false")

# 版本2
if is_even(x):
    print("x is even")
else:
    print("x is odd")