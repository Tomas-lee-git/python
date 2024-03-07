"""
    1. try:
        1). try, exception, else, finally;
        2). finally will always be executed;
    
    2. Python ternary expressions:
        1). A if condition else B:
            i. if condition == True, expression select A;
            ii. if condition == False, expression select B;

"""

from sys import argv

DEFAULT_TIMES = 1
LEAST_ARGV_LENGTH = 2


def meow(n: int = DEFAULT_TIMES) -> str:
    try:
        return "meow\n" * n
    except ValueError:
        print("n must be an int number")
        return ""


def get_number():
    return int(argv[1] if len(argv) >= LEAST_ARGV_LENGTH else DEFAULT_TIMES)


while True:
    try:
        number: int = get_number()
    except ValueError:
        print("Number must be an int number")
        number: int = int(input("Please input number to continue: "))
        meows: str = meow(number)
        print(meows, end="")
        break
    else:
        meows: str = meow(number)
        print(meows, end="")
        break
