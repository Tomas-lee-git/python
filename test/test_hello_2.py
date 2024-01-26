"""
    一、 question: how to test input()、print()?
        answer：
            1. python self function don't need to test😂;
            2. "side effect" will make logic can't to be test;
            3. def function should avoid "side effect" logic;
            4. if you are doing assert [==], you're looking for a [return value];
            5. tests should ideally be pretty simple and  pretty small;

    二、side effect（函数副作用）:
        在计算机科学中，side effect 指当调用函数时，除了返回可能的函数值之外，还对主调用函数产生附加的影响： 
            例如修改全局变量（函数外的变量），修改参数，向主调方的终端、管道输出字符或改变外部存储信息等。

    三、要想避免函数变得复杂，让函数具有“可测试性”，就要避免side effect，因为函数副作用完全不可预测；


"""
from hello_2 import hello

def test_hello_default(): # test default
    # print function will return None
    # assert hello("lee") == None
    assert hello() == "hello, world"

def test_hello_argument(): # test argument
    names = ["Lee","Tomas","Harry","Eric"]
    for name in names:  # use loop to test more cases
        assert hello(name) == f"hello, {name}"