# 防火墙

## 关闭防火墙

OS: CentOS

```shell
systemctl stop --now firewalld.service
systemctl disable --now firewalld.service
systemctl status firewalld.service | grep Active
```
