"""
    match, 也就是 js 中的 switch；
    没有 break；
    没有 default，使用 case _ 来表示" catch-all "；
    用 | 来连接“殊途同归”中的“殊途”；
"""

name = input("What's your name? ")

"""
    version 1

    if name == "Tom":
        print("It's a cat")
    elif name == "老皮":
        print("It's a cat")
    elif name == "蓝猫":
        print("It's a cat")
    elif name == "Jimmy":
        print("It's a mouse")
    else:
        print("What ?")
"""

"""
version 2
    if name == "Tom" or name == "老皮" or name == "蓝猫":
        print("It's a cat")
    elif name == "Jimmy":
        print("It's a mouse")
    else:
        print("What ?")
"""

"""
 version 3
    match name:
        case "Tom":
            print("It's a cat")
        case "老皮":
            print("It's a cat")
        case "蓝猫":
            print("It's a cat")
        case "Jimmy":
            print("It's a mouse")
        case _:
            print("What ?")
"""

# version 4

match name:
    case "Tom" | "老皮" | "蓝猫":
        print("It's a cat")
    case "Jimmy":
        print("It's a mouse")
    case _:
        print("What ?")
