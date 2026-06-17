pipeline {

    agent {
        label 'windows'
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
                bat '.venv\\Scripts\\python.exe -m pytest --alluredir=allure-results'
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

}