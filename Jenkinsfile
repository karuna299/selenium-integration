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

          # Step 1: bootstrap pip cleanly
          curl -sS https://bootstrap.pypa.io/get-pip.py | python3 - --break-system-packages

          # Step 2: Install dependencies smoothly
          python3 -m pip install flask selenium pytest webdriver-manager requests

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

