# xcode

## Xcode更新提示磁盘空间不足

检查磁盘空间
检查磁盘剩余空间十分足够，一般25-30G即可；

清空开发目录
如果磁盘空间足够，依然提示磁盘空间不足，可以尝试清空以下目录中的内容。
~/Library/Developer/CoreSimulator/Devices
~/Library/Developer/Xcode/DerivedData

## invalid active path

mac下卸载了xcode，使用git等命令时就提示错误。invalid active path(Applications/Xcode.app/Contents/Developer),这种情况可以通过xcode-select --switch指定一个xcode安装路径，如果不想安装xcode,那么可以通过重置系统默认开发工具路径。可以通过xcode-select命令来重置系统默认的CommandLineTools路径，如下：

```shell
sudo xcode-select -r
xcode-select --switch /Library/Developer/CommandLineTools
xcode-select -p
```
