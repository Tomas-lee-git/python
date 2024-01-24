"""
    self packages:
        1. python 会自动把文件名作为可以在本地引用的 package name；
        2. 可以直接通过文件名称，import 这个.py 文件中 def 的任意一个 function；
        3. 如果 import 或 from 的.py 文件中有 execute 的逻辑，在 import 或 from 时，这些方法也会直接被执行；
            tell python to go find that module, read it from top to bottom, left to right；
            为避免不必要的执行被 import 的 packages 中的 main()，可以使用变量 __name__ 来限制 main 只在执行 packages 本身时被执行；
        4. __name__:
            this is a variable automatically set by python:
                if you execute: "python3 a.py", in a.py,  __name__ == "__main__";
                if a.py is imported by other files such as b.py, in a.py, __name__ == "a";
            简单地理解：
            在内部 __name__ 是自家小名：__main__；
            出门在外，就是文件名这个大名喽；
        
        5. import multiple function from same packages/modules:
            from package/module import a, b, c, d, ……
            用 , 隔开就可以了 

"""

import sys

# from sayings import hello
# import sayings
from sayings import hello, goodbye

if(len(sys.argv) != 2):
    sys.exit()

hello(sys.argv[1])
goodbye("world")
