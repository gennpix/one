# K8S debug

使用 telepresence

示例：替换KubeSphere集群内的ks-apiserver进行测试

```shell
sudo telepresence --namespace kubesphere-system --swap-deployment ks-apiserver
```
