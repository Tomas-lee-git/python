# car = input("What's car are you want to rent? ")
# print(f"Let me see if I can find you a {car.title()}")

# number = int(input("How many of you are coming for dinner? "))
# if number > 8:
#     print("Sorry, there are no empty tables.")
# else:
#     print("There are empty tables.")

number = int(input("Enter a number, I will tell you if it's a multiple of 10: "))
if number % 10 == 0:
    message = "Yes, it is a multiple of 10"
else:
    message = "No, it is not a multiple of 10"
print(message)
