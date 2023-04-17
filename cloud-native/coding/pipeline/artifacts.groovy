pipeline {
    agent any
    stages {
        stage('审批') {
            steps {
                sh 'echo "待发布制品列表: ${ARTIFACTS}"'
                input(message: '本操作会将指定版本的制品标记为已发布，并晋级到生产库，请确认是否进行制品晋级?', submitter: 'your-name@domain.com')
            }
        }

    stage('发布制品') {
        steps {
        withCredentials([ usernamePassword(credentialsId:'xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',usernameVariable:'USERNAME',passwordVariable:'PASSWORD')]) {
            sh '''for artifact in $(echo "${ARTIFACTS}" | sed \'s/,/ /g\')
do
echo "---------------------------"
echo "发布制品：${artifact}"
curl -XPOST --header \'Content-Type: application/json\' \\
--header "Authorization: Bearer ${PASSWORD}" \\
"http://<host>/open-api?Action=ReleaseArtifactVersion" \\
--data-raw "{
    \\"Action\\": \\"ReleaseArtifactVersion\\",
    \\"ProjectId\\": your-project-id,
    \\"Repository\\": \\"your-repo-name\\",
    \\"Package\\": \\"${artifact}\\",
    \\"PackageVersion\\": \\"${RELEASE_VERSION}\\"
}"
done
'''
        }

      }
    }

    stage('拉取测试制品') {
      steps {
        withCredentials([ usernamePassword(credentialsId:'xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',usernameVariable:'USERNAME',passwordVariable:'PASSWORD')
                                                                                                          ]) {
          sh '''for artifact in $(echo "${ARTIFACTS}" | sed \'s/,/ /g\')
do
echo "---------------------------"
echo "拉取制品：${artifact}"
artifact_path=$(echo $artifact|awk -F "/" {\'print $1\'})
artifact_filename=$(echo $artifact|awk -F "/" {\'print $2\'})
mkdir -p $artifact_path
curl --fail -L -u $USERNAME:$PASSWORD "http://<your-host>/<your-project-name>/<your-repo-name>/${artifact}?version=${RELEASE_VERSION}" -o $artifact
ls -l $artifact_path
done
'''
        }

      }
    }

    stage('制品推送至生产') {
      steps {
        script {
          for (artifact in ARTIFACTS.split(",")){
            codingArtifactsGeneric(files: "${artifact}", repoName: 'your-repo-name', version: "${RELEASE_VERSION}")
          }
        }

      }
    }

    stage('生产发布') {
      steps {
        withCredentials([ usernamePassword(credentialsId:'xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',usernameVariable:'USERNAME',passwordVariable:'PASSWORD')
                                    ]) {
          sh '''for artifact in $(echo "${ARTIFACTS}" | sed \'s/,/ /g\')
do
echo "---------------------------"
echo "生产发布制品：${artifact}"
curl -XPOST --header \'Content-Type: application/json\' \\
--header "Authorization: Bearer ${PASSWORD}" \\
"http://<your-host>/open-api?Action=ReleaseArtifactVersion" \\
--data-raw "{
  \\"Action\\": \\"ReleaseArtifactVersion\\",
  \\"ProjectId\\": your-project-id,
  \\"Repository\\": \\"your-repo-name\\",
  \\"Package\\": \\"${artifact}\\",
  \\"PackageVersion\\": \\"${RELEASE_VERSION}\\"
}"
done
'''
        }

      }
    }

  }
}