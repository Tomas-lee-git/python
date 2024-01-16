"""
    for，可以用来循环 list 数据
    list: [1,2,3]
    range(n)函数:
        n: 指定list的内容：0-n，不包括n;
        return: list [0,……,n-1]
    _:
        在 python 中，如果定义的参数不需要直接使用，习惯使用 _ 来表示
        如果将来用到了，用更明确的变量名称来替换
        _ 本身也是可以正确的拿到值的
"""

# for i in  [0, 1, 2]:
for i in  range(3):
    print(i, "wow")

# 在 python 中，如果定义的参数不需要直接使用，习惯使用 _ 来表示
for _ in  range(3):
    print(_ , "wow")

for i in  range(3):
    if i < 2:
        print(i, "wow")

