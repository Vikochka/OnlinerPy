pipeline {
    agent any
    stages {
    stage('build') {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }

        stage('Scan') {
            steps {
              withSonarQubeEnv(installationName: 'sonarqube')
                sh '${scannerHome}/bin/sonar-scanner'
            }
        }
    }
}