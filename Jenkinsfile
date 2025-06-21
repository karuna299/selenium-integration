pipeline {
  agent any
  environment {
    VENV = "${WORKSPACE}/venv"
  }
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main',
        url: 'https://github.com/karuna299/selenium-integration.git'
      }
    }
    stage('Setup & Launch Flask') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          python3 -m pip install --upgrade pip
          pip install --break-system-packages \
            flask selenium pytest webdriver-manager requests
          python app.py &
          sleep 3
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

