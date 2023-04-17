mac下卸载了xcode，使用git等命令时就提示错误。invalid active path(Applications/Xcode.app/Contents/Developer),这种情况可以通过xcode-select --switch指定一个xcode安装路径，如果不想安装xcode,那么可以通过重置系统默认开发工具路径.

如果没有commandLineTools, 下载合适的版本：https://developer.apple.com/download/all/?q=Command%20Line%20Tools%20for%20Xcode   
然后通过xcode-select命令来重置系统默认的CommandLineTools路径，如下
解决方案
sudo xcode-select -r
xcode-select --switch /Library/Developer/CommandLineTools
xcode-select -p
