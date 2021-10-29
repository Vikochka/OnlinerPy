pipeline {
    agent any
    options{
      buildDiscarder(logRotator(numToKeepStr:'5'))
    }
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