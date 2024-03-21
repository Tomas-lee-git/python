from random import choice
lucky_number = 996
ticket_number = list(range(1, 999999))
n = 0

while True:
    if choice(ticket_number) == lucky_number:
        print(f"执行了{n}次循环才中了大奖！🤔")
        break
    else:
        print("又尼玛成韭菜了！")
        n += 1