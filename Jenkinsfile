pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/karuna299/selenium-integration.git', branch: 'main'
      }
    }

    stage('Setup & Launch Flask') {
      steps {
        sh '''
          # Create a fresh virtual environment
          python3 -m venv venv
          . venv/bin/activate

          # Replace broken pip inside venv (resolves PEP 668 import errors)
          rm -rf venv/lib/python*/site-packages/pip* \
                 venv/bin/pip venv/bin/pip3

          curl -sS https://bootstrap.pypa.io/get-pip.py \
            | python3 - --break-system-packages

          # Install project dependencies
          python3 -m pip install flask selenium pytest webdriver-manager requests

          # Log installed packages to verify correct installation
          python3 -m pip list

          # Start the Flask app in the background
          python3 app.py &
          sleep 3
        '''
      }
    }

    stage('Run Selenium Tests') {
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
