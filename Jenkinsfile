pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Test') {
            steps {
                echo 'Testing...'
                python3 test_calculator.py
            }
        }
    }
}