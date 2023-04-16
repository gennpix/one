## gofmt 格式化代码

1. gofmt 可以将你的源代码格式化成符合官方统一标准的风格
   ```shell
   gofmt -w *.go
   ```

1. gofmt 可以进行语法风格层面上的小型重构
   ```shell
   # 将源文件中没有意义的括号去掉
   gofmt -r '(a) -> a' -w *.go
   # 将源文件中多余的 len(a) 去掉
   gofmt -r 'a[n:len(a)] -> a[n:]' -w *.go
   # 将源文件中符合条件的函数的参数调换位置
   gofmt -r 'A.Func1(a,b) -> A.Func2(b,a)' -w *.go
   ```

1. flags参考 `gofmt [flags] [path ...]`
    ```
    -d
        Do not print reformatted sources to standard output.
        If a file's formatting is different than gofmt's, print diffs
        to standard output.
    -e
        Print all (including spurious) errors.
    -l
        Do not print reformatted sources to standard output.
        If a file's formatting is different from gofmt's, print its name
        to standard output.
    -r rule
        Apply the rewrite rule to the source before reformatting.
    -s
        Try to simplify code (after applying the rewrite rule, if any).
        An array, slice, or map composite literal of the form:
            []T{T{}, T{}}
        will be simplified to:
            []T{{}, {}}
        
        A slice expression of the form:
            s[a:len(s)]
        will be simplified to:
            s[a:]
        
        A range of the form:
            for x, _ = range v {...}
        will be simplified to:
            for x = range v {...}
        
        A range of the form:
            for _ = range v {...}
        will be simplified to:
            for range v {...}
    -w
        Do not print reformatted sources to standard output.
        If a file's formatting is different from gofmt's, overwrite it
        with gofmt's version. If an error occurred during overwriting,
        the original file is restored from an automatic backup.
    -cpuprofile filename
        Write cpu profile to the specified file.
    ```

## 参考
> [https://golang.org/cmd/gofmt/](https://golang.org/cmd/gofmt/)  
> [https://golang.com.cn/cmd/gofmt/](https://golang.com.cn/cmd/gofmt/)

## 链接

- [目录](README.md)
- 上一节：[]()
- 下一节：[]()