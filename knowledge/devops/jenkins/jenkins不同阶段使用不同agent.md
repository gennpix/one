# jenkins

处理用户的docker in docker 问题（改为阶段级"自定义构建环境"，参考：[根节点的工作空间，每个阶段不同 Docker](https://help.coding.net/docs/ci/ways.html)）

    ```pipeline
    pipeline {
        agent none
        stages {
            stage('Back-end') {
                agent {
                    docker {
                        image 'maven:3-alpine'
                        reuseNode 'true'
                    }
                }
                steps {
                    sh 'mvn --version'
                }
            }
            stage('Front-end') {
                agent {
                    docker {
                        image 'node:14-alpine'
                        reuseNode 'true'
                    }
                }
                steps {
                    sh 'node --version'
                }
            }
        }
    }
    ```
