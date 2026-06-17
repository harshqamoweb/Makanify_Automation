pipeline {

    agent {
        label 'windows'
    }

    environment {
        HEADLESS = 'true'
    }

    stages {

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                bat '.venv\\Scripts\\python.exe -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    bat '.venv\\Scripts\\python.exe -m pytest --alluredir=allure-results'
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure(
                    includeProperties: false,
                    results: [[path: 'allure-results']]
                )
            }
        }

    }

    post {
        always {
            emailext(
                subject: "Build ${currentBuild.currentResult}: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
Build Status: ${currentBuild.currentResult}

Job Name: ${env.JOB_NAME}
Build Number: ${env.BUILD_NUMBER}

Console Output:
${env.BUILD_URL}console

Allure Report:
${env.BUILD_URL}allure
""",
                to: "harsh.qa.moweb@gmail.com"
            )
        }
    }

}