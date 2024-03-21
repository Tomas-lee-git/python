"""一个继承自 User 类的关于管理员的类"""
from user import User
from privilege import Privileges as PL

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, country, privileges):
        super().__init__(first_name, last_name, age, gender, country)
        self.privileges = PL(privileges)