# exceptions: 例外情况，也就是 bug: SyntaxError、ValueError、NameError……

"""
    try: 
        do something
    except [ErrorType]:
        1. 可以catch error；

        2. 也可以使用 pass 直接静静地挂掉，不让错误暴露在用户面前；
    else:
        如果没有报错，一切正常的情况下，执行这里的代码

    路径一：try => except 进行错误处理
    路径二：try => else 进入后续流程
"""

"""    
0. SyntaxError: unterminated string literal (detected at line 6)
            未终止的字符串，也就是字符串没有的""没有正确的闭合

    SyntaxError must be fixed

"""
# print(hello")


""" 
1. ValueError: invalid literal for int() with base 10: 'cat'

    defensively，设置防御性的代码来避免

    try:
        do something
        try 只应该包含那些有可能会出错的代码，这样会更便于定位错误的位置
    except ValueError: 
        handle error
        可以用"ValueError" 来指定错误类型；
        也可以忽略指定错误类型，将会处理所有的错误类型；
        ❕但最好还是弄清楚会出现什么样的错误，这样才能写出针对性地 handle 逻辑

   try:
        x = int(input("What's x ? "))
        print(f"x is {x}")
    except ValueError:
        print("please input an integer number")
"""

"""
2. NameError: name 'x' is not defined

    try:
        x = int(input("What's x ? "))
    except ValueError:
        print("please input an integer number")
    
    # 如果用户输入了 stir 如 cat ，那在 int()函数调用这一步就出错了，
    # 在这种情况下 x = ？ 的定义和赋值操作就没有实现，
    # 所以 x 是 not defined；

    print(f"x is {x}")

"""
# 不断提示，直到用户输入数字，然后打印出来

# version 1：递归实现
def input_and_print_int():
    try:
        x = int(input("What's x ? "))
    except ValueError:
        print("please input an integer number")
        input_and_print_int()
    else:
        print(f"x is {x}")

# input_and_print_int()

# version 2：while:True 实现
# while True:
#     try:
#         x = int(input("What's x ? "))
#     except ValueError:
#         print("please input an integer number")
#         continue
#     else:
#         print(f"x is {x}")
#         break

# version 3： while: True 实现优化
# while True:
#     try:
#         x = int(input("What's x ? "))
#         break
#     except ValueError:
#         print("please input an integer number")

# print(f"x is {x}")

def get_int_1(): # 7行
    while True:
        try:
            x = int(input("What's x ? "))
        except ValueError:
            print("please input an integer number")
        else:
            # break
            # return 可以替代 break 来跳出 loop 
            return x

# print(f"x is {get_int_1()}")

def get_int_2(): # 6行
    while True:
        try:
            x = int(input("What's x ? "))
            return x
        except ValueError:
            print("please input an integer number")

# print(f"x is {get_int_2()}")

def get_int_3():  # 5行
    while True:
        try:
            return int(input("What's x ? "))
        except ValueError:
            print("please input an integer number")

# 心得：❕优化是没有终止的，最重要的是先写出来可用的代码，优化值得投入，但终究只是锦上添花