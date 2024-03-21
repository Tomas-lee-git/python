# composition 组合
"""一个描述电车电池的属性和方法的类"""


class Battery:
    """把电车电池相关的属性和方法提出来做一个 Battery 类"""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电车容量的信息"""
        print(f"The car has a {self.battery_size}-kwh battery.")

    def fill_gas_tank(self):
        """电车不用加油"""
        print("起开！电车加个屁的油哦.")

    def range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        """给电动车充电"""
        if self.battery_size < 65:
            self.battery_size = 65
            print("充电完成！🔋")
