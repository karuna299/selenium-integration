pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/karuna299/selenium-integration.git', branch: 'main'
      }
    }

    stage('Setup Node & Newman') {
      steps {
        script {
          // Use Jenkins NodeJS plugin tools
        }
        // Shell commands to ensure Node.js and Newman
        sh '''
          if ! command -v newman >/dev/null; then
            npm install -g newman
          fi
        '''
      }
    }

    stage('Run Postman Collection') {
      steps {
        sh '''
          # Run your exported Postman collection
          newman run your_collection.json \
            --environment your_environment.json \
            --reporters cli,html \
            --reporter-html-export newman-report.html \
            --disable-unicode --no-color
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'newman-report.html', allowEmptyArchive: false
      echo "✅ Newman execution completed. Check newman-report.html in workspace."
    }
  }
}
