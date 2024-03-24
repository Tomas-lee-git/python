# strip, Return a list of the substrings in the string, using sep as the separator string.
# count, Return the number of non-overlapping occurrences of substring sub in

from pathlib import Path

def count_words(file_path):
    """计算一个文件大致包含多少单词"""
    path = Path(file_path)
    file_name = file_path.split("/")[-1]
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass # 静默失败，pass 充当占位符，提示这里什么都没有做
        # print(f"Sorry, the file {path} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words_number  = len(contents.split())
        print(f"The file {file_name} has about {words_number} words.")
        
# count_words("./txt_files/alice.txt") # test function works successfully

def count_number(file_path, word):
    """计算一个单词在文件中出现了多少次"""
    path = Path(file_path)
    file_name = file_path.split("/")[-1]
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass # 静默失败，pass 充当占位符，提示这里什么都没有做
        # print(f"Sorry, the file {path} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        numbers  = contents.count(word.lower())
        print(f"The file {file_name} appear {numbers} times '{word}'.\n")