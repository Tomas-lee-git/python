"""一个用来表示汽车的类""" # 模块级文档字符串，对模块内容作简要的描述
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

    def fill_gas_tank(self):
        """加油哦"""
        print("95# 加满，谢谢！")