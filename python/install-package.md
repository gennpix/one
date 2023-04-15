# install packages

## install by pip

```shell
# 安装最新版，以 requests 为例
pip3 install requests # 或 python3 -m pip install requests

# 指定版本
pip3 install requests==2.28.1 # 或 python3 -m pip install requests==2.28.1 

# 指定超时时间
python3 -m pip --default-timeout=100 install requests

# 使用国内清华源
python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
```

## upgrade pip

```shell
pip install --upgrade pip
```

## 查看已安装的 package

```shell
# 查看安装的包列表
pip3 list  # 固定格式列表
pip3 freeze  # 可指定格式

# 查看某个包，以 requests 为例
pip3 show requests
```

## Troubleshooting

1. 执行 pip 命令时，报错 "ImportError: cannot import name 'SKIP_HEADER' from pip._vender.urllib3.util"。
   解决方法：重装 pip，重装后有可能需要将报错记录中的 pip 目录删除（因为有可能安装在不同的目录）。
   - 自由环境：`curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py`
   - 受限环境：从 `https://github.com/pypa/pip` 拿到合适的源码包，解压后执行： `python setup.py build && python setup.py install`。
