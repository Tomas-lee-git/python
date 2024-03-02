"""
    1. argparse:
        1). docs: docs.python.org/library/argparse.html;
        2). python built-in module to analysis of command line arguments;
        
"""
from sys import argv

def print_meow(n):
    print("meow\n" * n, end = "")

if len(argv) == 1:
    print("meow")
elif len(argv) == 2:
    n = int(argv[1])
    print_meow(n)
elif len(argv) == 3 and argv[1] == "-n":
    n = int(argv[2])
    print_meow(n)
else:
    print("usage: meow_simple.py")