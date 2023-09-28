# Pipeline 配置

## 定时构建

Build periodically 下的 Schedule 配置，扩展的 cron 格式，详情可在配置是查看。
`MINUTE HOUR DOM MONTH DOW`  --> 分钟（0-60），小时（0-23），日（1-31），月（1-12），周几（0-7,0和7都是周日）
支持时区，常用TZ： `Asia/Hong_Kong`, `UTC`，比如工作日每天12:30 和 18:30 执行：

```shell
TZ=Asia/Hong_Kong
30 12,18 * * 1-5
```
