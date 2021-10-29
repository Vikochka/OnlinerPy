pipeline {
    agent any
    stages {
      stage('build') {
        stage('Scan') {
            steps {
              def scannerHome = tool 'SonarQube Scanner 2.8';
              withSonarQubeEnv(installationName:'sonarqube')
                sh '${scannerHome}/bin/sonar-scanner:scanner'
            }
        }
      }
    }
    post {
    always {
      sh 'docker logout'
    }
  }
}