# product

## 运维自动化

### Ansible

简介：简单的自动化运维管理工具，可用来自动化部署应用、配置、编排task（持续交付、无宕机更新等），通过SSH或者ZeorMQ等连接主机。
特点：基于 Python paramiko 协议库开发，分布式，无需客户端，轻量级，配置与法使用YAML及Jinja2模板语言
优点：强大的远程命令执行操作
缺点：
更新：大约每2个月发布一个版本

### Puppet

特点：Rube开发，C/S 架构，基于SSL
优点：扩展性强
缺点：远程命令执行相对较弱

### SaltStack

特点：基于 Python 开发，C/S 架构，配置语法使用YAML
优点：比 puppet 更轻量，配置脚本更简单
缺点：
