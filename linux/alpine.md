# alpine

## 常用命令

1. 从远程镜像源中更新本地镜像源索引 `apk update`
2. 安装PACKAGES并自动解决依赖关系 `apk add`
3. 卸载并删除PACKAGES `apk del`
4. 升级当前已安装的软件包 `apk upgrade`
5. 搜索软件包 `apk search`
6. 列出PACKAGES或镜像源的详细信息 `apk info`

## 使用国内源

```shell
echo -e "https://mirrors.aliyun.com/alpine/v3.7/main" > /etc/apk/repositories
```
