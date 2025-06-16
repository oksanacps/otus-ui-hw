pipeline {
    agent {
        docker {
            image 'python:3.10.0-alpine'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        BROWSER = 'chrome'
        OPENCART_PORT = '8081'
        PHPADMIN_PORT = '8088'
        LOCAL_IP = 'host.docker.internal'
    }

    stages {
        stage('Setup Environment') {
            steps {
                sh 'apk add --no-cache docker-cli docker-compose'
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запускаем тесты через docker-compose
                    sh """
                        docker-compose up -d mariadb opencart
                        sleep 30  # Ждем запуска OpenCart
                        docker-compose run --rm tests
                    """
                }
            }
        }
    }

    post {
        always {
            // Останавливаем все контейнеры
            sh 'docker-compose down'
            
            // Публикуем Allure отчет
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-results']]
            ])
            
            // Очищаем рабочую директорию
            cleanWs()
        }
    }
} 