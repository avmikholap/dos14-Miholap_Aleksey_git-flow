pipeline {
    agent any
    stages {
        stage('Lint') {
            when {
                anyOf {
                    branch pattern:"feature-*"
                }
            }

        stage('Build') {
            steps {
                echo 'Deploying....'
            }
        }
    }
  }
}