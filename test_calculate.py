"""
    一、python test convention:
        1. if you want to test a module: a, create a file named as test_a.py;
        2. if you want to test a function: b, create a function named as test_b;
        3. don't testing one thing but test serval and make sure cover case;

    二、assert:
        1. the key word to sort of boldly claim that something is true;
        2. if something is not true, will see some kind of error on the screen;
        3. AssertionError:
            display Traceback, detail but not friendly to read
            use except to enhance readable


"""

import sys

from calculate import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared not equal 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared not equal 9")

if __name__ == "__main__":
    main()



