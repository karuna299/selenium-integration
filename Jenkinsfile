pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/karuna299/selenium-integration.git', branch: 'main'
      }
    }

    stage('Install & Launch Flask') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          # ... pip bootstrap and install logic ...
          python app.py &
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
      echo "Pipeline finished"
    }
  }
}
