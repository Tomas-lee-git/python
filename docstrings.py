"""
    1. docstring:
        1). docs: peps.python.org/pep-0257;
        2). add comment inside a function, be function's first line code;
        3). use triple quotation;
        4). python has built into it certain tools and certain assumptions that:
            i. if it detects that there is a comment using triple quote;
            ii. it will assume that's indeed the documentation for that function;
            iii. python ecosystem has a lot of tools to: 
                a. analyze code automatically;
                b. extract all of these document strings;
                c. generate web pages or PDFs of documentation for own functions without manually;
"""
def meow(n: int) -> str:
    """ 
    Meow n times
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    try:
        return "meow\n" * n
    except ValueError:
        print("n must be an int number")
    
try:
    number: int = int(input("Number:"))
except ValueError:
    print("Number must be an int number")
else:
    meows: str = meow(number)
    print(meows, end = "")