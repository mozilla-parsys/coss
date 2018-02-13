@Library('partinfra-libs') _

node('master') {
    slackSend color: 'good', message: "Starting build ${BUILD_NUMBER} for ${JOB_NAME} | <${BUILD_URL}changes | Changes>"
}

node('mesos') {
    def image
    def app_id = "parsys_cms"
    def dockerRegistry = "docker-registry.ops.mozilla.community:443"

    stage('Prep') {
        checkout scm
        gitCommit = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
    }

    stage('Build') {
        try {
            image = docker.build(app_id + ":" + gitCommit)
        }
        catch(e) {
            currentBuild.result = "FAILURE"
            slackSend color: 'bad', message: "Error building ${JOB_NAME} ${BUILD_NUMBER} | <${BUILD_URL}console | Console>"
            throw e
        }
    }

    stage('Push') {
        try {
            sh "docker tag ${image.imageName()} " + dockerRegistry + "/${image.imageName()}"
            sh "docker push " + dockerRegistry + "/${image.imageName()}"
        }
        catch(e) {
            currentBuild.result = "FAILURE"
            slackSend color: 'bad', message: "Error pushing ${JOB_NAME} ${BUILD_NUMBER} | <${BUILD_URL}console | Console>"
            throw e
        }
    }
}
