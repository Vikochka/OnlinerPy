pipeline {
    agent any
    node {
     stage('SCM') {
        checkout scm
      }
    stage('SonarQube Analysis') {
        def scannerHome = tool 'SONAR_RUNNER_HOME';
        withSonarQubeEnv() {
          sh "${scannerHome}/bin/sonar-scanner"
        }
      }
    }
}