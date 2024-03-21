"""继承自 Car 类的电车的类，使用了 Battery 类的组合"""
from car import Car # 导入类和导入函数的方式一致
from battery import Battery

# inheritance 类的继承
class ElectricCar(Car):
    """通过继承Car父类来定义电车子类"""

    def __init__(self, make, model, year, battery=40):
        # 把子类初始化实例时获得的属性值给到父类
        super().__init__(make, model, year)  # 注意super().__init__()中没有 self
        self.battery = Battery(battery)
