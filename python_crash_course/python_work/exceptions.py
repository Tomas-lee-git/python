# Python 使用称为异常（exception）的特殊对象来管理程序执行期间发生的错误。
# 每当发生 Python 不知所错的错误时，他都会创建一个异常对象。
# 异常需要使用 try-catch 代码块处理。


"""
    如何阅读 traceback：
        1. 先看最后一行，看错误类型；
        2. 从头开始，看错误发生的文件、行数、代码内容；
        3. 除了末尾错误类型、开头错误发生的位置，
            通常不需要详细阅读和理解 traceback 暴露出的详细内容；
"""

from word_count import count_words as cw

# from pathlib import Path

# n = print("Give me two numbers, and I will divide them.")
# print("Enter 'q' to quit.")

# while True:
while False:
    first_number = input("First number: ")
    if first_number == "q":
        print("Programming quits successfully.")
        break
    second_number = input("Second number: ")
    if second_number == "q":
        print("Programming quits successfully.")
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:  # ZeroDivisionError: division by zero
        print("You can't divide by zero!")
    else:
        print(f"{first_number} / {second_number} = {answer}")

# path = Path("./txt_files/alice.txt")
# path = Path("./txt_files/guest.txt")

# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
# contents = path.read_text(encoding="utf-8")

file_names = [
    "alice.txt",
    "moby_dick.txt",
    "siddhartha.txt",
    "little_women.txt",
    "old_homeless.txt",
]
for file_name in file_names:
    cw(f"./txt_files/{file_name}")
