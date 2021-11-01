node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SONAR_RUNNER_HOME';
    withSonarQubeEnv() {
      bat "${scannerHome}/bin/sonar-scanner"
    }
  }
  stage('Build') {
        steps {
           git 'https://github.com/Vikochka/OnlinerPy.git'
           // To run Maven on a Windows agent, use
           bat "python test_onliner.py"
        }

  }
}