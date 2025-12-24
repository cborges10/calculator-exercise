pipeline {
    agent { cloud 'docker-python-agent'
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