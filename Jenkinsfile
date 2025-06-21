pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { git 'https://your.repo/yourflask.git' }
    }
    stage('Install & Start Flask') {
      steps {
        sh 'pip install flask selenium'
        sh 'python app.py &'
        sh 'sleep 3'  // give Flask time to start
      }
    }
    stage('Run Selenium Tests') {
      steps { sh 'pytest test_e2e.py --capture=no' }
    }
    stage('Post-Cleanup') {
      steps { echo "Tests done; Flask should be shutdown" }
    }
  }
  post {
    always {
      junit '**/test_e2e.xml'
      archiveArtifacts artifacts: '**/*.png', fingerprint: true
      echo currentBuild.currentResult
    }
  }
}
