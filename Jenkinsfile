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
          python3 -m venv venv
          . venv/bin/activate

          # Clean out broken pip and reinstall a working version
          rm -rf venv/lib/python*/site-packages/pip* venv/bin/pip venv/bin/pip3
          curl -sS https://bootstrap.pypa.io/get-pip.py | python3 - --break-system-packages

          # Install requirements
          python3 -m pip install flask selenium pytest webdriver-manager requests

          echo "Installed packages:"
          python3 -m pip list

          # Start Flask
          python3 app.py &
          sleep 3
        '''
      }
    }

    stage('Run Selenium Tests') {
      steps {
        sh '''
          . venv/bin/activate
          pytest test_e2e.py --capture=no
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: '**/*.png', allowEmptyArchive: true
      echo "Build finished. Inspect logs above for test results."
    }
  }
}
