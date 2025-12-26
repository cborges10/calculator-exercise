pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }

    stages {
        11stage('Test') {
            steps {
                echo 'Testing...'
                sh 'python3 test_calculator.py'
            }
        }
    }
    post {
        always {
            echo 'This will always run after the stages.'
        }
    }
}