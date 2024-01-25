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
    
    三、pytest: https://docs.pytest.org/en/latest/
        1. third-party unit testing: pip3 install pytest;
        2. handled the try、except、print all of standardization of actually running these tests;
        3. execute "pytest", the implementation will be automatically added: try, except, print, etc.;
        4. unit tests are typically tests for functions that you have written;




"""

import sys

from calculate import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

if __name__ == "__main__":
    main()



