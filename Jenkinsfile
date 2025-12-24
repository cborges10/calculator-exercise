pipeline {
    agent { label 'python'
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