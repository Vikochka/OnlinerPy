pipeline {
    agent any
    stages {
    stage('build') {
        stage('Scan') {
            steps {
              withSonarQubeEnv('sonarqube')
                sh '${scannerHome}/bin/sonar-scanner:scanner'
            }
        }
    }
}