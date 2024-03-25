"""
    使用 pytest 编写测试用例的要求及规范：
        1. 测试文件的名称必须以 test_ 开头；
        2. 测试函数的名称必须以 test_ 开头，并且准确、详细地描述测试行为的目的；
        3. 使用 assert 关键字来设置一个断言，断言（assertion）就是声称满足特定的条件；
        4. 典型的测试方法是比较“函数运行结果”和“预期值”；
        5. 不需要自己调用测试函数，而是由 pytest 查找并运行它们，生成一份测试报告；
        6. 测试未通过：
            6.1 测试未通过意味着编写的新代码有错，在测试未通过时，不要修改测试；
            6.2 应该检查导致测试不能通过的代码，检查对函数所做的修改，找出不符合预期的地方；
            6.3 按预期修复更改，使它能够通过测试；
            6.4 重新运行测试用例，重复上面的过程，直到所有的测试用例都通过测试；
"""

"""
    执行 pytest 命令：
        1. 切换到这个测试文件所在的文件夹；
        2. pytest 会查找所有以 test_ 开头所标识的测试文件；
        3. pytest 会运行所有测试文件中，以 test_ 开头的单元测试；
        4. pytest 会生成一份测试报告：
            4.1 里面用绿色内容及绿色的 . ，表示通过的测试用例；
            4.2 用红色内容及红色的 F ，表示没有通过的测试用例；
"""

"""
    如何将形参设置为可选的：
        1. 把这个形参移到末尾；
        2. 给它一个 符合预期类型，但bool 为 False 的默认值（"",0,{},(),[],None)；
        3. 在函数内部对这个形参用 if 进行判断，根据是否存在，进行不同的处理；
"""

from name_function import get_formatted_name


def test_first_last_name():
    """能够正确处理像 Tomas Lee 这样的姓名吗？"""
    formatted_name = get_formatted_name("tomas", "lee")
    assert formatted_name == "Tomas Lee"


def test_first_last_middle_name():
    """能够正确处理像 Tomas A Lee 这样的姓名吗？"""
    formatted_name = get_formatted_name("tomas", "lee", "A")
    assert formatted_name == "Tomas A Lee"
