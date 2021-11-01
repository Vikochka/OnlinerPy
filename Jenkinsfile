pipeline {
    agent any
    stages {
        stage('Scan') {
            steps {
              withSonarQubeEnv(installationName:'sonarqube')
                sh './mvnw clean org.sonarsource.scanner.maven:sonar/maven-plugin:4.6.2.2472:sonar'
            }
        }
    }
}