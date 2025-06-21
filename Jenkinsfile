pipeline {
  agent any
  environment {
    VENV = "${WORKSPACE}/venv"
  }
  stages {
    stage('Checkout') {
      steps {
        // ✅ Use your actual public repo URL here:
        git url: 'https://github.com/karuna299/selenium-integration.git'
      }
    }
    stage('Setup & Launch Flask') {
      steps {
        sh '''
          python3 -m venv "${VENV}"
          . "${VENV}/bin/activate"
          pip install --upgrade pip
          pip install flask selenium pytest webdriver-manager requests
          python app.py &       # Run Flask in background
          sleep 3               # Allow it to start
        '''
      }
    }
    stage('Run Selenium Tests') {
      steps {
        sh '''
          . "${VENV}/bin/activate"
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

