pipeline {
    agent any

    parameters {
        choice(name: 'ENV', choices: ['dev', 'test', 'prod'], description: 'Target environment')
        choice(name: 'SERVICE', choices: ['abp', 'shortfall'], description: 'Pipeline service')
        choice(name: 'DEPLOY_TYPE', choices: ['dag', 'spark', 'config', 'all'], description: 'Deployment type')
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Branch: ${env.BRANCH_NAME}"
                echo "Environment: ${params.ENV}"
                echo "Service: ${params.SERVICE}"
                echo "Deploy Type: ${params.DEPLOY_TYPE}"
            }
        }

        stage('Validate') {
            steps {
                sh 'test -d dags'
                sh 'test -d spark_jobs'
                sh 'test -d configs'
                sh 'test -d deploy'
            }
        }

        stage('Deploy Simulation') {
            steps {
                sh """
                echo "Starting deployment"
                echo "Environment: ${params.ENV}"
                echo "Service: ${params.SERVICE}"
                echo "Deploy Type: ${params.DEPLOY_TYPE}"

                echo "Validating folders"

                if [ "${params.DEPLOY_TYPE}" = "dag" ] || [ "${params.DEPLOY_TYPE}" = "all" ]; then
                    echo "Checking DAG path: dags/${params.SERVICE}"
                ls -la dags || true
                fi

                if [ "${params.DEPLOY_TYPE}" = "spark" ] || [ "${params.DEPLOY_TYPE}" = "all" ]; then
                    echo "Checking Spark path: spark_jobs/${params.SERVICE}"
                ls -la spark_jobs || true
                fi

                if [ "${params.DEPLOY_TYPE}" = "config" ] || [ "${params.DEPLOY_TYPE}" = "all" ]; then
                    echo "Checking config path: configs/${params.SERVICE}"
                ls -la configs || true
                fi

                echo "Simulating CDE deployment completed successfully"
                """
            }
        }   
        
    }
}
