# 安装Node.js

[官网下载](https://nodejs.org/en)安装。

## 升级 Node.js

方法1： [官网下载安装](https://nodejs.org/en)
方法2： 使用NPM更新

```shell
node -v  # 检查版本号
npm cache clean -f  # 清除PM缓存
npm install -g n  # 全局安装 n
sudo n stable  # 安装最新稳定版， 安装最新版：sudo n latest，指定版本安装：sudo n 18.17.1
```
