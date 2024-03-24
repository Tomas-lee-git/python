from pathlib import Path

import json

from write_and_read import write, read


def get_stored_user_info(path):
    """获取用户名称，向用户打招呼"""
    user_info = read(path)
    return user_info  # 函数如果没有返回值，就没办法测试了


def get_new_user_info(path, name=None):
    """引导用户输入，存储用户名称、性别、年龄"""
    if name:  # 避免新用户重复输入两次姓名，莫名其妙😕
        username = name
    else:
        username = input("What's your name? ").title()
    gender = input("What's your gender? ")
    age = input("What's your age? ")
    user_info = {
        "username": username,
        "gender": gender,
        "age": age,
    }
    write(path, user_info)
    return user_info


def greet_user(path):
    """判断是否存在正确的用户名，有的话和用户打招呼，没有的话进行存储"""
    name = input("What's your name ? ").title()
    # Path(path).exists() will return bool to indicate whither the file exists
    if Path(path).exists():  # 判断存储用户名称的文件是否存在
        user_info = get_stored_user_info(path)
        username = user_info["username"]
        if name == username:  # 判断登录的用户和存储的用户信息是否一致
            print(f"Welcome back, {username}!")  # 如果一致就读取
        else:  # 否则就存储新的用户信息
            user_info = get_new_user_info(path, name)
            username = user_info["username"]
            gender = user_info["gender"]
            age = user_info["age"]
            print(
                f"We'll remember your info when you com back: {username, gender, age}!"
            )
    else:
        user_info = get_new_user_info(path)
        username = user_info["username"]
        gender = user_info["gender"]
        age = user_info["age"]
        print(f"We'll remember your info when you com back: {username, gender, age}!")


greet_user("./json_files/name.json")
