pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/karuna299/selenium-integration.git', branch: 'main'
      }
    }

    stage('Setup Virtualenv & Launch Flask') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate

          # Remove broken pip from venv
          rm -rf venv/lib/python*/site-packages/pip* venv/bin/pip* venv/bin/python*-config*

          # Bootstrap pip cleanly inside venv
          curl -sS https://bootstrap.pypa.io/get-pip.py \
            | python3 - --break-system-packages

          # Install your dependencies
          python3 -m pip install flask selenium pytest webdriver-manager requests

          # Verify pip list before tests
          echo "📦 Installed packages:"
          python3 -m pip list

          # Start Flask app
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
      echo "✅ Build complete. Check logs above for test outcomes."
    }
  }
}
