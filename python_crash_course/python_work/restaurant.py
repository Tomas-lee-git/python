"""一个关于餐馆的类"""
class Restaurant:
    """介绍餐馆特色和营业状况"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_severed = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} has {self.cuisine_type} foods.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is opening!")

    def print_number_severed(self):
        print(f"{self.number_severed} are eating!")
    
    def set_number_severed(self, number):
        if number >= 0:
            self.number_severed = number
        else:
            print("Are you kidding me?")
    
    def increment_number_served(self, number):
        new_number = self.number_severed + number
        if new_number >= 0:
            self.number_severed = new_number
        else:
            print("Are you kidding me?")