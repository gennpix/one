jq 命令

# 获取返回值

```shell
#!/bin/bash

is_running() {
    pid=`ps -ef|grep "/Applications/Visual Studio Code.app/Contents/MacOS/Electron" | grep -v grep | awk '{print $2}'`
    if [ -z "$pid" ]; then
        # return "empty"
        return 0
    fi
    return 258
    return "$pid"
}

is_running
echo $?
# ret=$(is_running)
# echo "ret: $ret"
```

获取返回值

```shell
1）获取返回值
返回值使用$?接收

function myfunc()
{
     return $1 + $2
}
 
myfunc 2 3
echo $?
2）获取标准输出
function myfunc()
{
echo $1+$2
}

echo $(myfunc 1 2)

ret = $(myfunc 1 2)
echo $ret
```

https://blog.csdn.net/iteye_11539/article/details/82407532
https://blog.csdn.net/ithomer/article/details/6836382
https://blog.csdn.net/ithomer/article/details/6120376
https://blog.csdn.net/ithomer/article/details/5904632
https://my.oschina.net/biner/blog/28354


```shell
# %-5s 格式为左对齐且宽度为5的字符串代替（'-'表示左对齐），不使用则默认右对齐。
# %-4.2f 格式为左对齐宽度为4，保留两位小数。
printf "%-5s %-10s %-4s\n" NO. Name Mark
printf "%-5s %-10s %-4.2f\n" 01 Tom 90.3456
# 输出
NO.   Name       Mark
01    Tom        90.35

printf "%s\n" 'hello world'
printf "%b" 'hello world\n'

printf '%q\n' 'a b c'
# 输出
a\ b\ c
```

#### 例子

```shell
# 使用 /usr/bin/printf 确保调用的不是内建命令。
# 当然，在你关闭内建printf以及确认当前环境没有printf函数的情况下，可直接使用printf，详见末尾"注意"的链接。

# 按行打印数组和关联数组的下标及值。

# 声明数组可以不加'declare -a'或'local -a'（在函数内声明的局部变量）。
arr=('line1' 'line2')
/usr/bin/printf "%s\n" ${!arr[@]}
# 输出下标
0
1
/usr/bin/printf "%s\n" ${arr[@]}
# 输出值
line1
line2

#声明关联数组（也就是字典）必须加'declare -A'或'local -A'（在函数内声明的局部变量）。
declare -A assoc_arr=(['key1']='value1' ['key2']='value2')
/usr/bin/printf "%s\n" ${!assoc_arr[@]}
# 输出键。
key2
key1
/usr/bin/printf "%s\n" ${assoc_arr[@]}
# 输出值。
value2
value1
```

看例子是最快的熟悉方法：
# cat << EOF > test.sh
> #!/bin/bash             #“shell脚本”
> #you Shell script writes here.
> EOF
 
结果：
引用# cat test.sh
#!/bin/bash
#you Shell script writes here.
 
可以看到，test.sh的内容就是cat生成的内容。
cat <<EOF >test.sh  内容 EOF 
---就是将内容写入test.sh，之前存在的内容会被覆盖掉。EOF可以换成其他符号比如EEE：cat <<EEE  >test.sh  内容 EEE
 
三、其他写法
1、追加文件
# cat << EOF >> test.sh  内容  EOF
---将内容追加到 test.sh 的后面，不会覆盖掉原有的内容
2、换一种写法
# cat > test.sh << EOF 内容  EOF
3、EOF只是标识，不是固定的
# cat << HHH > iii.txt
> sdlkfjksl
> sdkjflk
> asdlfj
> HHH
这里的“HHH”就代替了“EOF”的功能。结果是相同的。
引用# cat iii.txt
sdlkfjksl
sdkjflk
asdlfj
 
4、非脚本中
如果不是在脚本中，我们可以用Ctrl-D输出EOF的标识
# cat > iii.txt
skldjfklj
sdkfjkl
kljkljklj
kljlk
Ctrl-D
复制代码
就可以



3.递归查看某个目录的文件信息

lsof +D /filepath/filepath2/

备注: 使用了+D，对应目录下的所有子目录和文件都会被列出

1. 比使用+D选项，遍历查看某个目录的所有文件信息 的方法

lsof | grep ‘/filepath/filepath2/’

5. 列出某个用户打开的文件信息

lsof  -u username

备注: -u 选项，u其实是user的缩写

6. 列出某个程序所打开的文件信息

lsof -c mysql

备注: -c 选项将会列出所有以mysql开头的程序的文件，其实你也可以写成 lsof | grep mysql, 但是第一种方法明显比第二种方法要少打几个字符了

7. 列出多个程序多打开的文件信息

lsof -c mysql -c apache

8. 列出某个用户以及某个程序所打开的文件信息

lsof -u test -c mysql

9. 列出除了某个用户外的被打开的文件信息

lsof   -u ^root

备注：^这个符号在用户名之前，将会把是root用户打开的进程不让显示

10. 通过某个进程号显示该进行打开的文件

lsof -p 1

11. 列出多个进程号对应的文件信息

lsof -p 123,456,789

12. 列出除了某个进程号，其他进程号所打开的文件信息

lsof -p ^1

13 . 列出所有的网络连接

lsof -i

14. 列出所有tcp 网络连接信息

lsof  -i tcp

15. 列出所有udp网络连接信息

lsof  -i udp

16. 列出谁在使用某个端口

lsof -i :3306

17. 列出谁在使用某个特定的udp端口

lsof -i udp:55

特定的tcp端口

lsof -i tcp:80

18. 列出某个用户的所有活跃的网络端口

lsof  -a -u test -i

19. 列出所有网络文件系统

lsof -N

20.域名socket文件

lsof -u

21.某个用户组所打开的文件信息

lsof -g 5555

22. 根据文件描述列出对应的文件信息

lsof -d description(like 2)

23. 根据文件描述范围列出文件信息

lsof -d 2-3