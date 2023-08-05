# 分支合并插件

指定分支合并到目标分支。

## 任务配置

### 参数配置

SUBSYSTEM： 字符串类型，子系统
DEST_BRANCH： 单选（字符串），目标分支，自定义，建议：dev，uat、pre等
PRE_MERGE_BRANCH：单选（字符串），管理分支，范围：不使用，<预合并分支>
BRANCHES： 多选（字符串），分支列表

### Jenkinsfile配置建议

```pipeline
pipeline {
  agent any
  stages {
    stage('合并代码') {
      steps {
        withCredentials([ sshUserPrivateKey(credentialsId:'4f5da1c8-f892-4db9-a4c6-5e0be0e97146',keyFileVariable:'SSH_PRIVATE_KEY_PATH')
      ]) {
        sh 'echo 欢迎使用合并分支插件'
        useCustomStepPlugin(key: 'git-branches-merge', version: '0.1', params: [branches:'${BRANCHES}',dest_branch:'${DEST_BRANCH}',subsystem:'${SUBSYSTEM}',pre_merge_branch:'${PRE_MERGE_BRANCH}'])
      }

    }
  }
  stage('清单') {
    steps {
      sh '''cp *.tplist.json tplist.json
cp *.tplist.csv tplist.csv'''
      codingHtmlReport(name: '合并记录', path: 'tplist.json', entryFile: '')
      codingHtmlReport(name: '合并清单', path: 'tplist.csv')
    }
  }
}
}
```
