"""
    一、sys:
        sys.argv:
            argv => argument vector: 参数向量
            用 list 的方式记录了运行 python3 时后面的内容：
                1. sys.argv[0]: program name，也就是 *.py
                2. sys.argv[1]: something else input
                3. 字符串输入的，即使有空格，再长都算一个喽
                4. 如果没有输入，或者输入的内容对应 list 的 index 不存在：
                    IndexError: list index out of range
        sys.exit:
            exit program and recept a string parameter as prompt message


    二、如果加入了不必要的 indentation(缩进)，会报错：😄
        IndentationError: unexpected indent
    
    三、if:
        elif 可以有无限多个；
        但 else 只能有一个，用来 catch-all（兜底）；

    四、slice 操作:
        1. 注意到了 python 的 str 也就是 string 类型的数据也是 iterable 的
            所以可以使用 for in 来处理 str 哦🤔
        2. list[start:end]
            start 和 end 指 slice 操作时的 list index；
            截取的元素包含 start 但不包含 end；
            可以只指定 start 但忽略 end ：list[start:] 来表示从start 位置开始的剩余全部；
            如果 start 和 end 是 native int，代表：从后往前数，其它规则不变；
            如果 end 超过了实际 index 的最大值，效果等同于 list[start:]；
"""

import sys


def main():
    # sys_arg_version_1()
    # sys_arg_version_2()
    # sys_arg_version_3()
    sys_arg_version_4()


# 　version 1，处理报错
def sys_arg_version_1():
    try:
        print(f"hello, my name is {sys.argv[1]}")

    except IndexError:
        print("please add your name before hit Enter key")


# version 2，灵活应对
def sys_arg_version_2():
    argv_list = sys.argv
    if len(argv_list) == 2:
        print(f"hello, my name is {sys.argv[1]}")
    elif len(argv_list) < 2:
        print("please add your name before hit Enter key")
    else:
        print("too many arguments, please just input one")


# version 3，及时退出
def sys_arg_version_3():
    argv_list = sys.argv
    if len(argv_list) > 2:
        sys.exit("too many arguments, please just input one")
    elif len(argv_list) < 2:
        sys.exit("please add your name before hit Enter key")

    # 主要目的应该和 exception 处理区分开来
    print(f"hello, my name is {sys.argv[1]}")


# version 4，遍历输出
def sys_arg_version_4():
    argv_list = sys.argv

    # argv_list 最少有一个 element：*.py
    if len(argv_list) <= 1:
        sys.exit("please add your name before hit Enter key")

    """
        argv_list 的第一个元素是 *.py，并不是需要 print 的 name data ，
            所以需要对 argv_list 进行 slice 操作

    """
    for arg in argv_list[1:10]:
        print(f"hello, my name is {arg}")


main()
