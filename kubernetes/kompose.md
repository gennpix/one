# kompose

将 Docker compose 文件转换为Kubernetes 的yaml文件

[kubernetes/kompose](https://github.com/kubernetes/kompose)
[Releases · kubernetes/kompose](https://github.com/kubernetes/kompose/releases)

安装：

```shell
# Linux
curl -L https://github.com/kubernetes/kompose/releases/download/v1.17.0/kompose-linux-amd64 -o kompose
# MacOS
curl -L https://github.com/kubernetes/kompose/releases/download/v1.23.0/kompose-darwin-amd64 -o kompose

# 共同执行
chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose
```

## 自动完成

```shell
# Bash (add to .bashrc for persistence)
source <(kompose completion bash)

# Zsh (add to .zshrc for persistence)
source <(kompose completion zsh)
```

## 用法

1. 转换

    ```shell
    kompose convert -f docker-compose.yaml
    INFO Kubernetes file "frontend-service.yaml" created         
    INFO Kubernetes file "redis-master-service.yaml" created     
    INFO Kubernetes file "redis-slave-service.yaml" created      
    INFO Kubernetes file "frontend-deployment.yaml" created      
    INFO Kubernetes file "redis-master-deployment.yaml" created  
    INFO Kubernetes file "redis-slave-deployment.yaml" created 
    ```

2. 直接运行

    ```shell
    kompose up
    ```

## 转换后修改

- [Deployments](https://kubernetes.io/zh/docs/concepts/workloads/controllers/deployment/)

- 增加[resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)配置

    ```yaml
    resources:
        requests:
            memory: "64Mi"
            cpu: "250m"
        limits:
            memory: "128Mi"
            cpu: "500m"
    ```

- 如果有配置，比如环境变量，需要增加[configmap](https://kubernetes.io/docs/concepts/configuration/configmap/)

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
    name: game-demo
    data:
        # property-like keys; each key maps to a simple value
        player_initial_lives: "3"
        ui_properties_file_name: "user-interface.properties"
        # file-like keys
        game.properties: |
            enemy.types=aliens,monsters
            player.maximum-lives=5    
        user-interface.properties: |
            color.good=purple
            color.bad=yellow
            allow.textmode=true   
    ```

- [secret](https://kubernetes.io/docs/concepts/configuration/secret/)

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
    name: secret-sa-sample
    annotations:
        kubernetes.io/service-account.name: "sa-name"
    type: kubernetes.io/service-account-token
    data:
        # You can include additional key value pairs as you do with Opaque Secrets
        extra: YmFyCg==
    ```

- [volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
    [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
    [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

- [Ingress](https://kubernetes.io/zh/docs/concepts/services-networking/ingress/)