pipeline {
  agent any
    stages {
      stage('Lint') {
        agent {
            docker {
                image 'python:3.11.3-buster'
                args '-u 0'
            }
        }
        when {
          anyOf {
            branch pattern: "feature-*"
            branch pattern: "fix-*"
          }
        }
        steps {
          sh "pip install poetry"
          sh "poetry install --with dev"
          sh "poetry run -- black --check *.py"
        }
      }
      stage('Build') {
        when {
          anyOf {
            branch pattern: "master"
            branch pattern: "feature-*"
          }
        }
        steps {
          script {
            def image = docker.build "mikholap/app_authz:${env.GIT_COMMIT}"
            docker.withRegistry('','dockerhub-mikholap') {
              image.push()
              image.push('latest')
          }
        }
      }
    }
  }
}