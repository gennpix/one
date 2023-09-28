# Instance Group

1. managed instance group
2. unmanaged instance group

## Release

### 无中断升级

对于 stateless 服务，可通过配置 --max-unavailable=0 进行更新，保证新的服务正常启动后旧的服务才被删除。

`gcloud compute instance-group managed rolling-acction replace <mig_name> --unavailable=0 --project=<project_id>`
对于 regional 的 MIG， 可配置 `--max_surg` 参数，该参数只能为 0  或者 >= region 下的 zone的数量。
