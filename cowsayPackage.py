"""
    pip 使用遇到的问题：
    1. pip install cowsay   安装报错
            error message:
                zsh: /usr/local/bin/pip: bad interpreter  no such file or directory
            solution:
                因为安装的是python3，所以对应的，应该使用 pip3 install cowsay 😂

    2. ReadTimeoutError: pip3 被墙了
        error message:
            HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.
        solution:
            打开 dev-sidecar, 打开左下角的 pip加速，并把 pip 命令名改为：pip3
    
    3. github local can't pull and push
        because: 
            github 的 pull 和 push 时不时的就被墙了，WFT!!!😠

        solution：
            安装 dev-sidecar，使用[默认模式]，并确认打开了：代理服务、系统代理、Git.exe 代理

        [dev-sidecar](https://github.com/docmirror/dev-sidecar)
        
    4. getattr(x, 'foobar') is equivalent to x.foobar：
        这个是我看到 cowsay 有很多方法，可以打印不同的动物，就想着把这些方法遍历一遍把动物打印出来看看
        所以我需要实现 cowsay[type] 这样的逻辑，查找之后发现可以这样实现：
            getattr(cowsay, type)
        这样就相当于是 cowsay.type 而 type 可以是我 typeList 中的每一个动态的元素，这是我自己实现的嗷😄
    
    5. 生产环境下什么场景下会用到 sys.argv ?
        总是有各种各样的情况，需要区别的运行同一个文件，而 sys.argv 给我们提供了一个更快捷的方式来指定运行 program 的方式
"""


import cowsay # import third-party package
import sys # import python built-in module

# cowsay.cow("hello, world".title())

# if len(sys.argv) == 2:
#     cowsay.cow(f"hello, world, I'm {sys.argv[1]}")
# else:
#     cowsay.trex(f"hello, world, I'm {sys.argv[1]}")

my_fish = r'''
\
 \  
        /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´
'''

# cowsay.draw('Sharks are my best friend', my_fish)



typeList = [
    'beavis', 'cheese', 'cow', 'daemon', 'dragon', 
    'fox', 'ghostbusters', 'kitty','meow', 'miki',
    'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 
    'trex', 'turkey', 'turtle', 'tux'
    ]

for type in typeList:
    getattr(cowsay, type)(f"hello, world, I'm {type}")