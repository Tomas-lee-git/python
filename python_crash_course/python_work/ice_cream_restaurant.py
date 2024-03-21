"""继承了 Restaurant 类的冰淇淋摊的类"""
from restaurant import Restaurant as RT

class IceCreamStand(RT):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def describe_iceCream_flavors(self):
        print("We have those flavors: ")
        for flavor in self.flavors:
            print(f"\t{flavor}")