"""
    Python 社区的约定是行长不要超过79个字符:
        通过 settings.json 中编辑 editor.rulers: 80 来添加一条竖线来作为视觉提示
"""

"""
    python 的字符串过长时，处理方法：
        1. 把长字符串分为多个字符串，换行写；
        2. 每一行短的字符串都需要单独添加"";
        3. 除了末尾一行外，每一行的末尾（"之外)需要添加 backslash(\);
"""
print(
    "Hello Python world!Hello Python world!Hello Python world!"\
    "Hello Python world!Hello Python world!Hello Python world!"
)

"""
    vscode 快捷键（附录B）：
        1. 缩进和取消缩进：
            a. Tab / Shift + Tab;
            b. Command + ] / Command + [;
        2. 注释：Command + /;
        3. 上下移动代码块：Alt + ↑ / Alt + ↓;
        4.显示和隐藏资源管理器（侧边栏）： Command + B;
        5. 显示和隐藏命令行终端： Ctrl + ～;
"""

"""
    寻求帮助（附录C）：
        第一步. 向他人寻求帮助之前，请回答如下三个问题，答案应尽可能的具体：
            a. 你想要做什么？；
            b. 你已经尝试了哪些方法；
            c. 结果如何？；
            其它：小黄鸭调试法、再试试、歇一歇；
        第二部. 在线搜索：
            a. 搜索完整的错误信息；
            b. stack overflow：How do I Ask a Good Question?
            c. Python 官方文档；
            d. 库官方文档；
            e. Reddit subreddit: r/learnPython;
            f. 博客;
            g. Discord: Python Discord;
            h. Slack: PySlackers;
"""