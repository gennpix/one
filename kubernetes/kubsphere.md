# Kubesphere

https://github.com/kubesphere

前端：https://github.com/kubesphere/console

## 提交代码

```shell
git commit -s -m "you comment"
# 记得要加-s参数
-s, --signoff         add Signed-off-by:
```

## 查看目录结构

─ ~/go/src/kubesphere.io/kubesphere 
╰─ tree -L 2
.
├── CONTRIBUTING.md
├── LICENSE
├── Makefile
├── OWNERS
├── PROJECT
├── README.md
├── README_zh.md
├── api                 // generated api swagger docs
│   ├── api-rules
│   ├── ks-openapi-spec  // ks api
│   └── openapi-spec     // ks kakernetes crd api
├── build              // dockerfile 
│   ├── ks-apiserver
│   └── ks-controller-manager
├── cmd                // command line  入口
│   ├── controller-manager
│   └── ks-apiserver
├── config             // used by code-generator， kubebuilder生成的一些代码，一些yaml文件
│   ├── crd
│   ├── crds
│   ├── default
│   ├── manager
│   ├── rbac
│   ├── samples
│   └── webhook
├── doc.go
├── docs
│   ├── images
│   ├── powered-by-kubesphere.md
│   └── roadmap.md
├── go.mod
├── go.sum
├── hack               // scripts to help build ks  一些脚本，协助做一些自动化的事情
│   ├── boilerplate.go.txt
│   ├── custom-boilerplate.go.txt
│   ├── docker_build.sh
│   ├── generate_certs.sh
│   ├── generate_client.sh
│   ├── generate_group.sh
│   ├── gobuild.sh
│   ├── install_kubebuilder.sh
│   ├── lib
│   ├── lint-dependencies.sh
│   ├── pin-dependency.sh
│   ├── update-vendor-licenses.sh
│   └── update-vendor.sh
├── install         // deprecated 废弃了
│   ├── ingress-controller
│   ├── scripts
│   └── swagger-ui
├── pkg   // 源代码
│   ├── api          // 公共依赖的一些代码，单独放是为了避免循环调用，不适合放到其他包里面
│   ├── apis         // CRD package
│   ├── apiserver    // 功能模块 - ks-apiserver
│   ├── client       // used by code-generator, informer/lister/clientset  全自动生成的代码
│   ├── constants
│   ├── controller   // controllers ks-controllermgr
│   ├── db           // deprecated
│   ├── informers    
│   ├── kapis        // KubeSphere specific apis, api path starts with /kapis, ks特有的API,以kapis开头的都是ks特有的，以apis开头的，都是k8s标准的api
│   ├── models       // real business logic   真正的业务逻辑
│   ├── server
│   ├── simple       // client interface with other services, redis/ldap/es/k8s  对接第三方的接口
│   ├── test         
│   ├── tools.go
│   ├── utils
│   ├── version
│   └── webhook
├── test
│   ├── e2e
│   ├── network
│   └── testdata 
├── tools          // used to generate api doc
│   ├── cmd
│   ├── lib
│   └── tools.go
