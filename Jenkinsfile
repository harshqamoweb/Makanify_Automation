pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/harshqamoweb/Makanify_Automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --alluredir=allure-results'
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false,
                       jdk: '',
                       results: [[path: 'allure-results']]
            }
        }

    }
}