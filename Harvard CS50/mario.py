def main():
    print_columns(3, "#")
    print_row(4, "?")
    print_square(3, "*")


# def 的函数，不改变 name、parameters、return，只改变它内部的实现，不会影响之前的调用
def print_columns(height, content):
    print(f"{content}\n" * height, end="")


def print_row(width, content):
    print(content * width)


def print_square(size, content):
    # print each row in square
    for _ in range(size):
        # for j in range(size):
        #     print(content, end="")
        # print()

        # print each column in square
        print(content * size)


main()
