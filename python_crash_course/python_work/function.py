"""
    函数编写指南；
        1. 给函数指定描述性名称，且只使用小写字母和下划线（模块命名也应该遵循相同约定）；
        2. 每个函数都应包含简述其功能的注释：
            a. 注释应该紧跟在函数定义的下一行；
            b. 需要采用文档字符串的格式，也就是三对引号；
            c. 光标放在上面就能看到函数的介绍了；
        3. 给函数的形参指定默认值时，等号两边不要有空格；
        4. 调用函数时，关键字实参的等号两边不要有空格；
        5. PEP8建议代码行的长度不要超过 79 个字符，如果因为形参过多导致函数定义的长度超过了：
            a. 在函数定义中输入左括号后按回车键；
            c. 在下一行连按两次 table 键（这样就能与函数体区分开来）；
        6. 如果程序或模块中包含多个函数，每个函数需要用两个空格区分开来；
        7. 所有的 import 语都要放在文件的开头；
        8. 上述的格式方面的要求，都可以用python library: black 自动实现，平时注意一下就好；
"""


def greet_user(username):  # username 形参（parameter）
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")


greet_user("Tomas")  # "Tomas" 实参（argument）


def describe_pet(pet_name, animal_type="dog"):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("harry", "hamster")
describe_pet("Willie", "dog")  # position argument, notice order

describe_pet(pet_name="Willie", animal_type="dog")  # keyword argument, notice name

describe_pet("Willie")
describe_pet("Kitty", "cat")


# return value
def get_full_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


people = get_full_name("tomas", "lee")
print(people)

people = get_full_name("tomas", "lee", "middle")
print(people)

people = get_full_name("tomas", "lee", middle_name="middle")
print(people)


# *，代表任意数量的"位置实参“，收集在元组中 () => ('jack', 'tom', 'bill')
# **，代表任意数量的”关键字实参“，收集在对象中 {} => {'gender': 'female', 'age': '30'}
def hello(a, *others, **infos):
    print(others)
    # print(infos)
    for name in others:
        print(f"hello, {name}")
    for key, value in infos.items():
        print(f"key is {key}, value is { value}")


hello("jack")
hello("jack", "tom", "bill")
hello("def", gender="female", age="30")
