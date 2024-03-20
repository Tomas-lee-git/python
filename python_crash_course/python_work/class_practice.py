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
            
        
        
chinese_food = Restaurant("中华料理店", "chinese food")

japanese_food = Restaurant("大阪の御飯", "japanese food")

# chinese_food.describe_restaurant()
# chinese_food.open_restaurant()

# japanese_food.describe_restaurant()
# japanese_food.open_restaurant()

# chinese_food.print_number_severed()
# chinese_food.number_severed = 20
# chinese_food.print_number_severed()

# chinese_food.set_number_severed(-50) # Are you kidding me?
# chinese_food.set_number_severed(50)
# chinese_food.print_number_severed()

# chinese_food.increment_number_served(-500) # Are you kidding me?
# chinese_food.increment_number_served(50)
# chinese_food.print_number_severed()


class User:
    """用户信息相关"""
    def __init__(self, first_name, last_name, age, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.country = country
        self.login_attempts = 0
        self.name = f"{self.first_name} {self.last_name}".title()
        
    def describe_user(self):
        message = f"{self.name} is {self.gender}, {self.age} years old, from {self.country}."
        print(message)
        
    def greet_user(self):
        print(f"hello, {self.name}!")
        
    def print_login_attempts(self):
        print(f"{self.name}'s login attempts is {self.login_attempts}.")

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempt(self):
        self.login_attempts = 0
        
lee = User("tomas", "lee", 30, "male", "China")
# lee.describe_user()
# lee.greet_user()

lily = User("ken", "lily", 20, "female", "USA")
# lily.describe_user()
# lily.greet_user()

lee.print_login_attempts()

lee.increment_login_attempt()
lee.increment_login_attempt()
lee.increment_login_attempt()
lee.print_login_attempts()

lee.reset_login_attempt()
lee.print_login_attempts()