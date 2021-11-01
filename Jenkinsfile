pipeline {
    agent any
    stages {
        stage('Scan') {
            steps {
              scannerHome = tool 'SonarQube Scanner 2.8';
              withSonarQubeEnv(installationName:'sonarqube')
                sh '${scannerHome}/bin/sonar-scanner:scanner'
            }
        }
    }
}