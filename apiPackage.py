"""
    API:
        Application Program Interface，也就是应用接口；

    requests:
        make web requests

    ReadTimeoutError: 
        error message:
            HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.
            使用 pip3 install requests 时，及时开了 dev-sidecar 的 pip 加速，还是遇到了超时的问题
        解决方法：
            打开 dev-sidecar 的 pip 加速中配置，选” aliyun 镜像“

"""

import requests

