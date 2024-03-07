"""
    list:
        list[index],可以用 index 取出 list 中的一个具体的内容；
        for in 循环中，i 代表的直接是 list 中的具体元素；
        python 中除了 list，还有其它 iterable 类型的数据，都可以用到 for 循环；
    len():
        len function will return iterable data's length；
        使用 len() 函数获取 list 的长度，
        然后借用 range() 函数生成一个 index list，
        最后用 i 和 list[i] 来分别获取 index 和 element；
"""

students = ["Bob", "Tom", "Eric"]

print(students[0])

# ❕ for in 循环，在dict 中拿到的是 key，在 list 中拿到的 value
for student in students:
    print(student)

for i in range(len(students)):
    print(i, students[i])
