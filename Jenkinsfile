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
          export PIP_BREAK_SYSTEM_PACKAGES=1
          python3 -m pip install flask selenium pytest webdriver-manager requests
          python3 -m pip list
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

