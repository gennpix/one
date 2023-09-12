# brew

安装 Homebrew
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

卸载 Homebrew
`sudo /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"`

常用命令：

- `brew update` 更新 Homebrew
- `brew search package` 搜索软件包
- `brew install package` 安装软件包
- `brew uninstall package` 卸载软件包
- `brew upgrade` 升级所有软件包
- `brew upgrade package` 升级指定软件包
- `brew list` 列出已安装的软件包列表
- `brew services command package` 管理 brew 安装软件包
- `brew services list` 列出 brew 管理运行的服务
- `brew info package` 查看软件包信息
- `brew deps package` 列出软件包的依赖关系
- `brew help` 查看帮助
- `brew cleanup` 清除过时软件包
- `brew link package` 创建软件包符号链接
- `brew unlink package` 取消软件包符号链接
- `brew doctor` 检查系统是否存在问题
- `brew missing` 查看丢失依赖的软件包
