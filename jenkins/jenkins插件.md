# Jenkins 插件

## 版本号

1. 扩展了每日(BUILDS_TODAY)、每周(BUILDS_THIS_WEEK)、每月(BUILDS_THIS_MONTH)、每年(BUILDS_THIS_YEAR)等的构建数等。
[Version Number](https://plugins.jenkins.io/versionnumber/)

    ```groovy
    def version = new Date().format('yyyyMMddHHmmss') + VersionNumber(versionNumberString: '_${BUILDS_TODAY}')
    ```
