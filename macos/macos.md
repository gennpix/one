# MacOS

## 快捷键入口

`Shift + Command + /`

## 效率

1. 右键`使用群组`选中时，目录前不显示`>`。
2. Finder 中`显示/隐藏`隐藏文件：`Shift + Command + .`

## 工具

### 网络

1. wifi密码查看： 打开`钥匙串访问` / `系统` / `密码` / `AirPort网络密码` / 找到`名称`和wifi相符的记录 / 打开 / `属性` / 点击`显示密码`复选框，输入账号密码即可查看。

### Finder

1. 复制文件路径
   在Finder中选择文件或文件夹，先点击鼠标右键，再按住 Option 键，选择 `将 "***" 拷贝为路径名称`

### 窗口切换

1. 不同应用 `Command + Tab`
2. 统一应用不同窗口 `Command + ~` or `Command + Shift + ~`+
3. Finder/Chrome `Ctrl + Tab`

### iterm2

```shell
# 安装 iterm2
brew install iterm2
# 安装配置 rz sz
brew install lrzsz
git clone https://github.com/aikuyun/iterm2-zmodem.git
cp iterm2-zmodem/iterm2-* /usr/local/bin
chmod +x /usr/local/bin/iterm2-*
```

1. 配置 iterm2 trigger
    Profiles --> Open Profiles，选中 Default，点击 Edit Profiles 按钮，Advanced 标签，点击 Triggers 按钮，增加如下两个 Trigger：

    ```text
    Regular expression: /*/*B0100
    Action: Run Silent Coprocess
    Parameters:/usr/local/bin/iterm2-send-zmodem.sh
    ---
    Regular expression: /*/*B00000000000000
    Action: Run Silent Coprocess
    Parameters:/usr/local/bin/iterm2-recv-zmodem.sh
    ```

2. 效率提升
   - `⌥ + Backspace` 删除一个单词: Edit Profiles > Keys > Left option key：勾选`Esc+`
   - 删除光标之前的单词或字首：`ctrl + w` 和 `⌥ + Backspace`一样
   - 按单词后退光标：Edit Profiles > Keys > Key Mappings > + 一个新的 Key Mapping, 录制 `⌥←` ，`Action`选`Send Escape Sequence`, `Esc+`填`b`
   - 按单词前进光标：Edit Profiles > Keys > Key Mappings > + 一个新的 Key Mapping, 录制 `⌥→` ，`Action`选`Send Escape Sequence`, `Esc+`填`f`
   - 新建标签：`command + t`
   - 关闭标签/分屏：`command + w`
   - 切换标签：`command + 数字` 或 `command + 左右方向键` 或 `ctrl + tab`
   - 切换全屏：`command + enter`，全屏不透明，所以相当于透明度切换。
   - 查找：`command + f`，所查找的内容会被自动复制
   - 垂直分屏：`command + d`
   - 水平分屏：`command + shift + d`
   - 切换分屏的屏幕：`command + option + 四个方向键之一` 或 `command + [` 或 `command + ]`
   - 查看历史命令：`command + ;`
   - 查看剪贴板历史：`command + shift + h`
   - 清除当前行：`ctrl + u`
   - 到行首：`ctrl + a` 或 `home`
   - 到行尾：`ctrl + e` 或 `end`
   - 上一条命令：`ctrl + p`
   - 搜索命令历史：`ctrl + r`
   - 删除到文本末尾：`ctrl + k`
   - 交换光标处文本：`ctrl + t`
   - 清屏：`command + r` 或 `ctrl + l`
   - 真清屏：`command + k`
   - 选择即复制

## 问题

1. 升级 macOS Mojave 后部分软件(如 VS Code)字体变虚的解决方法
“非 Retina” 显示器，如果升级到 Mojave 后你会发现文字不清晰了，这是因为 Mojave 默认关闭了文字次像素渲染字体，你需要在终端里执行：
`defaults write -g CGFontRenderingFontSmoothingDisabled -bool NO`
升级 macOS Mojave 新系统后，苹果默认关闭了子像素抗锯齿，导致字体变细锯齿增多。

2. 无法打开应用程，因为它来自身份不明的开发者
   系统偏好设置-安全性与隐私-选择【仍要打开】
