pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code from branch: ${env.BRANCH_NAME}"
            }
        }

        stage('Validate') {
            steps {
                echo "Validating repo structure"
                sh 'ls -la'
                sh 'test -d dags'
                sh 'test -d spark_jobs'
                sh 'test -d configs'
                sh 'test -d deploy'
            }
        }

        stage('Build') {
            steps {
                echo "Packaging data pipeline artifacts"
            }
        }

        stage('Deploy Simulation') {
            steps {
                echo "Simulating deployment for branch: ${env.BRANCH_NAME}"
            }
        }
    }
}
