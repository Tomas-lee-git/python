def display():
    print("Learn Python function")

# display()

def favorite_book(title):
    print(f"My favorite book is {title}.")
    
# favorite_book("Alice in Wonderland")

def make_shirt(word = "Hello, World!", size = 170):
    print(f"Your shirt's size is {size}, and the slogan is '{word}'.")
    
# make_shirt() # Your shirt's size is 170, and the slogan is 'Hello,World!'.
# make_shirt("hey", 180) # Your shirt's size is 180, and the slogan is 'hey'.
# make_shirt(None, 170) # Your shirt's size is 170, and the slogan is 'None'.
# make_shirt(size = 170) # Your shirt's size is 170, and the slogan is 'Hello, World!'.
# make_shirt("ha") # Your shirt's size is 170, and the slogan is 'ha'.
# make_shirt(word = "ha") # Your shirt's size is 170, and the slogan is 'ha'.

def sandwich(*toppings):
    """概述要制作的三明治"""
    message = "Your sandwich include: "
    for topping in toppings:
        comma_symbol = "." if toppings[-1] == topping else ", "
        message += f"{topping}{comma_symbol}"
    print(message)
    
# sandwich("mushroom")
# sandwich("mushroom", "green peppers")
# sandwich("mushroom", "green peppers", "extra cheese")

def user_profile(first, last, middle = "",  **profiles):
    """generate user profile dict"""
    profiles["first_name"] = first.title()
    profiles["last_name"] = last.title()
    if middle:
        profiles["middle_name"] = middle.title()
        profiles["full_name"] = f"{first.title()} {middle.title()} {last.title()}"
    else:
        profiles["full_name"] = f"{first.title()} {last.title()}"
    
    return profiles

profile = user_profile("tomas", "lee", age="30", gender="male", habits="motor, read book")
print(profile)

profile = user_profile("tomas", "lee", "ale", age="30", gender="male", habits="motor, read book")
print(profile)
        
    

