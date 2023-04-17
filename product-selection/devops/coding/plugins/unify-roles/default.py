# coding:utf8

default_host = ""
default_headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json;charset=UTF-8",
    "x-xsrf-token": "xxx-xxx-xxx",
    "cookie": "xxxxx",
    "Referer": "http://xxx.xxxx.xxx.com/p/xxxx",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}

if __name__ == "__main__":
    import json

    print(json.dumps(default_headers))
