pipeline {
    agent any

    parameters {
        choice(name: 'SERVICE', choices: ['global-shortfall', 'evp'], description: 'Service to deploy')
        choice(name: 'DEPLOY_TO', choices: ['stage', 'prod', 'stage-and-prod'], description: 'Target deployment')
    }

    stages {
        stage('Checkout Info') {
            steps {
                echo "Branch: ${env.BRANCH_NAME}"
                echo "Service: ${params.SERVICE}"
                echo "Deploy To: ${params.DEPLOY_TO}"
            }
        }

        stage('Validate') {
            steps {
                echo "Validating pipeline folders"
                sh 'test -d dags'
                sh 'test -d spark_jobs'
                sh 'test -d configs'
            }
        }

        stage('Build Artifact') {
            steps {
                echo "Building artifact once"
                sh '''
                    mkdir -p artifact_repo
                    tar -czf artifact_repo/${SERVICE}-${BUILD_NUMBER}.tar.gz dags spark_jobs configs
                    ls -lh artifact_repo/
                '''
            }
        }

        stage('Deploy to Stage') {
            when {
                expression {
                    params.DEPLOY_TO == 'stage' || params.DEPLOY_TO == 'stage-and-prod'
                }
            }
            steps {
                echo "Deploying same artifact to STAGE"
                sh '''
                    mkdir -p deployments/stage
                    cp artifact_repo/${SERVICE}-${BUILD_NUMBER}.tar.gz deployments/stage/
                    ls -lh deployments/stage/
                '''
            }
        }

        stage('Approve Prod') {
            when {
                expression {
                    params.DEPLOY_TO == 'prod' || params.DEPLOY_TO == 'stage-and-prod'
                }
            }
            steps {
                input message: "Approve PROD deployment for ${params.SERVICE}?"
            }
        }

        stage('Deploy to Prod') {
            when {
                expression {
                    params.DEPLOY_TO == 'prod' || params.DEPLOY_TO == 'stage-and-prod'
                }
            }
            steps {
                echo "Deploying same artifact to PROD"
                sh '''
                    mkdir -p deployments/prod
                    cp artifact_repo/${SERVICE}-${BUILD_NUMBER}.tar.gz deployments/prod/
                    ls -lh deployments/prod/
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}
