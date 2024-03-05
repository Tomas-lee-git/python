x = 123


def main():
    # name = input("What's your name? ")
    hello()


"""
    NameError: name 'name' is not defined

    问题出在 scope：
        variable only existing in the context which you defined
        如果一个变量在函数中被定义，如 name ，那它只能在这个函数中被引用，除非作为参数复制到其它函数中
        但如果一个变量是在全局被定义的，如 x ，那它在任何位置都可以被引用
"""


def hello():
    print(f"hello, {x}")


main()
