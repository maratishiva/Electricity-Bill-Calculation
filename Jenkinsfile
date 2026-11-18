pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t electricity-app .'
            }
        }
        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f electricity-container 2>NUL'
                bat 'docker run -d -p 5000:5000 --name electricity-container electricity-app'
            }
        }
    }
}
