pipeline {
    agent {
        node {
            label 'maven'
        }
    }

    stages {
        stage('git clone') {
            steps {
                git(credentialsId: 'git-ci-user', url: 'https://xxxx.com/plugins/git/ai-operation-center/data-synchronization-flink.git', branch: 'master', changelog: true, poll: false)
            }
        }
        stage('build') {
            steps {
                container('maven') {
                    sh 'cd big-data-integration && mvn clean package  -DskipTests=true'
                }
            }
        }
        stage('docker build') {
            steps {
                container('maven') {
                    withCredentials([usernamePassword(credentialsId : 'registry' ,passwordVariable : 'DOCKER_PASSWORD' ,usernameVariable : 'DOCKER_USER' ,)]) {
                        sh '''cd big-data-integration
#set +x && mkdir -p ~/.docker && echo "$DOCKER_CONFIG" > ~/.docker/config.json

echo "$DOCKER_PASSWORD" | docker login reg.xxxxx.com --username $DOCKER_USER --password-stdin
tag=reg.xxxxx.com/bmp/bdi-service:$(date +"%Y%m%d%H%M%S")
docker build -t ${tag} .
echo "$tag"
docker push ${tag}'''
                    }
                }
            }
        }
        stage('deploy') {
            steps {
                container('maven') {
                    withCredentials([kubeconfigContent(credentialsId : 'kubeconfig' ,variable : '' ,)]) {
                        sh 'helm3 list -A'
                    }
                }
            }
        }
    }
}