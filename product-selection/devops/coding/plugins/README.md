# CODING 插件

官方文档：[自定义团队插件产品简介](https://help.coding.net/docs/ci/plugins/customize/overview.html)

插件配置参考文档：  [声明文件 - 基本信息](https://help.coding.net/docs/ci/plugins/customize/format.html#basic)

## demo

```yaml
# 插件版本, 用于定义插件包的版本, 做版本管理使用
version: '1.0'
 
# 插件ID
id: plugin_demo
 
# 插件中文名称
name: 插件 demo
 
# 插件描述
description: 插件 demo 描述
 
# 插件分类(build: 编译,test: 测试,security: 安全,release: 发布部署,message: 消息通知,scm: 代码管理,other: 其他)
category: build
 
# 声明插件使用的参数
variables:
  # name(string): 参数名, 必须是 英文名 + 数字 + 下划线, 作为 UI 配置以及执行器使用的参数名, 在没有配置 resolve 参数时也默认为传入给插件脚本的参数名。
  - name: arg1
    # type(string): 参数类型, 用于 UI 配置时渲染不同的 UI, 同时也根据此类型, 决定执行器传入插件脚本的行为:
    #   text: 文本类型, UI 默认使用单行文本框
    #   choice: 选项类型, 使用 choice 时，需跟 options 参数一并使用, UI 默认使用下拉框
    #   bool: 布尔类型, UI 使用复选框
    type: text
    # widget(string): UI 组件类型, 除了 type 的默认 UI 类型外, 还可以根据 widget 的不同, 设定不同的组件
    # 1.type == text, 可以支持的 widget 参数:
    #     input(默认): 单行文本框
    #     textarea: 多行文本框
    #     multiline-textarea: (特殊)多行文本框, 文本框每一行是一个参数, 即参数用换行符分隔
    #     userchooser: 用户选择器, 可使用 options 设置选项
    # 2.type == choice, 可以支持的 widget 参数:
    #     select(默认): 下拉框
    #     checkbox: 复选框
    #     radio: 单选框
    #     remote-select: 远程下拉框
    # 3.type == bool, 不支持 widget 参数, UI 组件会生成一个复选框
    widget: textarea

    # default(可选, string | boolean): 默认值, 注意: 只能使用 字符串(type == text|choice) 和 布尔(type == bool) 类型
    default: default value

    # label(string): 参数中文名, 用于 UI 配置时展示。
    label: 参数1

    # help(可选, string): 帮助信息
    help: this argument help description。

    # required(可选, boolean): 是否必填
    required: true

    # placeholder(可选, string): UI 组件的 placeholder, 仅在 UI 为文本框时生效
    placeholder: 请在此文本框输入xxx

    # options(可选, object | array): UI 组件选项, 根据 type 与 widget 的不同, 可以有如下的配置
    # 1. type == choice 需要配置每个选项的 label 和 value, 示例:
    # options:
    #   - label: label1
    #     value: value1
    #   - label: label2
    #     value: value2
    # 2.type == text && widget == userchooser 可选配置, 示例:
    # options:
    #   singleton: true / false (是否单选/复选)
    #   useEnv: true / false (是否可以输入环境变量)
    # 3.resolve(可选, string | null): 调整执行器传入给脚本参数名, 默认是长参数, 即: –{name}, 可由开发者自行调整(由于可以随意定制字符串, 请注意命令行参数规范):
    #     长参数: –foo, 这是默认设置
    #     短参数: -f
    #     无参数: ~ (注意是一个波浪号), 传入参数会变化, 具体参考 type 与 传入参数值的关系中 bool 类型一节
    # 4.advanced(可选, boolean): 是否是高级选项, advanced 设置成 true, 前端会将此字段放到高级选项栏里, 只有用户展开高级选项才能看到 , 适合插件参数太多, 部分参数可以选填的情况。
  - name: arg2
    ...
  - name: env1
    ...
 
# 执行入口配置, 声明如何运行插件脚本
entry:
  # 插件执行依赖
  # install(array): 一个 数组, 声明插件脚本运行前需要执行的命令, 可以使用 variables 定义的参数占位符 $var.
  install:
    - $QCI_PLUGIN_EXECUTABLE -m pip install -r $QCI_PLUGIN_RUNTIME/requirements.txt --user
 
  # 插件环境变量
  #   env(可选, object): 插件环境变量, 可以使用 variables 定义的占位符 $var, 可以让 variables 里定义的参数通过环境变量提供给插件脚本, 而不是参数.
  env:
    ENV: $env1
 
  # 插件启动入口
  #   start(string): 声明插件脚本运行命令行, 可以使用 variables 定义的参数占位符 $var, 如果有固定参数可以一并写入.
  start: $QCI_PLUGIN_EXECUTABLE $QCI_PLUGIN_RUNTIME/run.py $arg1 $arg2 --status $QCI_PLUGIN_RUNTIME/status.json
 
  # 插件状态文件
  #   status(可选, string): 插件脚本可以写入 status.json 决定程序是否执行成功, 如没有此节点, 会根据程序的退出码判定。
  status: $QCI_PLUGIN_RUNTIME/status.json

```

## 轮询结果

[timeout及细粒度操作](https://help.coding.net/docs/ci/plugins/customize/develop.html#polling-results)

## 状态上报

[status.json](https://help.coding.net/docs/ci/plugins/customize/develop.html#report)

## coding的一些API

1. 触发任务：https://help.coding.net/docs/project-settings/service-hook/event.html#item-event
2. 获取事项详情:https://help.coding.net/openapi#ed5e299cb8fc3bd326baa1090c025d70
curl -H 'Authorization: token b7a623d860f774ae8758f0835a1ff592469114c2' https://maxoio.coding.net/open-api?Action=DescribeIssue
3. 修改事项状态：https://help.coding.net/openapi#ed5e299cb8fc3bd326baa1090c025d70
修改事项：/open-api?Action=ModifyIssue