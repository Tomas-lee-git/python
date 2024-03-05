"""
    1. type hint:
        1). Python is a dynamically typed language;
        2). can use type hint to hint data type:
            i. docs: https://docs.python.org/3/library/typing.html;
    2. mypy:
        1). check variable and parameter type, function's return type;
        2). docs: mypy.readthedocs.io;
        3). pip3 install mypy;
        4). add type hint with "variable : int(data type)" or "def fn(n: int) -> str:"
        5). run "mypy file.py", will return:
            i.  ✅ Success: no issues found in 1 source file;
            ii. ❌ type_hint.py:26: error: Argument 1 to "meow" has incompatible type "str"; expected "int"  [arg-type]
                    Found 1 error in 1 file (checked 1 source file) ;
            iii. ❌ type_hint.py:27: error: Missing return statement  [return];
            iiii. ❌ type_hint.py:32: error: Incompatible return value type (got "int", expected "str")  [return-value];
        6). --check-untyped-defs:
            i.  By default the bodies of untyped functions are not checked, consider using --check-untyped-defs;
            ii. run " mypy file.py --check-untyped-defs ";
        7). mypy only can check data types and return types through type hints, it can't check automatically;
            
    
    3. input("alert message"): 
        1). input("alert message") function will return str type data;
        2). if need int, need use int() to convert it data type, otherwise:
            TypeError: 'str' object cannot be interpreted as an integer
        
    4. None:
        1). if a function fn is not return value, fn() == None is True;

    5. str:
        1). str + str => long str concatenated together;
        2). str * number => long str that is a multiple of number str concatenated together;
"""


def main():
    # number: int =  int(input("Number:"))
    # meow(number)
    ...


def meow(n: int) -> str:
    # meows = ""
    # for _ in range(n):
    #     meows += "meow "
    # return meows

    # return "meow " * n

    return "meow\n" * n


number: int = int(input("Number:"))
meows: str = meow(number)
print(meows, end="")


if __name__ == "__main__":
    main()
