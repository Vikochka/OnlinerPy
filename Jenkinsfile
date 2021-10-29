pipeline {
    agent { label 'windows'}
    stages {
        stage('Scan') {
            steps {
              withSonarQubeEnv(installationName: 'sonarqube')
                sh "${scannerHome}/bin/sonar-scanner"
            }
        }
    }
}