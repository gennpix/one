## 安装JDK

### 下载安装包

http://java.sun.com/javase/downloads/index.jsp.

### Linux 下安装

1. 安装到 /usr/jdk 目录
```shell
tar xzfv jdk-8u281-linux-x64.tar.gz -C /usr/jdk/
```
1. 设置环境变量
```shell
export JAVA_HOME=/usr/jdkk/jdk1.8.0_281
export PATH=$JAVA_HOME/bin:$PATH
```

### Windows 下安装
1. 双击无脑安装。
1. 设置环境变量 JAVA_HOME=C:\Program Files\Java\jdk1.8.0_281

## 参考
https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/