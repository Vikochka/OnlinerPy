pipeline {
    agent any
    stages {
        stage('Scan') {
            steps {
                script {
                    scannerHome = tool 'SonarQube Scanner 2.8'
                }
                withSonarQubeEnv('SonarQube Scanner') {
                sh "${scannerHome}/bin/sonar-scanner"
            }
        }
    }
}