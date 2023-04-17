# Jenkins 运维

## 安装jenkins

## 维护

### 管理插件

[管理插件](https://www.jenkins.io/zh/doc/book/managing/plugins/)

### 重启

`JENKINS_URL/restart/`

### 时区

1. JVM参数(建议)

    ```shell
    docker run -p 8080:8080 -p 50000:50000 --name jenkins -d -v /data/jenkins:/var/jenkins_home -e JAVA_OPTS=-Duser.timezone=Asia/Shanghai jenkins/jenkins:lts
    ```

    修改后，`new Date().format('yyyyMMddHHmmss')` 就可以正确获取，日志中的时间也修改过来了。

2. 系统管理 / 脚本命令行(临时方案，不建议)

    ```groovy
    System.setProperty('org.apache.commons.jelly.tags.fmt.timeZone', 'Asia/Shanghai')
    ```

## 问题及解决方法

### 安装时无法安装插件

1. 原因是默认updateCenter不可用的
    修改updateCenter，即修改`JENKINS_HOME/hudson.model.UpdateCenter.xml`文件。当然，也可以跳过后进入jenkins再设置UC地址，只是这样还要自行选择需要安装的插件，不如安装时方便。

    ```xml
    <?xml version=‘1.0‘ encoding=‘UTF-8‘?>
    <sites>
    <site>
        <id>default</id>
        <url>https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json</url>
    </site>
    </sites>
    ```

### 安装后无法安装插件

1. 原因是默认updateCenter不可用的
    `系统管理 / 插件管理 / 高级 / 升级站点 / URL` 改成 `https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json`，点击“提交”按钮。


### update-center

1. <https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json>
2. <http://mirror.xmission.com/jenkins/updates/update-center.json>
