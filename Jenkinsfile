pipeline {
    agent {
        dockerContainer {
            image 'python:3.11-slim'
        }
    }
    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'python3 test_calculator.py'
            }
        }
    }
}