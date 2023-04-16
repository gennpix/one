helm
===

用于 Kubernetes 应用的包（即 Charts ）管理工具。

## 安装
在 [Github](https://github.com/helm/helm/releases) 上下载最新版即可。

以 linux-amd64 v3.5.2 为例：
```shell
wget https://get.helm.sh/helm-v3.5.2-linux-amd64.tar.gz
tar xzvf helm-v3.5.2-linux-amd64.tar.gz
cp linux-amd64/helm /usr/local/bin/helm
chmod +x /usr/local/bin/helm
```

## 参数
常用操作：
> helm search:    从 repo 查找chart  
> helm pull:      下载 chart 到当前目录  
> helm install:   部署chart 到 Kubernetes 集群  
> helm list:      列出通过 charts 部署的应用  

## 实例

helm 常用操作
```shell
helm create my-app  # 创建一个 chart
helm lint  # 检查
helm template --debug my-app # 渲染
helm install . --dry-run --debug my-app  # 调试
helm install -n ns my-app my-app/  # 安装
helm uninstall -n ns my-app # 卸载
```

## 参考资料

- [https://github.com/helm/helm](https://github.com/helm/helm)