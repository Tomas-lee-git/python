class Employee:
    """员工姓名和收入的类"""
    def __init__(self, first_name, last_name, salary):
        """实例化 Employee 类并添加姓名和收入属性"""
        name = f"{first_name} {last_name}".title()
        self.name = name
        self.salary = salary
    
    def give_raise(self, number = 0):
        """薪水加加加，要加最少就加个30%"""
        if number:
            self.salary += number
        else:
            self.salary = self.salary * 1.3
        
    def double_up(self):
        """薪水翻倍爽翻了"""
        self.salary = self.salary * 2
    
    