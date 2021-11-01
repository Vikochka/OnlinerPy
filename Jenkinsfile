pipeline {
    agent any
    stages {
        stage('Scan') {
            steps {
              withSonarQubeEnv(installationName:'sonarqube')
                sh 'C:/Install/sonar-scanner-cli-4.6.2.2472-windows/sonar-scanner-4.6.2.2472-windows/bin/sonar-scanner:scanner'
            }
        }
    }
}