# JSON, Javascript Object Notation, 通用的轻量级数据格式；
# 因为文件读写都必须是 str 类型，使用 json.dumps()和 json.loads()，可以恢复数据原本的格式；


from pathlib import Path

import json

numbers = [2, 3, 5, 7, 11, 13]
# print(type(numbers)) # <class 'list'>
contents = json.dumps(numbers)
# print(type(contents)) # <class 'str'> json str
path = Path("./json_files/data.json")
path.write_text(contents) # 文件的读取和写入，数据的格式都只能是 str


contents = path.read_text()
# print(contents)
# print(type(contents)) # <class 'str'>
numbers = json.loads(contents)
# print(type(numbers)) # <class 'list'>
# print(numbers)

