# docker

## build

```shell
tag=domain/catagory/service-name:$(date +"%Y%m%d%H%M%S")
docker build -t ${tag} . && docker push ${tag}
```

## Dockerfile

配置参数为基本固定的，不要配置内存限制、数据库等参数，这些交给entrypoint.sh来操作。
CMD 和 ENTRYPOINT 配置部分如下所示：

```shell
 COPY entrypoint.sh /usr/local/bin/entrypoint.sh
 RUN chmod +x /usr/local/bin/entrypoint.sh
 CMD  ["java", "-jar", "app.jar"]
 ENTRYPOINT ["entrypoint.sh"]
```

## login

`echo "$DOCKER_PASSWORD" | docker login $REGISTRY -u "$DOCKER_USERNAME" --password-stdin`


# Docker

## 下载

[官方下载](https://download.docker.com/)

## 安装

### debian

```shell
dpkg -i /path/to/xxx.deb
```

## 常用操作

### 清理

参考：[Docker 清理none镜像](https://blog.csdn.net/gxf212/article/details/89676307)

1. 清理none镜像(虚悬镜像)

    ```shell
    docker image prune
    ```

2. 清理无容器使用的镜像

    ```shell
    docker image prune -a
    docker image prune -a --filter "until=24h"  # 清理24小时前创建的
    ```

3. 清理容器

   ```shell
   docker container prune
   ```

4. 清理网络

   ```shell
   docker network prune
   ```

5. 清理一切

   ```shell
   docker system prune
   ```

## 国内镜像加速

[阿里云镜像加速器](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)

## docker desktop

可以在docker desktop上启用Kubernetes，应用会创建一个单节点的k8s集群在主机上。
可设置`Show system containers (advanced)`来控制是否让`docker ps`显示这些k8s容器，默认不显示。
