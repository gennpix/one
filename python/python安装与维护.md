# Python安装与维护

## 使用阿里云镜像

```shell
vi ~/.pip/pip.conf

[global]
index-url=https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```

## macOS11上多版本卸载

示例：删除本机上多余的3.6和3.8版本（保留3.7和3.9）

```shell
# 查路径
which python3
# 查版本
ls -l /usr/local/bin/python*
# 删安装包
cd /Library/Frameworks/Python.framework/Versions
sudo rm -rf 3.6
sudo rm -rf 3.8
# 删软链
rm /usr/local/bin/python3.6*
rm /usr/local/bin/python3.8*
# 删除Python程序
ls -ld /Applications/Python*
sudo rm -rf /Applications/Python\ 3.6
sudo rm -rf /Applications/Python\ 3.8
# 确保Current指向正确的版本（如果不对，使用ln命令重新创建Current的软链）
ls -l /Library/Frameworks/Python.framework/Versions
```

## 虚拟环境

推荐：[virtualenvwrapper documentation](https://virtualenvwrapper.readthedocs.io/en/latest/)

1. 安装过程(不要用sudo，否则卸载也要加sudo，也可能导致一些别的权限问题)

    ```shell
    pip3 install virtualenv
    pip3 install virtualenvwrapper
    ```

2. 配置

    ```shell
    # 创建虚拟环境目录
    mkdir ~/pyvenvs
    # 配置环境变量(不同的shell配置不同，比如bash的~/.bashrc，zsh的 ~/.zshrc，以zsh为例)
    echo "export WORKON_HOME=~/pyvenvs" >> ~/.zshrc
    echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.9" >> ~/.zshrc
    echo "export VIRTUALENVWRAPPER_VIRTUALENV==/Library/Frameworks/Python.framework/Versions/3.9/bin/virtualenv" >> ~/.zshrc
    echo "source /Library/Frameworks/Python.framework/Versions/3.9/bin/virtualenvwrapper.sh" >> ~/.zshrc
    tail -n 4 ~/.zshrc
    ```

3. 使用

    ```shell
    # 查看
    workon
    # 创建
    mkvirtualenv python-django-env
    # 切换
    workon python_django_evn
    workon python_flask_env
    # 退出
    deactivate
    # 删除
    rmvirtualenv xenv
    # 多版本支持
    mkvirtualenv -p /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7 env3.7
    ```

4. 卸载

    ```shell
    pip3 uninstall virtualenv
    pip3 uninstall virtualenvwrapper
    ```
