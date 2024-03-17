# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# repeat user input until user input 'quit'
prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the prompt. "
message = ""
active = True

# flag
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#         print("Ok, input program is quitted.")
#     else:
#         print(f"{message}\n")

# break statement
# while True:
#     message = input(prompt)
#     if message == "quit":
#         print("Ok, input program is quitted.")
#         break # 不执行循环中剩余的代码，退出整个循环(break)
#     else:
#         print(f"{message}\n")

# continue statement
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue # 不执行循环中剩余的代码，从头开始继续(continue)循环
#     print(current_number)

# n = 1
# while n <= 5:
#     print(n)
#     n += 1

# n = 1
# while True:
#     if n > 5:
#         break
#     print(n)
#     n += 1

# 在列表中移动元素
unconfirmed_users = ["tom", "jerry", "doge", "bird", "kitty"]
confirmed_users = ["bob", "ford"]

# 不应该在 for 循环中修改列表，否则将导致 Python 难以跟踪其中的元素
# Python 中 bool 值为 False：'', "", 0, None, False, (), [], {}
# while unconfirmed_users:
#     user = unconfirmed_users.pop()
#     print(f"Verifying user: {user.title()}")
#     confirmed_users.append(user)

# print("\nThe follow user is been confirmed: ")
# for user in confirmed_users:
#     print(f"{user.title()}")

# pets = ["cat", "dog", "goldfish", "rabbit", "cat", "dog", "cat", "goldfish"]
# # remove all 'cat'
# print(pets)
# while "cat" in pets:
#     pets.remove("cat")

# print(pets)

responses = {}
while True:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("\nWould you like to let another person respond? (yes/no)")
    if repeat.lower() == "no":
        break
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
