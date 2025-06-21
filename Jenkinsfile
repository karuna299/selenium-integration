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

          # Remove broken pip
          rm -rf venv/lib/python*/site-packages/pip* \
                 venv/bin/pip venv/bin/pip3

          # Bootstrap working pip
          curl -sS https://bootstrap.pypa.io/get-pip.py | python3 - --break-system-packages

          # Install all dependencies inside venv
          python3 -m pip install flask selenium pytest webdriver-manager requests

          # OUTPUT: check to ensure selenium is installed
          echo "📦 venv packages:"
          python3 -m pip list

          # Start Flask in background
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
      echo "✅ Build complete. Review logs above for pip list and test outcome."
    }
  }
}
