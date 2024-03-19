# 可以将类视为：有关如何创建实例的说明
# 类中的函数称为：方法
# 给属性和方法指定合适的描述性名称


class Dog:  # 在 Python 中，首字母大写的名称指的是：类
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):  # 使用类来创建实例时，会自动调用这个方法
        """初始化属性 name 和 age"""
        # 与实例相关的方法，会自动传入实参 self（指向实例本身的引用），让实例访问类的属性和方法
        print(type(self))  # <class '__main__.Dog'>
        # 以 self 为前缀的变量可供类中的所有方法使用，可以通过类的任意实例来访问
        self.name = name  # 使用 . 来设置实例的属性
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog("旺财", 1)
print(my_dog)  # <__main__.Dog object at 0x10ed9b110>
print(f"My dog's name is {my_dog.name}")  # 使用 . 来访问实例的属性
print(f"My dog's age is {my_dog.age}")
my_dog.sit()  # instance_name.function_name()
my_dog.roll_over()
