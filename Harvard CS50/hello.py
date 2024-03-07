# Ask user for their name
# name = input("what's your name? ")
name = "what's your name? "

# Say hello to user
print("hello, " + name)

# sep=> separator
print("hi, ", "hey, ", name, sep='"', end="!!!")
print(name)

"""
    multi-line comment
"""

# print will automatically inserts space when you pass multiple arguments to print
print("hello,", name)

print("hello,", name, name)

print("hello", name, "bye")


# str => python string

# python中 '' 和 ""都可以,看个人习惯，统一就行

# 字符串插入变量的方法： f + {}, format string
print(f"hello,{name}, bye bye")

# str.strip(), remove whitespace from str(start and end position)

print("          昂哈哈哈哈       ".strip())

# python 可以链式调用方法

# str.capitalize(), capitalizing the first letter(only fist word)
print("   abc   ".strip().capitalize())

# str.title(), start with an uppercase character and the remaining characters are lowercase

print("         hello,woRld  ".strip().title())

print(input("what's your name? ").strip().title())


# Ask user for their name

# name = input("What's your name? ").strip().title()

# str.split(), return substring with sequence
first_name, last_name = name.split(" ")

# print(f"hello, {first_name}")
