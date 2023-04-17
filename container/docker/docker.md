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
