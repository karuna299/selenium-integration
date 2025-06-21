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

          # Clean out broken pip installations
          rm -rf venv/lib/python*/site-packages/pip*
          rm -f venv/bin/pip venv/bin/pip3

          # Bootstrap a fresh pip bypassing PEP‑668
          curl -sS https://bootstrap.pypa.io/get-pip.py | python3 - --break-system-packages

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

