// 1. 运行: go run hello.go
//
// 2. 不同环境下的编译：
//    GOOS：目标可执行程序运行操作系统，支持 darwin，freebsd，linux，windows
//    GOARCH：目标可执行程序操作系统构架，包括 386，amd64，arm
//
//    - Mac环境:
//        - Mac上运行: go build hello.go
//        - Linux上运行: CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build hello.go
//        - Windows上运行: CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build hello.go
//    - Linux环境:
//        - Mac上运行: CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build hello.go
//        - Linux上运行: go build hello.go
//        - Windows上运行: CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build hello.go
//    - Windows环境:
//       - Mac上运行:
//		  SET CGO_ENABLED=0
//		  SET GOOS=darwin3
//		  SET GOARCH=amd64
//		  go build hello.go
//      - Linux上运行:
//        SET CGO_ENABLED=0
//        SET GOOS=linux
//        SET GOARCH=amd64
//        go build hello.go
//      - Windows上运行: go build hello.go
//
// 3. 指定可执行文件路径/名称： go build -o hello_world hello.go

package main

import "fmt"

func main() {
	fmt.Println("Hello, 世界！")
}
