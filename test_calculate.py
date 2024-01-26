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
        5. with pytest.raises(error_type):
            f(n)
           在执行f(n)时，预期某种特定类型的错误，这样可以确保所有会发生的 error 都已经被考虑到且已经用 try、catch 处理到位了




"""
import pytest

import sys

from calculate import square

def main():
    test_square_positive()
    test_square_negative()
    test_square_zero()
    test_square_input()

def test_square_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_square_zero():
    assert square(0) == 0

def test_square_input():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()



