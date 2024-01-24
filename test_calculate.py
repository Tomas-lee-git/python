"""
    python test convention:
        1. if you want to test a module: a, create a file named as test_a.py;
        2. if you want to test a function: b, create a function named as test_b;
        3. don't testing one thing but test serval and make sure cover case;

"""

import sys

from calculate import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print(f"Test failed: 2 squared should be 4, but is {square(2)}")

    if square(3) != 9:
        print(f"Test failed: 3 squared should be 9, but is {square(3)}")

if __name__ == "__main__":
    main()



