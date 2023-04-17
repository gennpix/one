pipeline {
    agent any
    stages {
        stage('检出') {
            steps {
                checkout([
                        $class: 'GitSCM',
                        branches: [[name: env.GIT_BUILD_REF]],
                        userRemoteConfigs: [[
                            url: env.GIT_REPO_URL,
                            credentialsId: env.CREDENTIALS_ID
                        ]]])
                }
        }

        stage('变更检查') {
            steps {
                script {
                    if(CCI_TRIGGER_METHOD=="MANUAL"){
                        GIT_PREVIOUS_COMMIT = GIT_PREVIOUS_COMMIT_CUSTOM.trim()
                        if(GIT_PREVIOUS_COMMIT==""){
                        error("请填写GIT_PREVIOUS_COMMIT_CUSTOM变量")
                        }
                    }

                    if(GIT_PREVIOUS_COMMIT==GIT_COMMIT){
                        error("GIT_COMMIT 与 GIT_PREVIOUS_COMMIT 没有差异，不需要重新构建")
                    }

                    def gitDiffFiles = sh(script: "git diff ${GIT_PREVIOUS_COMMIT} ${GIT_COMMIT} --name-only", returnStdout: true).trim()
                    MODULES_CHANGED = ","
                    for(filePath in gitDiffFiles.split("\n")){
                        println(filePath)
                        firstDir = filePath.split("/")[0]
                        if(MODULES_CHANGED.find(","+firstDir+",")==null){
                        MODULES_CHANGED += firstDir+","
                        }
                    }
                    gitDiffFiles = sh(script: "git diff ${GIT_COMMIT} ${GIT_PREVIOUS_COMMIT} --name-only", returnStdout: true).trim()
                    for(filePath in gitDiffFiles.split("\n")){
                        println(filePath)
                        firstDir = filePath.split("/")[0]
                        if(MODULES_CHANGED.find(","+firstDir+",")==null){
                        MODULES_CHANGED += firstDir+","
                        }
                    }
                    if(MODULES_CHANGED==","){
                        currentBuild.result='ABORTED'
                        error("没有差异，取消执行")
                    }

                    println("本次变更的模块有: ${MODULES_CHANGED}")
                }

            }
        }

        stage('串行阶段') {
            steps {
                script {
                    if(MODULES_CHANGED.find(",svc,")==",svc,"){
                            // do something
                    }
                }
            }
        }


        stage('并行阶段') {
            parallel {
                stage('svc1') {
                    steps {
                        script {
                            if(MODULES_CHANGED.find(",svc1,")==",svc1,"){
                                // do something
                            }
                        }
                    }
                }

                stage('svc2') {
                    steps {
                        script {
                            if(MODULES_CHANGED.find(",svc2,")==",svc2,"){
                                // do something
                            }
                        }
                    }
                }
            }
        }
    }

    environment {
        MODULES_CHANGED = ''
    }
}