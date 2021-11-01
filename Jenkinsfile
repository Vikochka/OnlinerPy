pipeline {
    agent any
    stages {
        stage('Scan') {
            steps {
              withSonarQubeEnv(installationName:'sonarqube')
                sh '${scannerHome}/bin/sonar-scanner:scanner'
            }
        }
    }
}