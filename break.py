
"""
    recursion，递归：
        执行过程中，在特定情况下，需要从头开始重复整段逻辑；
        在这种需要“从下到上”回到开始位置的地方，用到的方法就是“递归”；
        遇到这种情况时，最好画一个流程图，协助搞明白流程是怎样的；
        ⚠️：递归写错了，容易陷入死循环昂🐶

    while: 使用 while 无限循环，特定情况下使用 break 结束无限循环
        while True:
            condition1:
                continue
            condition2:
                break
"""

"""
    要求：
        当用户输入 正整数时，输出；
        当用户输入负整数和 0 时，提醒用户重新输入；
"""

"""
     main 里面放置所有需要执行的函数：
        1. 这样可以更加清晰明确地控制流程；
        2. 把main()放在最后，可以避免“函数总需要被放置在它的调用位置之前的限制”；
"""
def main():
    printWow1()
    printWow2()
    printWow3()


# 方案1 用递归实现
def printWow1():
    n = askUser()

    if n <= 0:
        printWow1()
    else:
        wow(n, 1)


#方案2 用 while 实现

"""
    思路和递归是相反的：
        递归是：符合条件时进入，重复执行；
        while是：默认重复执行，直到符合条件时退出；
"""
def printWow2():
    flag = True
    while flag:
        n = askUser()
        if n > 0:
            flag = False
            wow(n, 2)

# 方案3，方案2的优化版本，使用自带的 break 来替代自己手动控制的 flag ，从而跳出循环

def printWow3():
    while True:
        n = askUser()
        if n > 0:
            break

    wow(n, 3)

# 抽取多次用到的逻辑，写成函数来复用
def wow(n, flag):
    for _ in range(n):
            print(f"Wow{flag}")
            
# 抽取多次用到的逻辑，写成函数来复用
def askUser():
    return int(input("What's n? （只能输入正整数嗷，不然让你重新输入😄 ）\n"))

main()