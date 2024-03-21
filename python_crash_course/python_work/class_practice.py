from restaurant import Restaurant as RT
from ice_cream_restaurant import IceCreamStand as ICS
from user import User
from admin import Admin

chinese_food = RT("中华料理店", "chinese food")
japanese_food = RT("大阪の御飯", "japanese food")

chinese_food.describe_restaurant()
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

ice = ICS("cold land", "iceCream", ["blueberry", "banana", "strawberry"])

ice.describe_restaurant()
# ice.describe_iceCream_flavors()

lee = User("tomas", "lee", 30, "male", "China")
lee.describe_user()
# lee.greet_user()

lily = User("ken", "lily", 20, "female", "USA")
# lily.describe_user()
# lily.greet_user()

# lee.print_login_attempts()

# lee.increment_login_attempt()
# lee.increment_login_attempt()
# lee.increment_login_attempt()
# lee.print_login_attempts()

# lee.reset_login_attempt()
# lee.print_login_attempts()

privileges = ["can add list", "can delete list", "can ban user"]
admin_lee = Admin("tom", "aden", 40, "female", "Japan", privileges)

admin_lee.describe_user()
# admin_lee.show_privileges()
admin_lee.privileges.show_privileges()  # 把管理员特权部分提取为 Privileges 类，进行组合
