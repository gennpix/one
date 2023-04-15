# centos

## 安装工具

```shell
# 更新源
yum clean all
yum makecache

# ping
yum install iputils

# ifconfig
yum search ifconfig
yum install net-tools[.x86_64]

# rsync
yum install rsync -y 
```
