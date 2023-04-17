## Linux 命令
- [cat](cat.md)

## 命令工具
1. [在线的 wangchujiang.com/linux-command](https://wangchujiang.com/linux-command/)  
   > https://github.com/jaywcjlove/linux-command
   
1. [pls](https://github.com/chenjiandongx/pls/releases)
   > https://github.com/chenjiandongx/pls 一个 go 程序的壳，显示 linux-command 的命令
   > https://github.com/jaywcjlove/linux-command.git

   Usage
    ```shell
    pls upgrade -d /path/of/commands
    # <Ctrl C> 终止掉，因为会失败
    git clone https://gitclone.com/github.com/jaywcjlove/linux-command.git
    cp linux-command/command/* /path/of/commands
    pls show cat
    pls show apt
    ```