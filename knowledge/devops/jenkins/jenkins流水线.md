# jenkins流水线

## 简介

### Jenkins 流水线是什么

- 一套插件
- 提供了一组可扩展的工具
- 通过流水线 DSL 将简单到复杂的交付流水线建模为“代码”
- DSL(domain specific language 领域专用语言)

### 为什么要用流水线？

### 怎么用流水线？

- pipeline as code
  - 独立的Jenkinsfile代码库（Pipeline script from SCM，推荐）
  - 共享库的方式（系统配置/Global Pipeline Libraries）
  - 跟随代码的Jenkinsfile（多分流水线）
  - 创建一个 Jenkinsfile 并将其检入源代码控制仓库是最佳实践
    - 流水线上的代码评审/迭代
    - 对流水线进行审计跟踪
    - 流水线的单一可信数据源，能够被项目的多个成员查看和编辑
- 静态Jenkinsfile（Pipeline script）

## 流水线语法

### 声明式流水线

```pipeline
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
```

agent: 指示 Jenkins 为整个流水线分配一个执行器（在 Jenkins 环境中的任何可用代理/节点上）和工作区。没有 agent 指令的话，声明式流水线不仅无效，它也不可能完成任何工作！

- 优先选择使用
- 声明式编程模型
- 简单易用
- 隔离复杂逻辑：插件，共享库
- 将复杂的代码排除在流水线之外一直是最佳实践，声明式流水线强制执行此操作

### 脚本化流水线

```pipeline
node {
    stage('Build') {
        echo 'Building..'
    }
    stage('Test') {
        echo 'Testing..'
    }
    stage('Deploy') {
        echo 'Deploying....'
    }
}
```

node: 与声明式流水线中的 agent 做了同样的事情（分配执行器和工作区），没有 node，流水线无法工作！

- 不推荐使用
- 命令式编程模型
- 可自由嵌入groovy脚本
- 可使用groovy实现所需功能
- 过于复杂，不易阅读，不易管理
- 熟悉Groovy不甚熟悉DSL的人造轮子
- 永远不要将复杂的代码放入管道中，无论它看起来是否可行

#### 声明式流水线 vs. 脚本化流水线

当Jenkins 流水线第一次构建时, Groovy 被选为基础。 Jenkins长期使用嵌入式 Groovy引擎来为管理员和用户提供高级脚本功能。另外, Jenkins流水线的实现者发现 Groovy是 构建现在成为 "脚本化流水线" DSL的坚实基础。

由于它是一个功能齐全的编程环境, 脚本化流水线为Jenkins用户提供了大量的灵活性性和可扩展性。 Groovy学习曲线通常不适合给定团队的所有成员, 因此创造了声明式流水线来为编写Jenkins流水线提供一种更简单、更有主见的语法。

两者本质上是相同的流水线子系统。他们都是 "流水线即代码" 的持久实现。它们都能够使用构建到流水线中或插件提供的步骤。它们都能够使用共享库。

但是它们的区别在于语法和灵活性。 声明式限制了用户使用更严格和预定义的结构，使其成为更简单的持续交付流水线的理想选择。脚本化提供了很少的限制, 以至于对脚本和语法的唯一限制往往是由Groovy子集本身定义的，而不是任何特定于流水线的系统, 这使他成为权利用户和那些有更复杂需求的人的理想选择。顾名思义,声明式流水线鼓励声明式编程模型。而脚本化流水线遵循一个更命令式的编程模型。

### 语法

声明式流水线中有效的基本语句和表达式遵循与Groovy的语法同样的规则，但有以下例外:

- 流水线顶层必须是一个 block : pipeline { }
- 没有分号作为语句分隔符，每条语句都必须在自己的行上
- 块只能由 节段, 指令, 步骤, 或赋值语句组成。 *属性引用语句被视为无参方法调用。例如, input被视为 input()


### 区别普通 Groovy

为了提供 durability（耐用性）, 这意味着运行流水线可以在Jenkins master 重启后继续运行，脚本化的流水线序列化数据到主服务器。由于这个设计需求, 一些Groovy 习惯用语，比如 `collection.each { item -> /* perform operation */ }` 都不完全支持。

### 效率工具与变量

todo：这部分要细过一遍

#### 片段生成器

- JENKINS_URL/pipeline-syntax

#### 声明式指令生成器

- Declarative Directive Generator
- JENKINS_URL/directive-generator
- 生成嵌套的指令配置
- when 指令内的条件
- stage 内的 steps 或 post 内的条件如 always 或 failure

#### 全局环境变量

- JENKINS_URL/pipeline-syntax/globals
- env.PATH
- env.BUILD_ID

#### 参数

- 流水线定义的所有参数作为Map
- params.MY_PARAM_NAME

#### currentBuild

- JENKINS_URL/pipeline-syntax/globals
- currentBuild.result
- currentBuild.displayName

## Q&A

1. Jenkinsfile语法高亮
    首行增加 `#!/usr/bin/env groovy`

## 参考文档

- [Declarative vs. scripted pipelines](https://www.theserverside.com/answer/Declarative-vs-scripted-pipelines-Whats-the-difference)
- [流水线语法](https://www.jenkins.io/zh/doc/book/pipeline/syntax/)
- [Jenkins2 流水线核心语法_GitChat-CSDN博客](https://blog.csdn.net/valada/article/details/104272154)

https://www.jenkins.io/zh/doc/book/pipeline/#pipeline-concepts
https://www.jenkins.io/zh/doc/book/pipeline/getting-started/
https://www.jenkins.io/zh/doc/book/pipeline/jenkinsfile/
https://www.jenkins.io/zh/doc/book/pipeline/syntax/#%E5%A3%B0%E6%98%8E%E5%BC%8F%E6%B5%81%E6%B0%B4%E7%BA%BF
https://blog.csdn.net/valada/article/details/104272154
