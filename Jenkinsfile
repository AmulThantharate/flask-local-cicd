pipeline {
    agent any

    stages {
        stage('Checkout Source Code') {
            steps {
                git branch: 'main', url: 'https://github.com/AmulThantharate/flask-local-cicd'
            }
        }

        stage("Commit Message SHA"){
            steps {
              script {
                env.COMMIT_SHA = sh(script: "git rev-parse --short=7 HEAD", 
                  returnStdout: true
                ).trim()
              }
              echo "Commit SHA: ${env.COMMIT_SHA}"
            }
        }

        stage("Install Dependencies"){
            steps {
                script {
                  sh """
                      python3 -m venv venv
                      . venv/bin/activate
                      pip install -r requirements.txt
                  """
                }
            }
        }
    }
}
