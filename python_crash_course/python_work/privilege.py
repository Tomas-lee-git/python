"""一个关于管理员特权的类，被 Admin 类用来组合"""
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print("Admin has those privileges: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")