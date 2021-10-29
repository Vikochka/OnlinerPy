pipeline {
    agent any
    stages {
      stage('build') {
        stage('Scan') {
            steps {
              withSonarQubeEnv(installationName:'sonarqube')
                sh '${scannerHome}/bin/sonar-scanner:scanner'
            }
        }
      }
    }
}