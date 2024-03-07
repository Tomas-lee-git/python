"""
    1. API:
        Application Program Interface，也就是应用接口；

    2. requests:make web requests
        requests.get(): get data from sever，return value is response object；
        response.json(): format response to JSON；
            TypeError: 'Response' object is not subscriptable
            ❕ 如果没有经过response.json()，那 response 本身是不可订阅的，没法取值；


    3. ReadTimeoutError: 
        error message:
            HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.
            使用 pip3 install requests 时，及时开了 dev-sidecar 的 pip 加速，还是遇到了超时的问题
        解决方法：
            打开 dev-sidecar 的 pip 加速中配置，选” aliyun 镜像“；

    4. JSON: 
        JavaScript Object Notation（JavaScript 对象表示法）；
        可以跨语言实现 exchanging data；
    
    5. json: python built-in module
        json.dumps(JSON, ident=2) => dump string nicely (按指定样式，转储 JSON 内容，增强 JSON 内容的可读性)；

    6. in:
        check if a element exists in a list => element in list

    7. break vs sys.exit()
        break: break loop, such as: while、for in
        sys.exist(): terminate the whole program，look like: shutdown


"""

import sys
import json

import requests

if len(sys.argv) != 2:
    sys.exit()  # 明确地退出，可以避免不符合预期的逻辑出 bug

name = sys.argv[1]  # get artist name from sys.argv

# generate requests url
url = f"https://itunes.apple.com/search?entity=song&limit=10&term={name}"

# use requests.get(): get data from sever，return value is response object
response = requests.get(url)

# response.json(): format response to JSON
# json.dumps(JSON, ident=2) => dump string nicely (按指定样式，转储 JSON 内容，增强 JSON 内容的可读性)
# print(json.dumps(response.json(), indent=2))

results = response.json()["results"]

# 指定一个我感兴趣的 key list 😚
need_info_list = ["artistId", "artistName", "trackName"]
n = 1  # 设置一个计数器
for result in results:
    print(f"=== 第{n}首歌的信息如下：===")
    for key in result:
        if (
            key in need_info_list
        ):  # check if a value exists in a list => element in list
            print(f"{key}: {result[key]}")
    n += 1  # 更新计数器
