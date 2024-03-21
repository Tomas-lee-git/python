"""一个关于用户信息和行为的类"""
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