# 推荐做法：1. 引入整个模块，使用 . 来调用具体函数；2. 引入模块中的具体函数，直接调用；

import pizza  # import module_name, 可以使用整个模块中的所有函数

# module_name.function_name()
pizza.make_pizza(12, "pepperoni")
pizza.make_pizza(16, "mushroom", "green pepper", "extra cheese")

# from module_name import function_name, 引入模块中的特定函数
from pizza import make_pizza

make_pizza(8, "onion")

# 使用关键字 as 给函数指定别名，来避免引入函数名称过长或者与自己程序中的名称冲突
from pizza import make_pizza as mp  # 通用命名方式：function_name as fn

# mp 就是 make_pizza 的别名，
mp(6, "pineapple")

# 使用关键字 as 给模块指定别名，这样可以只关注描述性的函数名，而不用再关注模块名，让代码更简洁
import pizza as pz  # 通用命名方式：module_name as mn

pz.make_pizza(15, "meat", "tomato")

# 导入模块中的所有函数
from pizza import *  # 不建议使用，不知道引入了哪些函数，会导致本地程序中相同名称的函数被意外覆盖

make_pizza(24, "egg")
