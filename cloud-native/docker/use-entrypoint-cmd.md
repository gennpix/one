## Java
### Dockerfile
配置参数为基本固定的，不要配置内存限制、数据库等参数，这些交给entrypoint.sh来操作。
CMD 和 ENTRYPOINT 配置部分如下所示：
```
 COPY entrypoint.sh /usr/local/bin/entrypoint.sh
 RUN chmod +x /usr/local/bin/entrypoint.sh
 CMD  ["java", "-jar", "app.jar"]
 ENTRYPOINT ["entrypoint.sh"]
```

### entrypoint.sh
不能把 JAVA_OPTS 当做一个普通的字符串用，会导致 java 无法识别参数。
```shell
#!/bin/bash
set -e
echo "input CMD: $@"
echo "JAVA_OPTS: $JAVA_OPTS"
if [ "$1" = "java" ]; then
  if [ "$JAVA_OPTS" ]; then
    java_opts_array=()
    while IFS= read -r -d "" item; do
      java_opts_array+=("$item")
    done < <([[ $JAVA_OPTS ]] && xargs printf "%s\0" <<<"$JAVA_OPTS")

    shift
    set -- java \
      "${java_opts_array[@]}" \
      "$@"
  fi
fi

echo "final CMD: $@"
exec "$@"
```

### 容器中怎么使用？
部署时，配置环境变量`JAVA_OPTS ` 即可实现自定义参数。
示例如下：
环境变量`JAVA_OPTS : -Xms128m -Xmx512m -XX:PermSize=128m -XX:MaxPermSize=128m`
Dockerfile中的 `CMD ["java", "-jar", "app.jar"]`
最终执行的命令为：`java -Xms128m -Xmx512m -XX:PermSize=128m -XX:MaxPermSize=128m -jar app.jar`
entrypoint.sh 脚本会在 `java` 和 后面的命令之间插入 `JAVA_OPTS` 自定义参数的内容。