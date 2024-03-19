def greet_user(username): # username 形参（parameter）
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")
    
greet_user("Tomas") # "Tomas" 实参（argument）

def describe_pet(pet_name, animal_type = "dog"):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet("harry", "hamster")
describe_pet("Willie", "dog" ) # position argument, notice order

describe_pet(pet_name="Willie", animal_type="dog") # keyword argument, notice name

describe_pet("Willie")
describe_pet("Kitty", "cat")

# return value
def get_full_name(first_name, last_name, middle_name = ""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

people = get_full_name("tomas", "lee")
print(people)

people = get_full_name("tomas", "lee", "middle")
print(people)

people = get_full_name("tomas", "lee",  middle_name = "middle" )
print(people)

# *，代表任意数量的"位置实参“，收集在元组中 () => ('jack', 'tom', 'bill')
# **，代表任意数量的”关键字实参“，收集在对象中 {} => {'gender': 'female', 'age': '30'}
def hello(a, *others, **infos):
    print(others)
    # print(infos)
    for name in others:
        print(f"hello, {name}")
    for key, value in infos.items():
        print(f"key is {key}, value is { value}")

hello("jack")
hello("jack", "tom", "bill")
hello("def", gender="female", age="30")

