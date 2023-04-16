## 安装 godoc
godoc 将会安装在 `$GOPATH/bin` 目录下。
```shell
go get -v  golang.org/x/tools/cmd/godoc
```

## Go 语言文档（ web 服务）
```shell
# 默认从 $GOROOT 和 $GOPATH 查找 packages 文档 
godoc -http=:6060
# 指定 goroot 目录
godoc -http=:6060 -goroot=/path/of/go
# 也可以从 zip 文件中查找文档
godoc -http=:6060 -zip=go.zip -goroot=/path/of/go
```
通过浏览器访问 `http://localhost:6060`

## Go 语言文档（命令行）
```shell
go doc package # 获取包的文档注释, 例如： go doc fmt
go doc package/subpackage # 获取子包的文档注释, 例如：go doc container/list
go doc package function # 获取某个函数在某个包中的文档注释，例如：go doc fmt Printf
```

## 为自定义包生成文档
```shell
godoc -http=:6060 -goroot=/path/to/my/package
```

## godoc [flag]
```
The flags are:

-v
	verbose mode
-timestamps=true
	show timestamps with directory listings
-index
	enable identifier and full text search index
	(no search box is shown if -index is not set)
-index_files=""
	glob pattern specifying index files; if not empty,
	the index is read from these files in sorted order
-index_throttle=0.75
	index throttle value; a value of 0 means no time is allocated
	to the indexer (the indexer will never finish), a value of 1.0
	means that index creation is running at full throttle (other
	goroutines may get no time while the index is built)
-index_interval=0
	interval of indexing; a value of 0 sets it to 5 minutes, a
	negative value indexes only once at startup
-play=false
	enable playground
-links=true
	link identifiers to their declarations
-write_index=false
	write index to a file; the file name must be specified with
	-index_files
-maxresults=10000
	maximum number of full text search results shown
	(no full text index is built if maxresults <= 0)
-notes="BUG"
	regular expression matching note markers to show
	(e.g., "BUG|TODO", ".*")
-goroot=$GOROOT
	Go root directory
-http=addr
	HTTP service address (e.g., '127.0.0.1:6060' or just ':6060')
-analysis=type,pointer
	comma-separated list of analyses to perform
	"type": display identifier resolution, type info, method sets,
		'implements', and static callees
	"pointer": display channel peers, callers and dynamic callees
		(significantly slower)
	See https://golang.org/lib/godoc/analysis/help.html for details.
-templates=""
	directory containing alternate template files; if set,
	the directory may provide alternative template files
	for the files in $GOROOT/lib/godoc
-url=path
	print to standard output the data that would be served by
	an HTTP request for path
-zip=""
	zip file providing the file system to serve; disabled if empty
```

## 参考
> [pkg.go.dev/golang.org/x/tools/cmd/godoc](https://pkg.go.dev/golang.org/x/tools/cmd/godoc)  
> [在线 Go 语言项目文档](https://gowalker.org/)

## 链接

- [目录](README.md)
- 上一节：[]()
- 下一节：[]()