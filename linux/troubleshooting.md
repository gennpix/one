# troubleshooting

1. 检查系统重启或开机时间或时长

   ```shell
   # 开机时间
    last reboot  # 列出目前与过去登入系统的用户相关信息，比如重启 -> last reboot，关机->last shutdown
    last reboot | head -1  # 最后一次启动记录
    who -b  # 显示当前所有登陆用户的信息，-b 参数显示上次启动时间

    # 开机时长
    who -r  # 当前系统运行时长
    top  # 顶部有 up 的时间
    w  # 显示目前登入系统的用户信息，但其返回内容包含up的时间
    uptime  # 查看Linux系统负载信息，包含up的时间
    cat /proc/uptime  #  第一个值为 up 的时间
   ```
