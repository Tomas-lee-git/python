"""
    1. argparse:
        1). docs: docs.python.org/library/argparse.html;
        2). python built-in module to analysis of command line arguments;
        3). argparse.ArgumentParser():
                all parameters should be passed as keyword arguments;
        4). parse.add_argument():
                define how a single command-line argument should be parsed;
        5). parse.parse_args():
            i. runs the parser and places the extracted data in a argparse.Namespace object;
            ii. can use dot to access argument value;
        
"""

# from sys import argv

# def print_meow(n):
#     print("meow\n" * n, end = "")

# if len(argv) == 1:
#     print("meow")
# elif len(argv) == 2:
#     n = int(argv[1])
#     print_meow(n)
# elif len(argv) == 3 and argv[1] == "-n":
#     n = int(argv[2])
#     print_meow(n)
# else:
#     print("usage: meow_simple.py")

import argparse

# common public code
parse = argparse.ArgumentParser(description="Meow like a cat")

# self code
parse.add_argument(  # how to parse argument
    "-n",  # argument's name
    type=int,  # specify argument's data type and convert it automatically
    # meow_cls_simple.py: error: argument -n: invalid int value: 's'
    default=99999999,  # argument's default value when it's without value
    help="specify how many times to print 'meow'",
)
# parse.add_argument("-d")
# parse.add_argument("-e")
# parse.add_argument("-f")

# common public code
args = parse.parse_args()

print(f"args is {args}")  # args is Namespace(n=3)
print(f"args.n is {args.n}")  # args.n is 3

for _ in range(args.n):
    print("meow")
