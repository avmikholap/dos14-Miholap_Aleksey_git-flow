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
        }
      }
      steps {
        sh "pip install poetry"
        sh "poetry install --with dev"
        sh "poetry run -- black --check *.py"
      }
    }
        stage('Build') {
            steps {
                echo 'Deploying....'
            }
        }
    }
  }
