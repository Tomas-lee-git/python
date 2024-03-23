# 路径（path）指的是文件或文件夹在系统中的准确位置
# 处理特定功能的模块通常称为库（library），pathlib 就是 path library，专门处理文件和目录
# 方法链式调用（method chaining）
"""
    文件路径：
        1. 绝对路径，在计算机中的准确位置，以系统的根文件夹为起点：
            "/home/eric/python_crash_course/python_work/txt_files/pi_digits.txt"
        2. 相对路径：相对于当前程序运行的所在目录的指定位置：
            "txt_files/pi_digits.txt"
        3. 绝对路径通常比相对路径长；
        4. 在相对路径行不通时，可以使用绝对路径；
        5. 代码中应该始终使用斜杠"/"来表示路径；
            5.1 Windows 系统使用反斜杠来表示路径，但我们不需要关心，
                pathlib 库会自动使用正确的路径表示方法；
"""
# 在可处理的数据量方面，Python 没有任何限制，只受限于系统的内存
# in 操作符，既可以用来判断元素是否在列表或者元祖中，也可以用来查找 substr 字符串是否存在


from pathlib import Path  # 从 pathlib 库导入 Path 类

path = Path(
    "txt_files/pi_digits.txt"
)  # 使用 Path 类来创造实例 path，需要属性：文件相对路径

# Open the file in text mode, read it, and close the file.
contents = path.read_text().rstrip()  # 访问文件的所有内容并删除末尾空格
# print(f"pi_digits.txt contents is {contents}")

# 将获取到的（整个文件的内容）切分为（由行组成的列表）
lines = contents.splitlines()
# print(f"lines type is {type(lines)}")  # lines type is <class 'list'>
pi_string = ""

for line in lines:
    # print(f"lin content is {line}")
    pi_string += line.lstrip()
# print(f"pi_string(first fifty-two letters) is {pi_string[:52]}")
# print(f"pi_string length is {len(pi_string)}, file lens is {len(lines)}")

birthday_date = "930918"
if birthday_date in pi_string:
    # print(f"Your birthday {birthday_date} appears in the first million digits of pi!")
    ...
else:
    # print("Your birthday does not appear in the first million digits of pi!")
    ...

# 如果指向的文件不存在，会新建指定路径的这个文件
path = Path("./txt_files/programming.txt") 
path.write_text("I love programming!")
path.write_text("I love programming!")
path.write_text("I love programming!")
path.write_text("asdf") # 会完全替换原有内容，也就是只保留最新的一次写入的内容
# path.write_text(2342) # TypeError: data must be str, not int

# 写入多行内容的方式, 使用 += 追加字符串
contents = "I love programming!\n"
contents += "I love Python!\n"
contents += "I love Javascript!\n"
contents += "I love Swift!\n"
path.write_text(contents)

