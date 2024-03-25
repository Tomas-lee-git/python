# 测试：核实一系列输入将得到预期的输出；
"""
    Python 中的包：
        1. Python 核心库即 Python 自带的标准库；
        2. 外部库即第三方包，指的是独立于 Python 核心的库，需要使用 pip 安装；
        3. 有些深受欢迎的第三方包最终会被纳入标准库，并从此随 Python 一起被安装，跟随 Python 语言同步演进；
        4. 独立的第三方包的更新频率往往更高；
"""
"""
    pip，安装第三方包：
        1. pip， 是 Python 提供的一款工具，用来安装第三方包，Python3 对应 pip3；
        2. 更新 pip3 的命令：pip3 install --upgrade pip ；
        3. 使用 pip 更新第三方包的命令： pip3 install --upgrade package_name；
"""


def get_formatted_name(first, second, middle=None):
    """接收名、姓、中间名，返回格式规范的姓名"""
    if middle:
        full_name = f"{first} {middle} {second}"
    else:
        full_name = f"{first} {second}"
    return full_name.title()
