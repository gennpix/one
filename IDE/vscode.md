# vscode

## settings.json

```go
"go.formatTool": "goimports",
"go.goroot": "/usr/local/go",
"go.gopath": "/Users/xin/GOPATH",
```

```python
"python.formatting.provider": "black",
```

## launch.json

### 执行单个文件

```go
{
    "name": "Launch",
    "type": "go",
    "request": "launch",
    "mode": "auto",
    "program": "${file}",
    "console": "integratedTerminal",
    "env": {},
    "args": []
}
```

### 运行一个服务

```go
{
    "name": "Launch",
    "type": "go",
    "request": "launch",
    "mode": "auto",
    "program": "${workspaceFolder}",
    "env": {},
    "args": []
}
```

### 根目录/.vscode/launch.json 示例

```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "运行",
            "type": "go",
            "request": "launch",
            "mode": "auto",
            // "program": "${workspaceFolder}",
            "program": "${file}",
            "env": {},
            "args": []
        }
    ]
}
```
