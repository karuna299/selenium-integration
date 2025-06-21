pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/karuna299/selenium-integration.git', branch: 'main'
      }
    }
    stage('Install Dependencies with pipx') {
      steps {
        sh '''
          # Install pipx if it's not installed
          if ! command -v pipx >/dev/null; then
            sudo apt-get update
            sudo apt-get install -y pipx
            pipx ensurepath
          fi

          # Globally install required tools via isolated environments
          pipx install --force flask selenium pytest webdriver-manager requests
        '''
      }
    }
    stage('Start Flask App') {
      steps {
        sh '''
          # Launch Flask app in background
          pipx run flask --app app run &
          sleep 3
        '''
      }
    }
    stage('Run Selenium Tests') {
      steps {
        sh '''
          pipx run pytest test_e2e.py --capture=no --junitxml=pytest-results.xml
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
