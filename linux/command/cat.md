## cat命令创建或覆盖文件
```shell
cat << EOF > test.sh
#!/bin/bash

echo "hello world!"
EOF
```
> EOF只是标识，不是固定的，可以换成任意字符串，比如AAA

## cat命令追加内容到文件
```shell
cat << EOF >> test.sh
echo "hello world!"
EOF
```

## cat 命令交互式操作
按行输入，可以用 Ctrl-D 快捷键输出 EOF 标识
```shell
cat > test.sh
echo "hello world!"
<Ctrl-D>
```