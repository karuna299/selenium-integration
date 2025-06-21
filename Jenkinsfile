pipeline {
  agent any
  environment {
    VENV = "${WORKSPACE}/venv"
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Setup & Start Flask') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install flask selenium pytest webdriver-manager requests
          python app.py &
          sleep 3
        '''
      }
    }
    stage('Run Tests') {
      steps {
        sh '''
          . venv/bin/activate
          pytest test_e2e.py --capture=no --junitxml=pytest-results.xml
        '''
      }
    }
  }
  post {
    always {
      junit 'pytest-results.xml'
      archiveArtifacts artifacts: '**/*.png', allowEmptyArchive: true
    }
  }
}
