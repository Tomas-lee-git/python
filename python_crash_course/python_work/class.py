# 可以将类视为：有关如何创建实例的说明
# 类中的函数称为：方法
# 给属性和方法指定合适的描述性名称


class Dog:  # 在 Python 中，首字母大写的名称指的是：类
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):  # 使用类来创建实例时，会自动调用这个方法
        """初始化属性 name 和 age"""
        # 与实例相关的方法，会自动传入实参 self（指向实例本身的引用），让实例访问类的属性和方法
        # print(type(self))  # <class '__main__.Dog'>
        # 以 self 为前缀的变量可供类中的所有方法使用，可以通过类的任意实例来访问
        self.name = name  # 使用 . 来设置实例的属性
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")

def check_dog_instance(instance):
    print(instance)  # <__main__.Dog object at 0x10ed9b110>
    print(f"My dog's name is {instance.name}")  # 使用 . 来访问实例的属性
    print(f"My dog's age is {instance.age}")
    instance.sit()  # instance_name.function_name()
    instance.roll_over()
    print("==========")

my_dog = Dog("旺财", 1)
# check_dog_instance(my_dog)

your_dog = Dog("欢欢", 6)
# check_dog_instance(your_dog)


class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def get_odometer_reading(self):
        """打印一条指出汽车里程的信息"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        # print(f"mileage is {mileage}")
        if mileage > self.odometer_reading: 
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")
        
    def increment_odometer(self, miles):
        """
        根据参数更新里程表读数
        禁止将里程表读数往回调
        """
        # print(f"miles is {miles}")
        if miles > 0: 
            self.odometer_reading += miles
        else:
            print("You can't roll back the odometer!")
    
my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.get_odometer_reading()

# 通过实例直接修改属性
my_new_car.odometer_reading = 2000
my_new_car.get_odometer_reading()

# 通过类中的方法， 传递参数，直接设置新的属性
# my_new_car.update_odometer(1000) # You can't roll back the odometer!
my_new_car.update_odometer(3000)
my_new_car.get_odometer_reading()

# 通过类中的方法，传递参数来让属性的值变化
# my_new_car.increment_odometer(-5000) # You can't roll back the odometer!
my_new_car.increment_odometer(5000)
my_new_car.get_odometer_reading()