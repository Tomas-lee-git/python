"""
    pip3 / pip command:
        --help / -h: show help;
        --list: list installed packages;
        --show packageName: show information about installed package;

    __name__:
        this is a variable automatically set by python:
            if you execute: "python3 a.py", in a.py,  __name__ == "__main__";
            if a.py is imported by other files such as b.py, in a.py, __name__ == "a";
        简单地理解：
            在内部 __name__ 是自家小名：__main__；
            出门在外，就是文件名这个大名喽；
"""

def main():
    hello("lee")
    goodbye("lee")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# print(f"__name__ is {__name__}")

if __name__ == "__main__":
    main()