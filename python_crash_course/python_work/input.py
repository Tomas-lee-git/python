# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nhello, {name.title()}")

# input 中的提示语，可以使用 \n 进行换行
# prompt = "If you share your name, we can personalize the message you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"{name}")

# input() return str
# number = input("What's your favorite number? ")
# type is <class 'str'>
# print(f"Your favorite number is {number}, type is {type(number)}")
# n = int(number)
# type is <class 'int'>
# print(f"Your favorite number is {n}, type is {type(n)}")

# n % 2 == 0, check number if it's even or odd
number = int(input("Enter a number, and I will tell you if it's even or odd: "))
message = "Odd" if number % 2 else "Even"
# message = "Even" if number % 2  == 0 else "Odd"
print(f"You entered {number} is {message}")

