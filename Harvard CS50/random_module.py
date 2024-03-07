"""
    import:
        用法一：import random: 引入整个 random module；
        用法二：from random import choice，引入 module 中的 specify function；

    random:
        choice(seq): return a value from list；
        randint(a, b): return an int number from a to b, include a and b；
        shuffle：❕ shuffle will change the parameter, and no return value(None)；
        
"""


def main():
    # import_whole_module()
    import_specify_function_from_module()


# 用法一
def import_whole_module():
    import random

    for _ in range(5):
        coin = random.choice(["heads", "tails"])
        print(f"methods 1:{coin}")
        # print(random)
        # <module 'random' from '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/random.py'>


# 用法二
def import_specify_function_from_module():
    # from random import choice

    # for _ in range(5):
    #     coin = choice(["heads","tails"])
    #     print(f"methods 2:{coin}")
    # print(choice)
    # <bound method Random.choice of <random.Random object at 0x7f9c8f80ce20>>

    """
    import randint from random
        SyntaxError: Did you mean to use 'from ... import ...' instead?
        ❕注意顺序：先 from 再 import 😂
    """

    # from random import randint

    # for _ in range(30):
    #     number = randint(-12, 10)
    #     print(number)

    from random import shuffle

    cards = ["jack", "queen", "king", "4", "pink"]

    for _ in range(10):
        card = shuffle(cards)
        # ❕ shuffle will change the parameter, and no return value
        print(cards)
        # print(card) None


main()
