pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -f docker-file/Dockerfile -t flask-app:v1 .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f flask-container || true
                docker run -d -p 5000:5000 --name flask-container flask-app:v1
                '''
            }
        }
    }
}
