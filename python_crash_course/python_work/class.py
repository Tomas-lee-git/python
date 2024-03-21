"""
    类的编程风格：
        1. 类名应该采用大驼峰命名法，每个单词的首字母大写，并且不使用下划线；
        2. 实例和模块名应该采用全小写格式，并在单词之间加上下划线；
        3. 对于每个类，都应在类定义后面紧跟一个文档字符串，简要的描述类的功能；
        4. 可以使用空行来组织代码：
            4.1 在类中使用一个空行来分隔方法；
            4.2 在模块中使用两个空行来分隔类；
        5. 先导入标准库中的模块，添加一个空行，再导入自己编写的模块；
"""

# 可以将类视为：有关如何创建实例的说明
# 类中的函数称为：方法
# 给属性和方法指定合适的描述性名称

from random import randint, choice  # 引入 Python 标准库

from dog import Dog, check_dog_instance  # 导入类和导入函数的方式一致
from car import Car  # 导入类和导入函数的方式一致
from electric_car import ElectricCar as EC  # 注意，如果使用了别名，那原名称就不能使用了

my_dog = Dog("旺财", 1)
check_dog_instance(my_dog)

your_dog = Dog("欢欢", 6)
# check_dog_instance(your_dog)

my_new_car = Car("audi", "a4", 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.get_odometer_reading()

# 通过实例直接修改属性
my_new_car.odometer_reading = 2000
# my_new_car.get_odometer_reading()

# 通过类中的方法， 传递参数，直接设置新的属性
# my_new_car.update_odometer(1000) # You can't roll back the odometer!
# my_new_car.update_odometer(3000)
# my_new_car.get_odometer_reading()

# 通过类中的方法，传递参数来让属性的值变化
# my_new_car.increment_odometer(-5000) # You can't roll back the odometer!
# my_new_car.increment_odometer(5000)
# my_new_car.get_odometer_reading()

my_tesla = EC("tesla", "model3", 2024, 65)
print(my_tesla.get_descriptive_name())
# my_tesla.get_odometer_reading()
# my_tesla.describe_battery()
my_tesla.battery.describe_battery()

# 在子类中定义同名方法，通过覆盖父类方法来重写自己的方法
# my_new_car.fill_gas_tank() # parent Class method
# my_tesla.fill_gas_tank() # child Class method
# my_tesla.battery.fill_gas_tank() # child Class method

my_tesla.battery.range()

print("===============")
my_tesla_2 = EC("tesla", "model666", 2024)
print(my_tesla_2.get_descriptive_name())
my_tesla_2.battery.describe_battery()
my_tesla_2.battery.range()
my_tesla_2.battery.upgrade_battery()
my_tesla_2.battery.describe_battery()
my_tesla_2.battery.range()

print("==== Python 标准库 ====")
print(randint(1, 20))  # 随机返回 start 和 end之间的一个整数，包含 a 和 b
print(choice([1, 2, 3, 4, 5]))  # 随机返回 list 或 tuple 中的一个元素
print(choice((1, 2, 3, 4, 5)))
