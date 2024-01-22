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
        
"""


import cowsay

cowsay.cow("hello, world".title())