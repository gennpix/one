// 一个简单的 webserver，用于查看执行运行目录下的文件列表、文件内容

package main

import (
	"net/http"
)

func main() {
	http.Handle("/", http.FileServer(http.Dir(".")))
	http.ListenAndServe(":8080", nil)
}
