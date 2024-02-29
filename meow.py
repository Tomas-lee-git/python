"""
    1. constant:
        1). Python doesn't actually make variables constant;
        2). it's indeed a convention in Python and some other languages at least capitalize variables name;
        3). there is nothing preventing programer from changing constant variables's value;

    2. range(n)函数:
        1). n: 数字 n，指定 list 的长度为0，内容为：0-n，不包括 n;
        2). return: list [0, ..., n-1]
    
    3._:
        1). in python, if the defined parameters don't need to be used directly, it's customary to use _ to represent them;
        2). if used in the future, replace it with a more specific variable name;
        3). and _ itself can also get the value correctly;

"""
MEOWS = 3
for _ in range(MEOWS):
    print("meow")