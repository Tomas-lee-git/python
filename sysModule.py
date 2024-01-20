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
"""

import sys

def main():
    # sys_arg_version_1()
    # sys_arg_version_2()
    sys_arg_version_3()

#　版本1，处理报错
def sys_arg_version_1():
    try:
        print(f"hello, my name is {sys.argv[1]}")

    except IndexError:
        print("please add your name before hit Enter key")


# 版本2，灵活应对
def sys_arg_version_2():
    argv_list = sys.argv
    if len(argv_list) == 2:
        print(f"hello, my name is {sys.argv[1]}")
    elif len(argv_list) < 2:
        print("please add your name before hit Enter key")
    else:
        print("too many arguments, please just input one")

# 版本3，及时退出
def sys_arg_version_3():
    argv_list = sys.argv
    if len(argv_list) > 2:
        sys.exit("too many arguments, please just input one")
    elif len(argv_list) < 2:
        sys.exit("please add your name before hit Enter key")

    # 主要目的应该和 exception 处理区分开来
    print(f"hello, my name is {sys.argv[1]}")

main()