## go build
在当前目录编译生成可执行文件，注意 go build 指令会调用所有引用包的源码进行重新编译而不是使用之前pkg里的文件

## go install
主要用于安装非标准库的包文件，将源代码编译成对象文件。
类似 go build 的功能 ，但 go install 命令执行生成的可执行文件是在 $GOPATH/bin 目录中

## go get
可以理解为两个操作 git clone + go install , 执行会将远程代码clone 到 $GOPATH/src 目录中

## go fix
用于将你的 Go 代码从旧的发行版迁移到最新的发行版，它主要负责简单的、重复的、枯燥无味的修改工作，如果像 API 等复杂的函数修改，工具则会给出文件名和代码行数的提示以便让开发人员快速定位并升级代码。Go 开发团队一般也使用这个工具升级 Go 内置工具以及 谷歌内部项目的代码。go fix 之所以能够正常工作是因为 Go 在标准库就提供生成抽象语法树和通过抽象语法树对代码进行还原的功能。该工具会尝试更新当前目录下的所有 Go 源文件，并在完成代码更新后在控制台输出相关的文件名称。

## go test
轻量级的单元测试框架

## go run
运行 go 代码

## Go 性能说明
https://github.com/unknwon/the-way-to-go_ZH_CN/blob/master/eBook/03.8.md

## 与其它语言进行交互
https://github.com/unknwon/the-way-to-go_ZH_CN/blob/master/eBook/03.9.md